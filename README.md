# Task Tracker

A command-line task management application built with Python.

This repository documents my journey from planning a project to building a modular Python application. The project evolved through two versions, with each version serving a different purpose in the learning process.

---

## Project Versions

### Task Tracker v1

The first version of the project.

This version was primarily used as a planning and development guide. It contains the initial project structure, ideas, and function breakdowns that helped define the requirements for the application.

Its purpose was to answer questions such as:

* What features should the application have?
* What functions need to be created?
* How should the project be organized?

---

### Task Tracker v2

The main implementation of the project.

Version 2 transforms the original plan into a working application and introduces a more modular architecture by separating responsibilities across multiple Python modules.

Current features include:

* Add tasks
* Update tasks
* Delete tasks
* Generate task IDs
* View task details
* List all tasks
* View pending tasks
* View in-progress tasks
* View completed tasks
* Store task data using JSON

---

## Repository Structure

```text
ROADMAP.SH_PROJECTS/
│
├── Task_Tracker v1/
│   ├── documentation.txt
│   └── main.py
│
└── Task_Trackerv2/
    ├── main.py
    ├── showTask.py
    ├── task.py
    ├── taskFile.py
    ├── taskStatus.py
    ├── taskUtilities.py
    ├── task_history.json
    └── documentation.txt
```

---

## Technologies Used

* Python
* JSON
* Modular Programming
* File Handling
* Exception Handling

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

One of the biggest lessons from this project was learning how applications load data into memory, modify it, and then save the updated version back to storage.

---

## Future Improvements

Planned improvements include:

* Improved input validation
* More robust error handling
* Additional code refactoring
* Enhanced user experience

---

## Project Status

Active Development

Task Tracker v2 is currently the primary focus of development and serves as a practical learning project for building maintainable Python applications.

---

## Project Demo

Demo / Walkthrough:

[(https://github.com/truth05-bizz/task_tracker/blob/main/Task_Trackerv2/HOW_TO_RUN.md)]

Repository:

[(https://github.com/truth05-bizz/task_tracker)]

---

## Author

Built by Truth as part of a personal journey into software development, computer science, and building real-world applications with Python.
