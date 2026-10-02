"""Tests for WorkItem data models."""

import unittest
from ot.models import WorkItemMetadata, Author, Comment, WorkItem, RelationshipType, generate_uuid


class TestWorkItemMetadata(unittest.TestCase):
    def test_default_initialization(self):
        meta = WorkItemMetadata(title="Test Task")
        self.assertTrue(bool(meta.id))
        self.assertEqual(meta.title, "Test Task")
        self.assertEqual(meta.type, "task")
        self.assertEqual(meta.status, "triage")
        self.assertIsNotNone(meta.created_at)
        self.assertEqual(meta.dependencies, [])
        self.assertEqual(meta.tags, [])

    def test_serialization_and_deserialization(self):
        raw = {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "title": "Build Parser",
            "type": "feature",
            "status": "in_progress",
            "size": "medium",
            "created_at": "2026-10-02T12:00:00Z",
            "updated_at": "2026-10-02T13:00:00Z",
            "author": {"name": "Alice", "email": "alice@example.com"},
            "parent": "12345678-1234-5678-1234-567812345678",
            "dependencies": ["abcdef12-3456-7890-abcd-ef1234567890"],
            "tags": ["frontend", "parser"],
            "custom_field": "preserved",
        }
        meta = WorkItemMetadata.from_dict(raw)
        self.assertEqual(meta.id, "550e8400-e29b-41d4-a716-446655440000")
        self.assertEqual(meta.title, "Build Parser")
        self.assertEqual(meta.type, "feature")
        self.assertEqual(meta.status, "in_progress")
        self.assertEqual(meta.size, "medium")
        self.assertEqual(meta.author.name, "Alice")
        self.assertEqual(meta.author.email, "alice@example.com")
        self.assertEqual(meta.parent, "12345678-1234-5678-1234-567812345678")
        self.assertEqual(meta.dependencies, ["abcdef12-3456-7890-abcd-ef1234567890"])
        self.assertEqual(meta.tags, ["frontend", "parser"])
        self.assertEqual(meta.custom, {"custom_field": "preserved"})

        exported = meta.to_dict()
        self.assertEqual(exported["id"], raw["id"])
        self.assertEqual(exported["custom_field"], "preserved")


class TestComment(unittest.TestCase):
    def test_comment_creation_and_markdown(self):
        c = Comment(
            author=Author(name="Bob", email="bob@example.com"),
            timestamp="2026-10-02T14:00:00Z",
            body="Looks good to me!",
        )
        md = c.to_markdown()
        self.assertIn("Comment by Bob <bob@example.com> on 2026-10-02T14:00:00Z", md)
        self.assertIn("Looks good to me!", md)
        self.assertIn(f"<!-- comment-id: {c.id} -->", md)

    def test_comment_dict_roundtrip(self):
        c = Comment(
            id="1234-5678",
            author=Author(name="Bob"),
            timestamp="2026-10-02T14:00:00Z",
            body="Test body",
        )
        d = c.to_dict()
        c2 = Comment.from_dict(d)
        self.assertEqual(c2.id, "1234-5678")
        self.assertEqual(c2.author.name, "Bob")
        self.assertEqual(c2.body, "Test body")


class TestWorkItemRelationships(unittest.TestCase):
    def test_dependency_management(self):
        meta = WorkItemMetadata(id="task-1", title="Task 1")
        item = WorkItem(meta=meta)
        self.assertEqual(item.dependencies, [])

        item.add_dependency("task-2")
        self.assertEqual(item.dependencies, ["task-2"])

        # No duplicates
        item.add_dependency("task-2")
        self.assertEqual(item.dependencies, ["task-2"])

        # Cannot depend on self
        item.add_dependency("task-1")
        self.assertEqual(item.dependencies, ["task-2"])

        # Removal
        self.assertTrue(item.remove_dependency("task-2"))
        self.assertEqual(item.dependencies, [])
        self.assertFalse(item.remove_dependency("task-2"))


if __name__ == "__main__":
    unittest.main()

