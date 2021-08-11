from data_manager import DataManager


def register_new_user():
    print('Welcome to Flight Club')
    print('We find the best flight deals and email you')
    first_name = input('What is your first name?: ')
    last_name = input('What is your last name?: ')
    email_1 = input('What is your email?: ')
    email_2 = input('Type your email again: ')
    if email_1 == email_2:
        print('You\'re in the club!')
        data_manager.register_new_user(first_name, last_name, email_1)


if __name__ == '__main__':
    data_manager = DataManager()
    register_new_user()
