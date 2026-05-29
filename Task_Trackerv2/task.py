import taskFile
import datetime
import json
import showTask
import taskUtilities
import taskStatus

file_path = taskFile.file_path()
file_name = taskFile.json_file()

def add_task():

    task_name = input('Enter task: ')
    task_id = len(taskUtilities.read_file()) +1
    task_description = input('Description: ')
    task_status = taskStatus.get_status()
    task_createdAT = datetime.datetime.now()
    task_updatedAT = None

    new_task = {
        'title': task_name,
        'id': task_id,
        'description': task_description,
        'status': task_status,
        'createdAt': task_createdAT.strftime('%c'),
        'updated': task_updatedAT,
    }


    task_data = taskUtilities.read_file()

    task_data.append(new_task)

    with open(file_name, 'w') as f:
        json.dump(task_data, f, indent=4)

    print('Task added.')


def update_task():
    lst_task = showTask.show_task_title()
    task_data = taskUtilities.read_file()

    print()
    user_prompt = input('Enter a task to update: ') .lower() .strip()
    print()
    for data in task_data:
        if user_prompt == data['title']:
            data
            # formatted task data for user frienly view
            print(f"Title: {data['title']}")
            print('--------------------------------')
            print(f"id: {data['id']} Not updateable")
            print('--------------------------------')
            print(f"Description: {data['description']}")
            print('--------------------------------')
            print(f"Status: {data['status']}")
            print('--------------------------------')
            print(f"Date/Time created: {data['createdAt']} Not updateable")
            print()
            if not data['updated']:
                print('---No update has been made yet---.')
            else:
                print(f"Date/time updated: {data['updated']}")

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

    taskUtilities.write_to_file(task_data)
        
    print('file updated successfully')

def delete_task():
    task_data = taskUtilities.read_file()
    
    # show task list 
    showTask.show_task_title()

    print()
    user_prompt = input('Enter task to delete: ')
    print(f"Are you sure you want to delete '{user_prompt}'")
    print('y/n...')
    user_input = input('>>> ') .lower() .strip()
    if user_input == 'y':
        for task in task_data:
            if task['title'] == user_prompt:
                task_data.remove(task)

    elif user_input == 'n':
        print('Aborted.')
        return
    
    taskUtilities.task_id_settings(task_data) 
    

    print(f"TASK:[{user_prompt}] deleted successfully")