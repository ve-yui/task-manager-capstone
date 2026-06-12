"""
Unit tests for TaskManager.
"""

import unittest
from task import Task
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """Tests for TaskManager."""

    def setUp(self):
        """Create a fresh TaskManager before each test."""
        self.manager = TaskManager()
        self.manager.tasks = []

    def test_add_task(self):
        """Test adding a task."""

        task = Task(1, "Study Python", "2026-06-01")

        self.manager.add_task(task)

        self.assertEqual(len(self.manager.tasks), 1)

    def test_remove_task(self):
        """Test removing a task."""

        task = Task(1, "Study Python", "2026-06-01")

        self.manager.add_task(task)
        self.manager.remove_task(1)

        self.assertEqual(len(self.manager.tasks), 0)

    def test_update_task(self):
        """Test updating a task."""

        task = Task(1, "Old Task", "2026-06-01")

        self.manager.add_task(task)

        self.manager.update_task(
            1,
            "New Task",
            "2026-07-01"
        )

        self.assertEqual(
            self.manager.tasks[0].description,
            "New Task"
        )

    def test_mark_complete(self):
        """Test marking a task complete."""

        task = Task(1, "Study Python", "2026-06-01")

        self.manager.add_task(task)

        self.manager.mark_task_complete(1)

        self.assertTrue(
            self.manager.tasks[0].completed
        )


if __name__ == "__main__":
    unittest.main()
