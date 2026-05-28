# Only for developer use/access only!

import json
import taskFile

def read_file(json_file=taskFile.json_file()):
    json_task_file = json_file
    try:
        with open(json_task_file, 'r') as f:
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

    for index, task in enumerate(task_data):
        index += 1
        task['id'] = index

    write_to_file(task_data)
    return
