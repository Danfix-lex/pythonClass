import bcrypt

username = input("Enter your username: ")
password = input("Enter your password: ")

def hashed_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())

def validate_user(username, password):
    with open(USER_DETAILS, 'r') as f:

def save_to_file(username, password):
    with open("user_details.txt", "a") as file:
        file.write(f'{username},{hashed_password(password.encode('utf-8'))}\n')

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

        save_to_file(username, password)

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



# my_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#
# print("username:", username)
# print("password:", my_password)