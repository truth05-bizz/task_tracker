import json
from pathlib import Path
import showTask
import task
import taskFile
import taskStatus

# Requirements :

"""
- Add, Updates, and Delete task
- Mark a task as in progress or done
- List all tasks
- List all tasks that are not done
- List all tasks that are in progres
"""
file_name = taskFile.json_file()
file_path = taskFile.file_path()

def menu():
    # program (task tracker), navigation menu
    print('Welcome to Task Tracker v2')
    print('----------MENU----------')
    print()
    print('- Show all task.')
    print('- Add task. ')
    print('- update task. ')
    print('- delete task. ')
    print('- undone task. ')
    print('- task in progress. ')
    print()

    user_prompt = input('>>> ') .lower() .strip()
    if user_prompt == 'show all task':
        showTask.all_task()       
    elif user_prompt == 'add task':
        task.add_task()
    elif user_prompt == 'update task':
        task.update_task()
    elif user_prompt == 'undone task':
        taskStatus.all_undone_task()
    elif user_prompt == 'task in progress':
        taskStatus.all_task_inprogress()
    elif user_prompt == 'done task':
        taskStatus.done_task()
    elif user_prompt == 'delete task':
        task.delete_task()
    

menu()

