from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due date (YYYY-MM-DD): ")

            try:
                add_task(title, desc, due)
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            index = int(input("Enter task index: "))
            mark_task_as_complete(index)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            progress = calculate_progress()
            print(f"Progress: {progress:.2f}%")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()