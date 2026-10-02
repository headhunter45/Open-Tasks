"""Tests ensuring example work items are valid."""

import unittest
from pathlib import Path
from ot.models import WorkItemMetadata


def parse_frontmatter(content: str) -> dict:
    """Simple YAML-like frontmatter parser for basic verification."""
    lines = content.strip().split("\n")
    if not lines or lines[0] != "---":
        return {}
    fm_lines = []
    for line in lines[1:]:
        if line == "---":
            break
        fm_lines.append(line)
    # Use basic YAML parsing or line parsing
    data = {}
    current_key = None
    list_items = []
    sub_dict = {}

    import re

    for line in fm_lines:
        if line.startswith("  - "):
            item = line[4:].strip()
            list_items.append(item)
            data[current_key] = list(list_items)
        elif line.startswith("  ") and ":" in line:
            sub_k, sub_v = line.strip().split(":", 1)
            sub_dict[sub_k.strip()] = sub_v.strip()
            data[current_key] = dict(sub_dict)
        elif ":" in line:
            current_key, val = line.split(":", 1)
            current_key = current_key.strip()
            val = val.strip()
            list_items = []
            sub_dict = {}
            if val:
                data[current_key] = val
            else:
                data[current_key] = None
    return data


class TestExampleDocuments(unittest.TestCase):
    def test_examples_directory_exists(self):
        examples_dir = Path(__file__).resolve().parent.parent / "examples" / "sample-project" / ".ot" / "tasks"
        self.assertTrue(examples_dir.exists())

        task_files = list(examples_dir.rglob("index.md"))
        self.assertGreaterEqual(len(task_files), 4)

        for tf in task_files:
            content = tf.read_text(encoding="utf-8")
            data = parse_frontmatter(content)
            self.assertIn("id", data)
            self.assertIn("title", data)
            self.assertIn("type", data)
            self.assertIn("status", data)
            meta = WorkItemMetadata.from_dict(data)
            self.assertTrue(bool(meta.id))
            self.assertTrue(bool(meta.title))


if __name__ == "__main__":
    unittest.main()
