import datetime

# Requirements :

"""
- Add, Updates, and Delete task
- Mark a task as in progress or done
- List all tasks
- List all tasks that are not done
- List all tasks that are in progres
"""

# Getting Started

new_task = input('Enter tasks: ')
task_description = input('Enter task description: ')
task_status = input('Input status: ')
task_createdAt = datetime.datetime.now()
task_updatedAt = None


programing = {
    'task_name': 'Programming',
    'id': 1,
    'description': 'learning python',
    'status': 'pending',
    'createdAt': task_createdAt.strftime('%c'),
    'updatedAt': task_updatedAt,
}

reading = {
    'task_name': 'Reading',
    'id': 2,
    'description': 'reading books',
    'status': 'In progress',
    'createdAt': task_createdAt.strftime('%c'),
    'updatedAt': task_updatedAt,
}

to_do_list = [programing, reading]
task_id = len(to_do_list)+1


new_task = {
    'task_name': new_task,
    'id': task_id,
    'description': task_description,
    'status': task_status,
    'createdAt': task_createdAt.strftime('%c'),
    'updatedAt': task_updatedAt,
}


to_do_list.append(new_task)

print(to_do_list)
print()
print(f"Task name: {to_do_list[0]['task_name']}")
print(f"Task id: {to_do_list[0]['id']}")
print(f"Task description: {to_do_list[0]['description']}")
print(f"Task status: {to_do_list[0]['status']}")


