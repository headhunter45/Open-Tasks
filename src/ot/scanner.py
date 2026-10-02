"""Repository scanner and in-memory WorkItem index."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

from ot.config import Config, load_config
from ot.discovery import find_project_root
from ot.identifiers import (
    AmbiguousIdentifierError,
    IdentifierNotFoundError,
    compute_short_id,
    resolve_identifier,
)
from ot.models import WorkItem
from ot.parser import read_work_item


class RepositoryScanner:
    """Discovers and scans WorkItem files within an Open Tasks project."""

    def __init__(self, project_root: Optional[Path | str] = None):
        self.project_root = find_project_root(project_root)

    def scan_tasks_directory(self) -> List[WorkItem]:
        """Scan .ot/tasks/ for all WorkItems."""
        if not self.project_root:
            return []

        tasks_dir = self.project_root / ".ot" / "tasks"
        if not tasks_dir.is_dir():
            return []

        work_items: List[WorkItem] = []
        for path in sorted(tasks_dir.rglob("*.md")):
            # Ignore hidden files or template directories
            if any(part.startswith(".") for part in path.parts):
                # Allow .ot itself
                rel_parts = path.relative_to(self.project_root).parts
                if any(part.startswith(".") and part != ".ot" for part in rel_parts):
                    continue

            try:
                item = read_work_item(path)
                # Only treat as WorkItem if it has a valid title or ID
                if item.meta.id:
                    work_items.append(item)
            except Exception:
                # Malformed files can be flagged by validation later
                pass

        return work_items


class WorkItemIndex:
    """In-memory index and graph of WorkItems in a project."""

    def __init__(self, items: Iterable[WorkItem]):
        self._items_by_id: Dict[str, WorkItem] = {}
        self._children_by_parent: Dict[str, List[WorkItem]] = defaultdict(list)
        self._dependents_by_dep: Dict[str, List[WorkItem]] = defaultdict(list)
        self._short_ids: Dict[str, str] = {}

        for item in items:
            self.add(item)

    def add(self, item: WorkItem) -> None:
        self._items_by_id[item.id] = item
        if item.parent_id:
            self._children_by_parent[item.parent_id].append(item)
        for dep_id in item.dependencies:
            self._dependents_by_dep[dep_id].append(item)
        self._recompute_short_ids()

    def _recompute_short_ids(self) -> None:
        all_ids = list(self._items_by_id.keys())
        self._short_ids = {
            item_id: compute_short_id(item_id, all_ids) for item_id in all_ids
        }

    def get_by_id(self, item_id: str) -> Optional[WorkItem]:
        return self._items_by_id.get(item_id)

    def get_short_id(self, item_id: str) -> str:
        return self._short_ids.get(item_id, item_id[:6])

    def resolve(self, query: str) -> WorkItem:
        """Resolve query (UUID, short ID, or title) to a WorkItem."""
        _, item = resolve_identifier(query, self._items_by_id)
        return item

    def all(self) -> List[WorkItem]:
        return list(self._items_by_id.values())

    def get_children(self, parent_id: str) -> List[WorkItem]:
        return list(self._children_by_parent.get(parent_id, []))

    def get_parent(self, item: WorkItem) -> Optional[WorkItem]:
        if item.parent_id:
            return self.get_by_id(item.parent_id)
        return None

    def get_dependencies(self, item: WorkItem) -> List[WorkItem]:
        """Return list of WorkItems that `item` depends on."""
        deps = []
        for dep_id in item.dependencies:
            dep_item = self.get_by_id(dep_id)
            if dep_item:
                deps.append(dep_item)
        return deps

    def get_dependents(self, item: WorkItem) -> List[WorkItem]:
        """Return list of WorkItems that depend on `item` (items blocked by `item`)."""
        return list(self._dependents_by_dep.get(item.id, []))

    def filter(
        self,
        item_type: Optional[str] = None,
        status: Optional[str] = None,
        size: Optional[str] = None,
        tag: Optional[str] = None,
        author_name: Optional[str] = None,
    ) -> List[WorkItem]:
        """Filter work items by criteria."""
        results = []
        for item in self.all():
            if item_type and item.type != item_type:
                continue
            if status and item.status != status:
                continue
            if size and item.meta.size != size:
                continue
            if tag and tag not in item.meta.tags:
                continue
            if author_name and (not item.meta.author or item.meta.author.name != author_name):
                continue
            results.append(item)
        return results


def load_index(start_dir: Optional[Path | str] = None) -> WorkItemIndex:
    """Scan repository and build WorkItemIndex."""
    scanner = RepositoryScanner(start_dir)
    items = scanner.scan_tasks_directory()
    return WorkItemIndex(items)
