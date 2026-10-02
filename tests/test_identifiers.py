"""Tests for UUID generation, short ID generation, and identifier resolution."""

import unittest
from ot.identifiers import (
    AmbiguousIdentifierError,
    IdentifierNotFoundError,
    compute_short_id,
    generate_uuid,
    is_valid_uuid,
    resolve_identifier,
)


class DummyItem:
    def __init__(self, item_id: str, title: str):
        self.id = item_id
        self.title = title


class TestIdentifiers(unittest.TestCase):
    def test_uuid_generation_and_validation(self):
        u = generate_uuid()
        self.assertTrue(is_valid_uuid(u))
        self.assertFalse(is_valid_uuid("invalid-uuid"))
        self.assertFalse(is_valid_uuid(""))

    def test_short_id_computation_no_collisions(self):
        u1 = "550e8400-e29b-41d4-a716-446655440000"
        short = compute_short_id(u1)
        self.assertEqual(short, "550e84")

    def test_short_id_computation_with_collision_expansion(self):
        # Two UUIDs sharing a prefix
        u1 = "abcdef11-0000-0000-0000-000000000000"
        u2 = "abcdef22-0000-0000-0000-000000000000"
        all_ids = [u1, u2]

        short1 = compute_short_id(u1, all_ids)
        short2 = compute_short_id(u2, all_ids)

        self.assertEqual(short1, "abcdef1")
        self.assertEqual(short2, "abcdef2")
        self.assertNotEqual(short1, short2)

    def test_identifier_resolution_exact_uuid(self):
        u1 = "550e8400-e29b-41d4-a716-446655440000"
        item1 = DummyItem(u1, "Task 1")
        lookup = {u1: item1}

        resolved_id, resolved_item = resolve_identifier(u1, lookup)
        self.assertEqual(resolved_id, u1)
        self.assertEqual(resolved_item, item1)

    def test_identifier_resolution_short_prefix(self):
        u1 = "550e8400-e29b-41d4-a716-446655440000"
        item1 = DummyItem(u1, "Task 1")
        lookup = {u1: item1}

        resolved_id, resolved_item = resolve_identifier("550e84", lookup)
        self.assertEqual(resolved_id, u1)
        self.assertEqual(resolved_item, item1)

    def test_identifier_resolution_ambiguous(self):
        u1 = "550e8411-0000-0000-0000-000000000000"
        u2 = "550e8422-0000-0000-0000-000000000000"
        lookup = {u1: DummyItem(u1, "T1"), u2: DummyItem(u2, "T2")}

        with self.assertRaises(AmbiguousIdentifierError):
            resolve_identifier("550e84", lookup)

    def test_identifier_resolution_not_found(self):
        lookup = {"550e8400-e29b-41d4-a716-446655440000": DummyItem("550e8400-e29b-41d4-a716-446655440000", "T1")}
        with self.assertRaises(IdentifierNotFoundError):
            resolve_identifier("ffffff", lookup)


if __name__ == "__main__":
    unittest.main()
