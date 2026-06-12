"""
Task Manager module.

Contains the TaskManager class that manages task operations
and file persistence.
"""

from task import Task


class TaskManager:
    """Handles all task management functionality."""

    def __init__(self):
        """Create a TaskManager and load existing tasks."""
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        """
        Add a task.

        Args:
            task (Task): Task object to add.
        """
        self.tasks.append(task)

    def remove_task(self, task_id):
        """
        Remove a task by ID.

        Args:
            task_id (int): ID of task to remove.
        """
        self.tasks = [
            task for task in self.tasks
            if task.task_id != task_id
        ]

    def update_task(self, task_id, description, due_date):
        """
        Update a task.

        Args:
            task_id (int): Task ID.
            description (str): New description.
            due_date (str): New due date.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = description
                task.due_date = due_date

    def mark_task_complete(self, task_id):
        """
        Mark a task complete.

        Args:
            task_id (int): Task ID.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_complete()

    def save_tasks(self):
        """Save all tasks to a text file."""

        with open("tasks.txt", "w") as file:
            for task in self.tasks:

                # Store data in a format that is easy to reload
                file.write(
                    f"{task.task_id},"
                    f"{task.description},"
                    f"{task.due_date},"
                    f"{task.completed}\n"
                )

    def load_tasks(self):
        """Load tasks from tasks.txt if it exists."""

        try:
            with open("tasks.txt", "r") as file:
                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 4:
                        task_id = int(data[0])
                        description = data[1]
                        due_date = data[2]
                        completed = data[3] == "True"

                        task = Task(
                            task_id,
                            description,
                            due_date
                        )

                        task.completed = completed

                        self.tasks.append(task)

        except FileNotFoundError:
            # File does not exist yet
            pass
