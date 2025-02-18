from diaryApp import Diary

class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        self.diaries.append(Diary(username, password))

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.get_username() == username:
                return diary
        return None

    def delete(self, username, password):
        diary = self.find_by_username(username)
        if diary and diary.get_password() == password:
            self.diaries.remove(diary)
        else:
            raise ValueError("Invalid username or password.")