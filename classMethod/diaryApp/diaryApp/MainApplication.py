def main():
    diaries = Diaries()
    while True:
        option_str = input(
            """Welcome to the Danfix's Diary Application
            1. Create Diary
            2. Lock Diary
            3. Unlock Diary
            4. Create Entry
            5. View Entries
            6. Update Entry
            7. Delete Entry
            8. Delete Diary
            9. Exit
            Enter your choice: """
        )
        try:
            option = int(option_str)
            process_option(option, diaries)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def process_option(option, diaries):
    if option == 1:
        create_diary(diaries)
    elif option == 2:
        lock_diary(diaries)
    elif option == 3:
        unlock_diary(diaries)
    elif option == 4:
        create_entry(diaries)
    elif option == 5:
        view_entries(diaries)
    elif option == 6:
        update_entry(diaries)
    elif option == 7:
        delete_entry(diaries)
    elif option == 8:
        delete_diary(diaries)
    elif option == 9:
        print("Thank you for using Danfix's Diary Application!")
        exit()
    else:
        print("Invalid option. Please try again.")

def create_diary(diaries):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    diaries.add(username, password)
    print("Your Diary has been created successfully!")

def lock_diary(diaries):
    username = input("Enter the username of your diary to lock: ")
    diary = diaries.find_by_username(username)
    if diary:
        diary.lock_diary()
        print("Your Diary has been locked successfully!")
    else:
        print("Diary not found.")

def unlock_diary(diaries):
    username = input("Enter the username of your diary to unlock: ")
    diary = diaries.find_by_username(username)
    if diary:
        password = input("Enter your password: ")
        try:
            diary.unlock_diary(password)
            print("Your Diary has been unlocked successfully!")
        except ValueError as e:
            print(e)
    else:
        print("Diary not found.")

if __name__ == "__main__":
    main()