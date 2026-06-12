"""
Main entry point for the Task Manager application.
"""

from task import Task
from task_manager import TaskManager


def main():
    """Run the Task Manager application."""

    manager = TaskManager()

    while True:

        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            task_id = int(input("Task ID: "))
            description = input("Description: ")
            due_date = input("Due Date: ")

            task = Task(
                task_id,
                description,
                due_date
            )

            manager.add_task(task)

            print("Task added.")

        elif choice == "2":

            for task in manager.tasks:
                print(task.display_task())

        elif choice == "3":

            task_id = int(input("Task ID: "))
            manager.mark_task_complete(task_id)

        elif choice == "4":

            task_id = int(input("Task ID: "))
            manager.remove_task(task_id)

        elif choice == "5":

            manager.save_tasks()
            print("Tasks saved.")

        elif choice == "6":

            manager.save_tasks()
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
