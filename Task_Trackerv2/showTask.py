import json
import taskUtilities


def all_task():
    task_lst = show_task_title()

    if not isinstance(task_lst, list):
        task_lst = []
        print('No task in task list.')
        return
                
    
    print()
    print('Enter task for more details.')

    user_prompt = input('>>> ').lower().strip()

    for task in task_lst:
        if user_prompt == task['title'].lower():
            taskUtilities.formatted_task_data(task)
            break
            
    else:
        print('Task not found!')
            

def show_task_title():
    print('------TASK LIST-------')
    print()
    task_data = taskUtilities.read_file()
    print(task_data)
    print(type(task_data))
    for task in task_data:
        print(f"- {task['title']}")
    
    return task_data

# all_task()
# show_task_title()