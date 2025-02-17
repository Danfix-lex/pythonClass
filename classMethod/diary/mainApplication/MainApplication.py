from datetime import datetime

class Entry:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.date_created = datetime.now()

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body

    def get_date_created(self):
        return self.date_created

from diary import Diary
from diaries import Diaries

def main():
    diaries = Diaries
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

def create_entry(diaries):
    username = input("Enter the username of your diary: ")
    diary = diaries.find_by_username(username)
    if diary:
        if diary.is_locked:
            print("Your Diary is locked. Unlock it first.")
            return
        title = input("Enter your entry title: ")
        body = input("Enter your entry body: ")
        diary.create_entry(title, body)
        print("Your Entry has been created successfully!")
    else:
        print("Diary not found.")

def view_entries(diaries):
    username = input("Enter the username of your diary: ")
    diary = diaries.find_by_username(username)
    if diary:
        for entry in diary.get_entries():
            print(f"ID: {entry.get_id()}, Title: {entry.get_title()}, Body: {entry.get_body()}, Date: {entry.get_date_created()}")
    else:
        print("Diary not found.")

def update_entry(diaries):
    username = input("Enter the username of your diary: ")
    diary = diaries.find_by_username(username)
    if diary:
        if diary.is_locked:
            print("Your Diary is locked. Unlock it first.")
            return
        entry_id = int(input("Enter your entry ID: "))
        new_title = input("Enter your new title: ")
        new_body = input("Enter your new body: ")
        try:
            diary.update_entry(entry_id, new_title, new_body)
            print("Entry updated successfully!")
        except ValueError as e:
            print(e)
    else:
        print("Diary not found.")

def delete_entry(diaries):
    username = input("Enter the username of your diary: ")
    diary = diaries.find_by_username(username)
    if diary:
        if diary.is_locked:
            print("Your Diary is locked. Unlock it first.")
            return
        entry_id = int(input("Enter your entry ID: "))
        try:
            diary.delete_entry(entry_id)
            print("Your Entry deleted successfully!")
        except ValueError as e:
            print(e)
    else:
        print("Diary not found.")

def delete_diary(diaries):
    username = input("Enter the username of your diary: ")
    password = input("Enter your password: ")
    try:
        diaries.delete(username, password)
        print("Your Diary has been deleted successfully!")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
