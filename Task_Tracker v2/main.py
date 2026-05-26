import json
from pathlib import Path
import showTask
import task
import taskFile

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
    print()

    user_prompt = input('>>> ') .lower() .strip()
    if user_prompt == 'show all task':
        x = showTask
        x.all_task()
    elif user_prompt == 'add task':
        y = task
        y.add_task()
    elif user_prompt == 'update task':
        z = task
        z.update_task()
    elif user_prompt == 'see undone task':
        pass
    elif user_prompt == 'see task in progress':
        pass
    elif user_prompt == 'delete task':
        a = task
        a.delete_task()


menu()

