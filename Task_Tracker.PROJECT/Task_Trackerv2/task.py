import taskFile
import datetime
import json
import showTask
import taskUtilities
import taskStatus
import taskLogin

file_path = taskFile.file_path()
file_name = taskFile.json_file()
check_id = showTask.validate_id()

def add_task():

    task_name = input('Enter task: ')
    task_id = len(taskUtilities.read_file(taskFile.file_path())) +1
    task_description = input('Description: ')
    task_status = taskStatus.get_status()
    task_createdAT = datetime.datetime.now()
    task_updatedAT = None
    user_acc = taskUtilities.active_user()

    new_task = {
        'title': task_name,
        'id': task_id,
        'description': task_description,
        'status': task_status,
        'createdAt': task_createdAT.strftime('%c'),
        'updated': task_updatedAT,
        'task_acc_id': user_acc
    }


    task_data = taskUtilities.read_file(taskFile.file_path())

    task_data.append(new_task)

    taskUtilities.write_to_file(task_data, taskFile.json_file())

    print('Task added.')


def update_task():
    showTask.show_task_title()
    task_data = taskUtilities.read_file(taskFile.file_path())

    if check_id:
        print()
        user_prompt = input('Enter a task to update: ') .lower() .strip()
        print()
        for data in task_data:
            if user_prompt == data['title']:

                # formatted task data for user frienly view
                taskUtilities.formatted_task_data(data)

                # default task value
                default_title = data['title']
                default_status = data['status']
                default_description = data['description']

                # user input for new task update
                title_update = input('Enter a new title: ')
                status_update = input('Enter status(pending, in progress, done): ')
                description_update = input('Enter task description: ')
                date_updated = datetime.datetime.now()

                old_task = data # stores old task (might be use if a feature for seeing old update is requested by the user)
                print()
            # updating json file to have new data correction   
                if title_update == '':
                    data['title'] = default_title
                else:
                    data['title'] = title_update
                if status_update == '':
                    data['status'] = default_status
                else:
                    data['status'] = status_update
                if description_update == '':
                    data['description'] = default_description
                else:
                    data['description'] = description_update
                data['updated'] = date_updated.strftime('%c')

    else:
        return

    taskUtilities.write_to_file(task_data, taskFile.json_file())
        
    print('file updated successfully')

def delete_task():
    curr_user_id = taskUtilities.active_user()
    task_data = taskUtilities.read_file(taskFile.file_path())
    
    # show task list 
    # showTask.show_task_title()

    # capture the returned value
    showTask.show_task_title()

    if check_id:
        print()
        user_prompt = input('Enter task to delete: ')
        print(f"Are you sure you want to delete '{user_prompt}'")
        print('y/n...')
        user_input = input('>>> ') .lower() .strip()
        if user_input == 'y':
            for task in task_data:
                if task['title'] == user_prompt and task['task_acc_id'] == curr_user_id:
                    task_data.remove(task)

        elif user_input == 'n':
            print('Aborted.')
            return
        
    else:
        return
    
    taskUtilities.task_id_settings(task_data) 
    

    print(f"TASK:[{user_prompt}] deleted successfully")


    