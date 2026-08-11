import taskUtilities
import taskFile
import random
import menu


def sign_up():

    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    user_name = input("Enter your user name: ")
    gmail = input("Enter your gmail: ")
    password1 = input("Enter your passworg: ")
    password2 = input("Confirm your password: ")

    user_details = {
        "user_fname": fname,
        "user_lname": lname,
        "user_name": user_name,
        "user_gmail": gmail,
        "user_password": password1,
        "unique_id": taskUtilities.generate_id(),
    }

    user_data = taskUtilities.read_file(taskFile.json_userDetails())
    user_data.append(user_details)

    taskUtilities.write_to_file(user_data, taskFile.json_userDetails())

    print("Account Created.")
    sign_in()


def sign_in():
    user_data = taskUtilities.read_file(taskFile.json_userDetails())

    user_name = input("Enter your user name: ")
    password = input("Enter password: ")

    for user in user_data:
        if user_name == user["user_name"] and password == user["user_password"]:
            print(f"Welcome Back {user['user_name']}")

            # get current/login user id
            user_id = user["unique_id"]
            # create and read id file list(stores login id(history and current))
            active_id = taskUtilities.read_file(taskFile.json_user_log())
            # add recently login id to list file
            active_id.append(user_id)
            # write to file
            taskUtilities.write_to_file(active_id, taskFile.json_user_log())
            menu.main()
            break

    else:
        print("Wrong credentials.")


def sign_out():
    user_log = taskUtilities.read_file(taskFile.json_user_log())
    user_id = None
    user_log.append(user_id)

    taskUtilities.write_to_file(user_log, taskFile.json_user_log())
