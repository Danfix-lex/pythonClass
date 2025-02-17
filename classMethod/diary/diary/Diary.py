from entry import Entry

class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = False
        self.entries = []
        self.next_entry_id = 1

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def is_locked(self):
        return self.is_locked

    def lock_diary(self):
        self.is_locked = True

    def unlock_diary(self, password):
        if self.password == password:
            self.is_locked = False
        else:
            raise ValueError("Incorrect password.")

    def create_entry(self, title, body):
        if self.is_locked:
            raise RuntimeError("Diary is locked.")
        self.entries.append(Entry(self.next_entry_id, title, body))
        self.next_entry_id += 1

    def find_entry_by_id(self, id):
        for entry in self.entries:
            if entry.get_id() == id:
                return entry
        return None

    def update_entry(self, id, new_title, new_body):
        entry = self.find_entry_by_id(id)
        if entry:
            entry.set_title(new_title)
            entry.set_body(new_body)
        else:
            raise ValueError("Entry not found.")

    def delete_entry(self, id):
        entry = self.find_entry_by_id(id)
        if entry:
            self.entries.remove(entry)
        else:
            raise ValueError("Entry not found.")

    def get_entries(self):
        return self.entries
