# Task Tracker

A command-line task management application built with Python.

This repository documents my journey from planning a project to building a modular Python application. The project evolved through two versions, with each version serving a different purpose.

**Project URL:** [https://github.com/truth05-bizz/task_tracker](https://github.com/truth05-bizz/task_tracker),
https://roadmap.sh/projects/task-tracker

---

## Getting Started

### Prerequisites

- Python 3.x
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/truth05-bizz/task_tracker.git
   cd task_tracker
   ```

2. Navigate to Task Tracker v2:
   ```bash
   cd Task_Trackerv2
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

Once you run the application, you'll see the main menu with the following options:

- **Show all task** - Display all your tasks in the system
- **Add task** - Create a new task
- **Update task** - Modify an existing task
- **Delete task** - Remove a task
- **Undone task** - View all incomplete tasks
- **Task in progress** - View all tasks currently in progress
- **Done task** - View all completed tasks
- **Quit/Exit** - Exit the application

### Example Workflow

1. Start the application: `python main.py`
2. Sign up or sign in with your credentials
3. Enter `add task` to create a new task
4. Enter `show all task` to view your tasks
5. Enter `update task` to change a task's status or details
6. Enter `quit` to exit

For a detailed walkthrough, see [HOW_TO_RUN.md](https://github.com/truth05-bizz/task_tracker/blob/main/Task_Trackerv2/HOW_TO_RUN.md)

---

## Project Versions

### Task Tracker v1

#### Description
The first version of the project.

This version was primarily used as a planning and development guide. It contains the initial project structure, ideas, and function breakdowns that helped define the requirements for the application.

Its purpose was to answer questions such as:

* What features should the application have?
* What functions need to be created?
* How should the project be organized?

---

### Task Tracker v2

#### Description
The main implementation of the project.

Version 2 transforms the original plan into a working application and introduces a more modular architecture by separating responsibilities across multiple Python modules.

Current features include:

* **User Authentication** - Sign up and sign in system for user management
* Add tasks
* Update tasks (user-specific)
* Delete tasks (user-specific)
* Generate task IDs
* View task details
* List all tasks (filtered by logged-in user)
* View pending tasks
* View in-progress tasks
* View completed tasks
* Store task data using JSON
* **Multi-user support** - Each user can only see and manage their own tasks

---

## Repository Structure

```text
task_tracker/
│
├── README.md
├── Task_Tracker v1/
│   ├── documentation.txt
│   └── main.py
│
└── Task_Trackerv2/
    ├── main.py                 # Main entry point
    ├── showTask.py            # Display task functionality
    ├── task.py                # Task operations (add, update, delete)
    ├── taskFile.py            # File handling operations
    ├── taskStatus.py          # Task status management
    ├── taskUtilities.py       # Utility functions
    ├── taskLogin.py           # User authentication
    ├── task_history.json      # Task data storage
    ├── user_details.json      # User account data
    ├── user_log.json          # User session log
    ├── documentation.txt      # v2 documentation
    └── HOW_TO_RUN.md         # User guide
```

---

## Technologies Used

* Python
* JSON
* Modular Programming
* File Handling
* Exception Handling
* User Authentication

---

## What I Learned

This project helped me practice and better understand:

* Functions
* Python modules
* JSON file handling
* Exception handling
* Program structure
* Data persistence
* Separation of concerns
* The Read → Modify → Write workflow
* User authentication and session management
* Multi-user data isolation

One of the biggest lessons from this project was learning how applications load data into memory, modify it, and then save the updated version back to storage. Additionally, I learned how to implement multi-user functionality while ensuring data privacy and isolation between users.

---

## Project Features

### Core Functionality
- ✅ Create, read, update, and delete tasks
- ✅ Mark tasks as pending, in-progress, or completed
- ✅ Persistent data storage using JSON
- ✅ Interactive command-line menu
- ✅ Automatic task ID generation
- ✅ User authentication (sign up/sign in)
- ✅ Multi-user support with data isolation

### User Management
- User registration with unique IDs
- Secure login system
- Session management
- User-specific task filtering

### Data Management
- Tasks are stored in `task_history.json`
- User accounts stored in `user_details.json`
- Session logs in `user_log.json`
- All changes are automatically persisted
- Easy-to-read JSON format
- Each user only sees their own tasks

---

## Future Improvements

Planned improvements include:

* Improved input validation
* More robust error handling
* Additional code refactoring
* Enhanced user experience
* Task priority levels
* Due date functionality
* Task categories/tags
* Password encryption
* Data backup functionality

---

## Project Status

**Status:** Active Development

Task Tracker v2 is currently the primary focus of development and serves as a practical learning project for building maintainable Python applications with multi-user support.

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named..."
**Solution:** Make sure you're running the script from the `Task_Trackerv2` directory where all the modules are located.

### Issue: JSON file errors
**Solution:** The `task_history.json`, `user_details.json`, and `user_log.json` files will be created automatically on first run. If they get corrupted, delete them and restart the application.

### Issue: Menu not responding
**Solution:** Make sure to use lowercase text and press Enter. The menu accepts commands like: `show all task`, `add task`, `quit`, etc.

### Issue: Sign in failed
**Solution:** Make sure you're using the correct username and password. Create a new account with `sign up` if you don't have one yet.

### Issue: No tasks appear in task list
**Solution:** This is normal if you just created your account. Create a new task using the `add task` option. Tasks are user-specific and only show for the logged-in user.

---

## Project Demo

For a detailed walkthrough and usage examples, see: [HOW_TO_RUN.md](https://github.com/truth05-bizz/task_tracker/blob/main/Task_Trackerv2/HOW_TO_RUN.md)

---

## Author

Built by Truth as part of a personal journey into software development, computer science, and building real-world applications with Python.
