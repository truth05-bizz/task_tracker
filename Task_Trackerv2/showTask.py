import json
import taskUtilities
import taskFile




def all_task():
    task_lst = show_task_title() 

    if not task_lst:
        print('< No task have been created yet(File is empty!) >')
        print()
        return
    

    else:
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
    curr_user_id = taskUtilities.active_user()
    print('------TASK LIST-------')
    print()

    task_data = taskUtilities.read_file(taskFile.file_path())
    #print(task_data)

    # print(task_data) - for debugging
    # print(type(task_data)) - for debugging
    if not task_data:
        return False

    found = False

    for task in task_data:
        if task['task_acc_id'] == curr_user_id:
            print(f"- {task['title']}")
            found = True

    if not found:
        print('< Task list is empty >')
        
                
            
    
    return task_data


def validate_id():
    curr_user_id = taskUtilities.active_user()
    task_data = taskUtilities.read_file(taskFile.file_path())

    for task in task_data:
        if task['task_acc_id'] == curr_user_id:
            task_id = True
            break

    else:
        task_id = False

    return task_id 



# all_task()
# show_task_title()