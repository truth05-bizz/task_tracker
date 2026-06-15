import taskUtilities
import taskLogin


def Main():
    print()
    print('-------------------------')
    print()
    print('WELCOME TO TASK TRACKER v2')
    print()
    print('-------------------------')
    print()
    print('< Get Started >')
    print('-----SIGN UP/SIGN IN-----')
    user_prompt = input('>>> ') .lower()  .strip()


    if user_prompt == 'sign up':
        print()
        print('---CREATE AND ACCOUNT---')
        print()
        taskLogin.sign_up()

    elif user_prompt == 'sign in':
        print()
        print('---LOGIN TO ACCOUNT---')
        print()
        taskLogin.sign_in()

Main()
