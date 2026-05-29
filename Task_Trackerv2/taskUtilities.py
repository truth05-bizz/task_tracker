# Only for developer use/access only!

import json
import taskFile
from pathlib import Path
import taskFile

def read_file():
    json_task_file = taskFile.file_path()
    if json_task_file.exists():
        try:
            with open(json_task_file, 'r') as f:
                task_data = json.load(f)
                if not isinstance(task_data, list):
                    task_data = []
                    print('No task in task list.')

            
        except (FileNotFoundError, json.JSONDecodeError):
            task_data = []
            file_error = 'No valid task file found; aborting.'
            return file_error
    
    else:
        task_data = []

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

def formatted_task_data(data):
    print()
    print('--------------------------------------')
    print(f"Task name: {data['title']}")
    print(f"Task id: {data['id']}")
    print(f"Task status: {data['status']}")
    print(f"Task info: {data['description']}")
    print(f"Date created: {data['createdAt']}")
    if not data['updated']:
        print(f"Date updated: Not updated.")
    else:
        print(f"Date updated: {data['updated']}")
    print('--------------------------------------')

def empty_json():
    task_data = read_file()

    if not task_data:
        return None
