import json
import taskUtilities


def all_task():
    task_lst = show_task_title() 

    if not show_task_title():
        print('< No task have been created yet(File is empty!) >')
        print()

    elif show_task_title():
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

    # print(task_data) - for debugging
    # print(type(task_data)) - for debugging
    if not task_data:
        return False

    else:
        for task in task_data:
            print(f"- {task['title']}")
    
    return task_data

# all_task()
# show_task_title()