import taskUtilities
import taskFile


def all_undone_task():
    curr_user_id = taskUtilities.active_user()
    task_status = ['pending', 'in progress']

    task_data = taskUtilities.read_file(taskFile.file_path())
    found = False

    for task in task_data:
        if task['status'] in task_status and task['task_acc_id'] == curr_user_id:
            taskUtilities.formatted_task_data(task)
            found = True

    if not found:
        print()
        print('< No task found. >')
        

def all_task_inprogress():
    curr_user_id = taskUtilities.active_user()
    task_data = taskUtilities.read_file(taskFile.file_path())
    found = False

    for task in task_data:
        if task['status'] == 'in progress' and task['task_acc_id'] == curr_user_id:
            taskUtilities.formatted_task_data(task)
            found = True

    if not found:
        print()
        print('< No task in progress >')

def done_task():
    curr_user_id = taskUtilities.active_user()
    task_data = taskUtilities.read_file(taskFile.file_path())

    found = False
    for task in task_data:
        if task['status'] == 'done' and task['task_acc_id'] == curr_user_id:
            print(task)
            found = True
    
    if not found:
        print()
        print('< No task has been done yet. >')

def get_status():
    allowed_stat = ['pending', 'in progress', 'done']
    while True:
        task_status = input('Task status(Pending, In progress or Done): ')
        if task_status in allowed_stat:
            break

        print()
        print('< Invalid status. Please enter; pending, in progress, or done. >')

    return task_status

