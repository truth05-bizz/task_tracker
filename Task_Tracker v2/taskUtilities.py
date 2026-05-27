# Only for developer use/access only!

import json
import taskFile

def read_file():
    try:
        with open(taskFile.json_file(), 'r') as f:
            task_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print('No valid task file found; aborting.')
        return
    
    return task_data

def write_to_file(data):
    with open(taskFile.json_file(), 'w') as f:
        json.dump(data, f, indent=4)

def task_id_settings(fetch_data):
    task_data = fetch_data

    if not task_data:
        task_data = read_file()
        print(task_data)

    max_task_id = 0
    for task in task_data:
        task_id = task.get('id')
        if isinstance(task_id, int) and task_id > max_task_id:
            max_task_id = task_id

    for task in task_data:
        if task.get('id') is None:
            max_task_id += 1
            task['id'] = max_task_id

    write_to_file(task_data)
    return


