"""
Task module.

Contains the Task class used by the Task Manager application.
"""


class Task:
    """Represents a single task."""

    def __init__(self, task_id, description, due_date):
        """
        Initialise a task.

        Args:
            task_id (int): Unique task identifier.
            description (str): Task description.
            due_date (str): Due date for the task.
        """
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def display_task(self):
        """Return a formatted string describing the task."""
        status = "Complete" if self.completed else "Incomplete"

        return (
            f"ID: {self.task_id}, "
            f"Task: {self.description}, "
            f"Due: {self.due_date}, "
            f"Status: {status}"
        )
