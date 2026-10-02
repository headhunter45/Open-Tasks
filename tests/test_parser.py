"""Tests for WorkItem parser, reader, writer, and round-trip preservation."""

import tempfile
import unittest
from pathlib import Path

from ot.models import Author, Comment, WorkItem, WorkItemMetadata
from ot.parser import (
    parse_work_item_content,
    read_work_item,
    render_work_item,
    write_work_item,
)


SAMPLE_DOCUMENT = """---
id: 550e8400-e29b-41d4-a716-446655440000
title: Implement Fast Parser
type: feature
status: in_progress
size: medium
created_at: 2026-10-02T10:00:00Z
author:
  name: Alice
  email: alice@example.com
dependencies:
  - 12345678-1234-5678-1234-567812345678
tags:
  - parser
  - core
extra_custom_field: preserve_me
---

# Implement Fast Parser

## Summary
Need to build a resilient parser for Markdown work items.

## Unknown Custom Section
This custom section and notes should not be lost.

## Comments

### Comment by Bob <bob@example.com> on 2026-10-02T11:00:00Z
<!-- comment-id: c1111111-1111-1111-1111-111111111111 -->

First comment on this item.

### Comment by Charlie on 2026-10-02T12:00:00Z
<!-- comment-id: c2222222-2222-2222-2222-222222222222 -->

Second comment without email.
"""


class TestParser(unittest.TestCase):
    def test_parse_work_item_content(self):
        item = parse_work_item_content(SAMPLE_DOCUMENT)
        self.assertEqual(item.id, "550e8400-e29b-41d4-a716-446655440000")
        self.assertEqual(item.title, "Implement Fast Parser")
        self.assertEqual(item.type, "feature")
        self.assertEqual(item.status, "in_progress")
        self.assertEqual(item.meta.author.name, "Alice")
        self.assertEqual(item.meta.author.email, "alice@example.com")
        self.assertEqual(item.meta.custom, {"extra_custom_field": "preserve_me"})

        # Body contains custom sections
        self.assertIn("# Implement Fast Parser", item.body)
        self.assertIn("## Unknown Custom Section", item.body)
        self.assertIn("This custom section and notes should not be lost.", item.body)

        # Comments
        self.assertEqual(len(item.comments), 2)
        self.assertEqual(item.comments[0].id, "c1111111-1111-1111-1111-111111111111")
        self.assertEqual(item.comments[0].author.name, "Bob")
        self.assertEqual(item.comments[0].author.email, "bob@example.com")
        self.assertEqual(item.comments[0].body, "First comment on this item.")

        self.assertEqual(item.comments[1].id, "c2222222-2222-2222-2222-222222222222")
        self.assertEqual(item.comments[1].author.name, "Charlie")
        self.assertEqual(item.comments[1].body, "Second comment without email.")

    def test_write_and_read_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "MyTask" / "index.md"
            item = parse_work_item_content(SAMPLE_DOCUMENT)

            # Write to disk
            written_path = write_work_item(item, file_path)
            self.assertTrue(written_path.exists())

            # Read back from disk
            read_item = read_work_item(written_path)
            self.assertEqual(read_item.id, item.id)
            self.assertEqual(read_item.title, item.title)
            self.assertEqual(read_item.meta.custom, {"extra_custom_field": "preserve_me"})
            self.assertIn("## Unknown Custom Section", read_item.body)
            self.assertEqual(len(read_item.comments), 2)

    def test_preserve_unknown_content_after_meta_mutation(self):
        item = parse_work_item_content(SAMPLE_DOCUMENT)
        # Modify status and add a comment
        item.meta.status = "completed"
        item.comments.append(
            Comment(
                author=Author(name="Dana"),
                timestamp="2026-10-02T13:00:00Z",
                body="Task is finished.",
            )
        )

        rendered = render_work_item(item)
        self.assertIn("status: completed", rendered)
        self.assertIn("extra_custom_field: preserve_me", rendered)
        self.assertIn("## Unknown Custom Section", rendered)
        self.assertIn("Task is finished.", rendered)


if __name__ == "__main__":
    unittest.main()
