# Task Tracker v2 - README

## Overview

**Task Tracker v2** is a command-line task management application built with Python. It provides a simple yet effective way to manage your daily tasks with features like creating, updating, deleting, and filtering tasks by status.

This version represents the main implementation of the Task Tracker project, featuring a modular architecture that separates concerns across multiple Python modules for better maintainability and scalability.

---

## Features

✅ **Core Task Management**
- Create new tasks with titles and descriptions
- Update existing tasks (title, description, status)
- Delete tasks with confirmation
- View all tasks or filter by status
- Automatic task ID generation

✅ **Task Status Management**
- Track tasks as **Pending**, **In Progress**, or **Done**
- Filter tasks by status
- View undone tasks (pending + in progress)
- View all in-progress tasks
- View all completed tasks

✅ **Data Persistence**
- All tasks stored in JSON format (`task_history.json`)
- Automatic file creation on first run
- Persistent data between sessions
- Task timestamps (created, updated)

✅ **User Experience**
- Interactive command-line menu
- User-friendly task details display
- Confirmation prompts for destructive actions
- Simple and intuitive interface

---

## Project Structure

```
Task_Trackerv2/
├── main.py                    # Main entry point with menu system
├── task.py                    # Core task operations (CRUD)
├── showTask.py                # Display and view tasks
├── taskStatus.py              # Task status management
├── taskFile.py                # File path configuration
├── taskUtilities.py           # Utility functions (read/write)
├── task_history.json          # Task data storage
├── README.md                  # This file
├── HOW_TO_RUN.md              # Quick start guide
└── documentation.txt          # Technical documentation
```

---

## Module Description

### **main.py**
- Entry point for the application
- Implements the main menu loop
- Handles user input and routes to appropriate modules
- Manages the overall program flow

### **task.py**
- **add_task()** - Creates a new task with title, description, and status
- **update_task()** - Modifies an existing task's properties
- **delete_task()** - Removes a task with user confirmation
- Handles the CRUD (Create, Read, Update, Delete) operations

### **showTask.py**
- **all_task()** - Displays all tasks and allows viewing task details
- **show_task_title()** - Lists all task titles
- Provides a readable interface for viewing tasks

### **taskStatus.py**
- **all_undone_task()** - Shows tasks that are pending or in progress
- **all_task_inprogress()** - Filters and displays in-progress tasks
- **done_task()** - Shows all completed tasks
- **get_status()** - Validates and returns user-selected task status

### **taskFile.py**
- **file_path()** - Returns the path to the JSON file
- **json_file()** - Returns the filename
- Centralizes file configuration

### **taskUtilities.py**
- **read_file()** - Reads and parses JSON task data
- **write_to_file()** - Writes task data to JSON
- **task_id_settings()** - Manages and reassigns task IDs
- **formatted_task_data()** - Displays task details in a user-friendly format
- **empty_json()** - Checks if task file is empty

---

## Installation & Setup

### Prerequisites
- Python 3.x (Python 3.8 or higher recommended)
- No external dependencies required (uses only Python standard library)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/truth05-bizz/task_tracker.git
   cd task_tracker
   ```

2. **Navigate to Task Tracker v2:**
   ```bash
   cd Task_Trackerv2
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

   Or on some systems:
   ```bash
   python3 main.py
   ```

---

## Usage Guide

### Main Menu Options

When you run the application, you'll see the main menu:

```
Welcome to Task Tracker v2
----------MENU----------

- Show all task.
- Add task. 
- update task. 
- delete task. 
- undone task. 
- task in progress. 
- done task.

>>>
```

### Menu Commands

| Command | Description |
|---------|-------------|
| `show all task` | Display all tasks and view details |
| `add task` | Create a new task |
| `update task` | Modify an existing task |
| `delete task` | Remove a task (with confirmation) |
| `undone task` | Show pending and in-progress tasks |
| `task in progress` | Show tasks currently being worked on |
| `done task` | Show completed tasks |
| `quit` or `exit` | Exit the application |

### Step-by-Step Examples

#### **Adding a Task**
```
>>> add task
Enter task: Complete project report
Description: Finish the quarterly report
Task status(Pending, In progress or Done): pending
Task added.
```

#### **Viewing All Tasks**
```
>>> show all task
------TASK LIST-------

- Complete project report
- Buy groceries
- Call client

Enter task for more details.
>>> complete project report
--------------------------------------
Task name: Complete project report
Task id: 1
Task status: pending
Task info: Finish the quarterly report
Date created: Mon Jun  2 14:30:45 2026
Date updated: Not updated.
--------------------------------------
```

#### **Updating a Task**
```
>>> update task
------TASK LIST-------

- Complete project report

Enter a task to update: complete project report
--------------------------------------
Task name: Complete project report
Task id: 1
Task status: pending
Task info: Finish the quarterly report
Date created: Mon Jun  2 14:30:45 2026
Date updated: Not updated.
--------------------------------------

Enter a new title: (press Enter to keep same)
Enter status(pending, in progress, done): in progress
Enter task description: (press Enter to keep same)
file updated successfully
```

#### **Viewing Undone Tasks**
```
>>> undone task
--------------------------------------
Task name: Complete project report
Task id: 1
Task status: in progress
Task info: Finish the quarterly report
Date created: Mon Jun  2 14:30:45 2026
Date updated: Mon Jun  2 14:35:12 2026
--------------------------------------
```

#### **Deleting a Task**
```
>>> delete task
------TASK LIST-------

- Complete project report

Enter task to delete: Complete project report
Are you sure you want to delete 'Complete project report'
y/n...
>>> y
TASK:[Complete project report] deleted successfully
```

---

## Data Format

### Task Object Structure

Each task is stored as a JSON object with the following properties:

```json
{
  "title": "Task name",
  "id": 1,
  "description": "Detailed task description",
  "status": "pending",
  "createdAt": "Mon Jun  2 14:30:45 2026",
  "updated": "Mon Jun  2 14:35:12 2026"
}
```

### Task Statuses

- **pending** - Task hasn't been started
- **in progress** - Currently working on the task
- **done** - Task is completed

### Sample task_history.json

```json
[
    {
        "title": "Complete project report",
        "id": 1,
        "description": "Finish the quarterly report",
        "status": "in progress",
        "createdAt": "Mon Jun  2 14:30:45 2026",
        "updated": "Mon Jun  2 14:35:12 2026"
    },
    {
        "title": "Buy groceries",
        "id": 2,
        "description": "Milk, eggs, bread",
        "status": "pending",
        "createdAt": "Mon Jun  2 14:31:20 2026",
        "updated": null
    }
]
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'main'`
**Cause:** Running from the wrong directory  
**Solution:** Make sure you're in the `Task_Trackerv2` directory before running `python main.py`

### Issue: `FileNotFoundError: [Errno 2] No such file or directory`
**Cause:** The script is looking for `task_history.json` in the wrong location  
**Solution:** Run the script from the `Task_Trackerv2` directory. The JSON file will be created automatically.

### Issue: Menu not responding to input
**Cause:** Case sensitivity or extra spaces  
**Solution:** Input should be lowercase (e.g., `add task`, not `Add Task`). Extra spaces are automatically stripped.

### Issue: `json.JSONDecodeError`
**Cause:** The `task_history.json` file is corrupted  
**Solution:** Delete the corrupted file and restart the application. A fresh file will be created.

### Issue: Task status not accepted
**Cause:** Incorrect status format  
**Solution:** Use exactly one of these statuses: `pending`, `in progress`, or `done` (lowercase, with space for "in progress")

---

## Known Limitations

- Task IDs are automatically generated sequentially from 1 to n (cannot set custom IDs)
- No task categories or tags
- No recurring tasks
- No due dates (only creation and update timestamps)
- Single-user application (no multi-user support)
- No task priority levels
- Data stored locally (no cloud sync)

---

## Future Improvements

Planned features for future versions:

- [ ] Task priority levels (Low, Medium, High)
- [ ] Task due dates and reminders
- [ ] Task categories/tags
- [ ] Search functionality
- [ ] Task history/audit trail
- [ ] Data export (CSV, PDF)
- [ ] Configuration file support
- [ ] Task dependencies
- [ ] Recurring tasks
- [ ] Database backend (SQLite, MongoDB)
- [ ] GUI interface
- [ ] Multi-user support

---

## Technologies Used

- **Python** - Core programming language
- **JSON** - Data storage format
- **Pathlib** - File path handling
- **Datetime** - Timestamp management
- **Modular Programming** - Clean code architecture

---

## Learning Outcomes

This project helped demonstrate:

- ✓ Python functions and modules
- ✓ File I/O operations and error handling
- ✓ JSON data manipulation
- ✓ Data persistence patterns
- ✓ Command-line application design
- ✓ Separation of concerns
- ✓ Read → Modify → Write workflow
- ✓ User input validation
- ✓ Application state management

---

## Project Status

**Status:** Active Development 🚀

Task Tracker v2 is the primary implementation of the Task Tracker project and serves as a practical learning project for building maintainable Python applications.

---

## Author

Built by **Truth** as part of a personal journey into software development, computer science, and building real-world applications with Python.

**Repository:** [https://github.com/truth05-bizz/task_tracker](https://github.com/truth05-bizz/task_tracker)

---

## License

This project is open source and available for educational purposes.

---

## Questions or Issues?

If you encounter any issues or have suggestions for improvement, feel free to:
- Report issues on GitHub
- Review the [HOW_TO_RUN.md](./HOW_TO_RUN.md) for quick start guide
- Check the [documentation.txt](./documentation.txt) for technical details

---

**Last Updated:** June 2, 2026