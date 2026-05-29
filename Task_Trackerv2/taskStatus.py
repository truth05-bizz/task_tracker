import taskUtilities


def all_undone_task():
    task_status = ['pending', 'in progress']

    task_data = taskUtilities.read_file()
    for task in task_data:
        if task['status'] in task_status:
            taskUtilities.formatted_task_data(task)

        else:
            print('No task found.')
        

def all_task_inprogress():
    task_data = taskUtilities.read_file()
    for task in task_data:
        if task['status'] == 'in progress':
            taskUtilities.formatted_task_data(task)
        else:
            print('No task in progress')

def done_task():
    task_data = taskUtilities.read_file()
    for task in task_data:
        if task['status'] == 'done':
            print(task)
    
        else:
            print('No task has been done yet.')

def get_status():
    allowed_stat = ['pending', 'in progress', 'done']
    while True:
        task_status = input('Task status(Pending, In progress or Done): ')
        if task_status in allowed_stat:
            break
        print('Invalid status. Please enter; pending, in progress, or done.')

    return task_status