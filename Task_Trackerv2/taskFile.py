from pathlib import Path


def file_path():
    task_file_path = Path("task_history.json")
    return task_file_path


def json_file():
    file_name = "task_history.json"
    return file_name


def json_userDetails():
    file_name = "user_details.json"
    return file_name


def json_user_log():
    file_name = Path("user_log.json")
    return file_name
