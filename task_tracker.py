import sys
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description, "status": "todo"})
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")


def update_task(task_id, description):
    tasks = load_tasks()
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Invalid task ID.")


def delete_task(task_id):
    tasks = load_tasks()
    task_id = int(task_id)
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully.")


def mark_status(task_id, status):
    tasks = load_tasks()
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            save_tasks(tasks)
            print(f"Task marked as {status}.")
            return
    print("Invalid task ID.")


def list_tasks(filter_status=None):
    tasks = load_tasks()
    for task in tasks:
        if filter_status is None or task["status"] == filter_status:
            print(f"{task['id']}. {task['description']} [{task['status']}]")


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == "update" and len(sys.argv) > 3:
        update_task(sys.argv[2], " ".join(sys.argv[3:]))
    elif command == "delete" and len(sys.argv) > 2:
        delete_task(sys.argv[2])
    elif command == "mark-in-progress" and len(sys.argv) > 2:
        mark_status(sys.argv[2], "in-progress")
    elif command == "mark-done" and len(sys.argv) > 2:
        mark_status(sys.argv[2], "done")
    elif command == "list":
        list_tasks()
    elif command == "list" and len(sys.argv) > 2:
        list_tasks(sys.argv[2])
    else:
        print("Invalid command or missing arguments.")


if __name__ == "__main__":
    main()
