# Only for developer use/access only!

import json
import taskFile
from pathlib import Path
import taskFile
import random
import string

def read_file(file='Default'):
    json_filename = Path(file)
    if json_filename.exists():
        try:
            with open(json_filename, 'r') as f:
                file_data = json.load(f)

                # safely check and correct file type
                if not isinstance(file_data, list):
                    file_data = []
                    # print('No task in task list.') - to spot where issue/error was generated from (for debugging)

            
        except (FileNotFoundError, json.JSONDecodeError):
            file_data = []
    
    
    else:
        file_data = []

    return file_data

def write_to_file(data, file):
    # function for writing to file
    json_file = file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

def task_id_settings(fetch_data):
    task_data = fetch_data

    # safely check function parameter content
    if not task_data:
        # if file is empty, manually read file from the data base
        task_data = read_file(taskFile.file_path())

    # update task id
    for index, task in enumerate(task_data):
        index += 1
        task['id'] = index

    write_to_file(task_data, taskFile.json_file())
    return

def formatted_task_data(data):
    # formatted file data to ease reability and clean output
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
    print()

def generate_id():
    lst_id = [random.randint(0, 9) for _ in range(1, 6)] # in list format
    
    # covert list numbers to integer
    id = int(''.join(map(str, lst_id)))

    # creating a random string
    unique_letters = ''.join(random.sample(string.ascii_letters, k=3))

    # combine both numbers and strings
    unique_id = str(id) + unique_letters
    
    return unique_id


