# Only for developer use/access only!

import json
import taskFile

def task_id_settings():
    try:
        with open(taskFile.json_file(), 'r') as f:
            task_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print('No valid task file found; aborting.')
        return
    
    max_task_id = 0
    for task in task_data:
        task_id = task.get('id')
        if isinstance(task_id, int) and task_id > max_task_id:
            max_task_id = task_id

    for task in task_data:
        if task.get('id') is None:
            max_task_id += 1
            task['id'] = max_task_id
            
    with open(taskFile.json_file(), 'w') as f:
        json.dump(task_data, f, indent=4)

    print('Done')
    return max_task_id


