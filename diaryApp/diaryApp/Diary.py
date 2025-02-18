import Entry

class Diary:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self._locked = True
        self.entries = {}
        self.next_entry_id = 1

    def get_username(self):
        return self.name

    def is_locked(self):
        return self._locked

    def unlock_diary(self, password):
        if password == self.password:
            self._locked = False
        else:
            raise ValueError("Incorrect password")

    def lock_diary(self):
        self._locked = True

    def create_entry(self, title, body):
        if self._locked:
            raise Exception("Diary is locked")
        if not title or not body:
            raise ValueError("Title and body cannot be empty")
        entry = Entry(self.next_entry_id, title, body)
        self.entries[self.next_entry_id] = entry
        self.next_entry_id += 1
        return entry

    def find_entry_by_id(self, entry_id):
        return self.entries.get(entry_id)

    def update_entry(self, entry_id, new_title, new_body):
        if self._locked:
            raise Exception("Diary is locked")
        if entry_id not in self.entries:
            raise ValueError("Entry not found")
        entry = self.entries[entry_id]
        entry.update(new_title, new_body)
        return entry

    def delete_entry(self, entry_id):
        if self._locked:
            raise Exception("Diary is locked")
        if entry_id in self.entries:
            del self.entries[entry_id]