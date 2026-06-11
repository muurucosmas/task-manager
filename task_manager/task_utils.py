from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")

def view_pending_tasks(tasks=tasks):
    found = False
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i+1}. {task['title']} (Due: {task['due_date']})")
            found = True
    if not found:
        print("No pending tasks.")

def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100