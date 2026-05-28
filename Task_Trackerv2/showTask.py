import json

def all_task():
    task_data = show_task_title()
    
    print()
    print('Enter task for more details.')

    user_prompt = input('>>> ').lower().strip()

    for task in task_data:
        if user_prompt == task['title'].lower():
            print()
            print(task)
            break
    else:
        print('Task not found!')

def show_task_title():
    print('------TASK LIST-------')
    print()
    try:
        with open('task_history.json', 'r') as f:
            task_data = json.load(f)
            for task in task_data:
                print(f"- {task['title']}")
    except (json.JSONDecodeError, FileNotFoundError):
        print('File is not readable or missing.')
        return
    
    return task_data


