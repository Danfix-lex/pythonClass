import re

import bcrypt

USER_DETAILS = 'user_details.txt'

def hashed_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(username, hashed_password):
    with open(USER_DETAILS, "a") as file:
        file.write(f'{username},{hashed_password.decode("utf-8")}\n')

def validate_user(username, password):
    with open(USER_DETAILS, 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username:
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
    return False

def register_user():
    while True:
        username = input("Enter your username: ")
        if not username:
            print("Username cannot be empty")
            continue
        break

    while True:
        password = input("Enter your password: ")
        if not password:
            print("Password cannot be empty")
            continue
        break

    save_to_file(username, hashed_password(password))
    main()

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if validate_user(username, password):
        print("Logged in successfully")
    else:
        print("Invalid login credentials")
    main()

def main():
    menu = """
    1. Register user
    2. Login User
    3. Exit
    """

    choice = input(menu)
    match choice:
        case "1":
            register_user()
        case "2":
            login_user()
        case "3":
            print("Thank you for registering")

main()
# while True:
#     password = input("Enter your password: ")
#     if re.fullmatch(r'\w{8,}', password):
#         print("Thank you for registering")
#         break
#     else:
#         print("Invalid password")
help(re.match)
help(re.fullmatch)