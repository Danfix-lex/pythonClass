class Diaries:
    def __init__(self):
        self.diary_collection = {}

    def add_diary(self, diary):
        if diary.name in self.diary_collection:
            raise ValueError(f"A diary with the username '{diary.name}' already exists.")
        self.diary_collection[diary.name] = diary

    def find_diary_by_username(self, username):
        return self.diary_collection.get(username)

    def delete_diary(self, username):
        if username in self.diary_collection:
            del self.diary_collection[username]