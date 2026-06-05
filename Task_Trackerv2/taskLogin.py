import taskUtilities
import taskFile
import random

print('Welcome')



def sign_up():

    fname = input('Enter your first name: ')
    lname = input('Enter your last name: ')
    user_name = input('Enter your user name: ')
    gmail = input('Enter your gmail: ')
    password1 = input('Enter your passworg: ')
    password2 = input('Confirm your password: ')


    user_details = {
        'user_fname': fname,
        'user_lname': lname,
        'user_name': user_name,
        'user_gmail': gmail,
        'user_password': password1,
        'unique_id': taskUtilities.generate_id()
    }

    user_data = taskUtilities.read_file(taskFile.json_userDetails())
    user_data.append(user_details)
    
    taskUtilities.write_to_file(user_data, taskFile.json_userDetails())


def sign_in():
    user_data = taskUtilities.read_file(taskFile.json_userDetails())

    user_name = input('Enter your user name: ')
    password = input('Enter password: ')

    if user_name == user_data[0]['user_name'] and password == user_data[0]['user_password']:
        print(f"Welcome Back {user_data[0]['user_name']}")

    else:
        print('Wrong credentials.')




sign_up()