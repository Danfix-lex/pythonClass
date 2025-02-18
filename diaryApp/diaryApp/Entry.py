from datetime import datetime

class Entry:
    def __init__(self, entry_id, title, body):
        self.id = entry_id
        self.title = title
        self.body = body
        self.time = datetime.now()

    def update(self, new_title, new_body):
        if not new_title or not new_body:
            raise ValueError("Title and body cannot be empty")
        self.title = new_title
        self.body = new_body
        self.time = datetime.now()