# How to Run Task Tracker v2 - Quick Start Guide

## Prerequisites

- Python 3.x installed on your system
- Git (for cloning the repository)

## Installation & Quick Start

### Option 1: Using Git (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/truth05-bizz/task_tracker.git
   ```

2. **Navigate to Task Tracker v2:**
   ```bash
   cd task_tracker/Task_Trackerv2
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

   Or if you're on a system where Python 3 is explicitly required:
   ```bash
   python3 main.py
   ```

### Option 2: Direct Download

1. Download the repository as a ZIP file from GitHub
2. Extract the ZIP file
3. Open terminal/command prompt and navigate to `task_tracker/Task_Trackerv2`
4. Run `python main.py`

---

## Platform-Specific Instructions

### On Windows

```bash
# Open Command Prompt or PowerShell

git clone https://github.com/truth05-bizz/task_tracker.git
cd task_tracker\Task_Trackerv2
python main.py
```

If Python 3 is not in your PATH, you may need to specify the full path to Python:
```bash
C:\Python39\python.exe main.py
```

### On macOS

```bash
# Open Terminal

git clone https://github.com/truth05-bizz/task_tracker.git
cd task_tracker/Task_Trackerv2
python3 main.py
```

### On Linux

```bash
# Open Terminal

git clone https://github.com/truth05-bizz/task_tracker.git
cd task_tracker/Task_Trackerv2
python3 main.py
```

---

## Verify Installation

Before running, verify Python is installed:

```bash
python --version
```

Or:

```bash
python3 --version
```

You should see output like: `Python 3.x.x`

---

## Running the Application

Once started, you'll see the welcome menu:

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

### Entering Commands

1. Type one of the menu options (e.g., `add task`)
2. Press Enter
3. Follow the prompts
4. To exit, type `quit` or `exit`

---

## First Time Running

On your first run:

1. The application will create a `task_history.json` file automatically
2. This file stores all your tasks
3. You can now start adding tasks

### Test Run

Try this sequence to test the application:

```
>>> add task
Enter task: Learn Python
Description: Complete Python basics
Task status(Pending, In progress or Done): pending
Task added.

>>> show all task
------TASK LIST-------

- Learn Python

Enter task for more details.
>>> learn python

--------------------------------------
Task name: Learn Python
Task id: 1
Task status: pending
Task info: Complete Python basics
Date created: [current date and time]
Date updated: Not updated.
--------------------------------------

>>> quit
Goodbye!
```

---

## Troubleshooting

### "No such file or directory"
- Make sure you're in the `Task_Trackerv2` directory
- Run `pwd` (macOS/Linux) or `cd` (Windows) to check your location

### "ModuleNotFoundError"
- Ensure all Python files are in the same directory
- Don't rename the Python files
- You must be in the `Task_Trackerv2` folder to run the app

### "Python not found"
- Python may not be installed or not in your PATH
- Download and install from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation (Windows)

### Application doesn't start
- Check your Python version (requires Python 3.x)
- Ensure you're using `python main.py` not `python -c main.py`
- Check for typos in the file name (it's `main.py`, not `Main.py`)

---

## Features to Try

Once running, try these commands:

| Try This | Then Type |
|----------|----------|
| Add a task | `add task` |
| View all tasks | `show all task` |
| Update a task | `update task` |
| See pending tasks | `undone task` |
| See in-progress tasks | `task in progress` |
| See completed tasks | `done task` |
| Delete a task | `delete task` |
| Exit program | `quit` |

---

## File Structure

After running for the first time, you'll see:

```
Task_Trackerv2/
├── main.py
├── task.py
├── showTask.py
├── taskStatus.py
├── taskFile.py
├── taskUtilities.py
├── task_history.json        ← Created automatically
└── [other files]
```

The `task_history.json` file contains all your tasks in JSON format.

---

## Next Steps

- Read the full [README.md](./README.md) for detailed documentation
- Check [documentation.txt](./documentation.txt) for technical details
- Try all menu options to familiarize yourself with the app
- Experiment with adding, updating, and deleting tasks

---

## Tips & Tricks

💡 **Pro Tips:**

- Press Up/Down arrows in terminal to recall previous commands
- Use `quit` or `exit` to leave the application gracefully
- Tasks are automatically saved to `task_history.json`
- You can manually edit `task_history.json` with a text editor if needed
- Status values must be: `pending`, `in progress`, or `done` (case-sensitive)
- Press Enter to skip updating a field when updating a task

---

## Getting Help

If you need more information:

1. Read the full [README.md](./README.md)
2. Check [documentation.txt](./documentation.txt)
3. Review the code comments in the Python files
4. Visit the [GitHub repository](https://github.com/truth05-bizz/task_tracker)

---

## Happy Task Tracking! 🎉

You're all set! Start organizing your tasks with Task Tracker v2.

**Questions?** Check the README or documentation files for more details.