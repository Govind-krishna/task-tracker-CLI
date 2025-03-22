# Task Tracker CLI

Task Tracker CLI is a simple command-line application to manage your tasks. It allows you to add, update, delete, and list tasks using a JSON file as storage.

## Features
- Add a new task
- Update or delete a task
- Mark a task as "in-progress" or "done"
- List all tasks
- Filter tasks by status ("todo", "in-progress", "done")

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd Task-Tracker-CLI
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```
3. Run the script using Python:
   ```sh
   python task_tracker.py <command> [arguments]
   ```

## Making `task-cli` a Recognized Command (Optional)
By default, you need to run the script using `python task_tracker.py`. If you want to use `task-cli` as a command, follow these steps:

### **For Windows**
1. Create a `task-cli.bat` file in the same directory as `task_tracker.py`.
2. Add this line inside:
   ```bat
   @echo off
   python "%~dp0task_tracker.py" %*
   ```
3. Now you can run:
   ```sh
   task-cli add "Buy groceries"
   ```

### **For Linux/Mac**
1. Rename `task_tracker.py` to `task-cli`.
2. Make it executable:
   ```sh
   chmod +x task-cli
   ```
3. Move it to `/usr/local/bin` (or another directory in your `PATH`):
   ```sh
   sudo mv task-cli /usr/local/bin/
   ```
4. Now you can use:
   ```sh
   task-cli add "Buy groceries"
   ```

## Usage Examples

### Adding a new task
```sh
python task_tracker.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Updating and deleting tasks
```sh
python task_tracker.py update 1 "Buy groceries and cook dinner"
python task_tracker.py delete 1
```

### Marking a task as in-progress or done
```sh
python task_tracker.py mark-in-progress 1
python task_tracker.py mark-done 1
```

### Listing all tasks
```sh
python task_tracker.py list
```

### Listing tasks by status
```sh
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress
```

## Project Page
For more details, visit the project page: [Task Tracker](https://roadmap.sh/projects/task-tracker)

