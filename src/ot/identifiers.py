"""Identifier generation, formatting, and resolution for Open Tasks."""

from __future__ import annotations

import re
from typing import Dict, Iterable, List, Optional, Set, Tuple
import uuid

UUID_REGEX = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    re.IGNORECASE,
)
HEX_CHARS_REGEX = re.compile(r"^[0-9a-f]+$", re.IGNORECASE)

DEFAULT_SHORT_ID_LENGTH = 6
MIN_SHORT_ID_LENGTH = 4


def generate_uuid() -> str:
    """Generate a standard UUIDv4 canonical string."""
    return str(uuid.uuid4()).lower()


def is_valid_uuid(val: str) -> bool:
    """Validate whether a string is a standard UUID."""
    if not isinstance(val, str):
        return False
    return bool(UUID_REGEX.match(val.strip()))


def clean_hex(val: str) -> str:
    """Strip hyphens and lowercase a hex or UUID string."""
    return val.replace("-", "").strip().lower()


def compute_short_id(
    target_uuid: str,
    all_uuids: Optional[Iterable[str]] = None,
    min_length: int = DEFAULT_SHORT_ID_LENGTH,
) -> str:
    """Compute a Git-style short identifier for `target_uuid`.

    If `all_uuids` is provided, ensures the short identifier is unique among the set,
    expanding length beyond `min_length` if necessary.
    """
    clean_target = clean_hex(target_uuid)
    if not clean_target:
        return ""

    if not all_uuids:
        return clean_target[:min_length]

    other_cleans: Set[str] = {
        clean_hex(u) for u in all_uuids if clean_hex(u) != clean_target
    }

    curr_len = max(min_length, MIN_SHORT_ID_LENGTH)
    while curr_len <= len(clean_target):
        prefix = clean_target[:curr_len]
        # Check collision with other UUIDs
        collision = any(other.startswith(prefix) for other in other_cleans)
        if not collision:
            return prefix
        curr_len += 1

    return clean_target


class AmbiguousIdentifierError(ValueError):
    """Raised when an identifier matches multiple items."""

    def __init__(self, query: str, matches: List[str]):
        super().__init__(
            f"Ambiguous identifier '{query}' matches multiple WorkItems: {', '.join(matches)}"
        )
        self.query = query
        self.matches = matches


class IdentifierNotFoundError(KeyError):
    """Raised when an identifier matches no items."""

    def __init__(self, query: str):
        super().__init__(f"No WorkItem found matching identifier '{query}'")
        self.query = query


def resolve_identifier(
    query: str,
    all_items_by_id: Dict[str, Any],
) -> Tuple[str, Any]:
    """Resolve a user-provided query (full UUID, short hex prefix, or title) to (uuid, item).

    Raises:
        IdentifierNotFoundError if no item matches.
        AmbiguousIdentifierError if multiple items match.
    """
    q = query.strip()
    if not q:
        raise IdentifierNotFoundError(query)

    # 1. Exact UUID match
    if q.lower() in all_items_by_id:
        return q.lower(), all_items_by_id[q.lower()]

    # Case-insensitive full UUID match
    for item_id, item in all_items_by_id.items():
        if item_id.lower() == q.lower():
            return item_id, item

    # 2. Hex prefix match against clean UUIDs
    clean_q = clean_hex(q)
    if HEX_CHARS_REGEX.match(clean_q) and len(clean_q) >= MIN_SHORT_ID_LENGTH:
        matching_ids = [
            item_id
            for item_id in all_items_by_id
            if clean_hex(item_id).startswith(clean_q)
        ]
        if len(matching_ids) == 1:
            matched_id = matching_ids[0]
            return matched_id, all_items_by_id[matched_id]
        if len(matching_ids) > 1:
            raise AmbiguousIdentifierError(query, matching_ids)

    # 3. Match by exact title or unique case-insensitive title prefix
    exact_title_matches = [
        (item_id, item)
        for item_id, item in all_items_by_id.items()
        if getattr(item, "title", None) and item.title.lower() == q.lower()
    ]
    if len(exact_title_matches) == 1:
        return exact_title_matches[0]
    if len(exact_title_matches) > 1:
        raise AmbiguousIdentifierError(query, [m[0] for m in exact_title_matches])

    raise IdentifierNotFoundError(query)
