import bcrypt

class User:
    def __init__(self, user_id: int, username: str, password: str, role: str):
        self.user_id = user_id
        self.username = username
        self.password = self._hash_password(password)
        self.role = role

    def _hash_password(self, password: str) -> bytes:
        if isinstance(password, str):
            return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return password

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def __str__(self):
        return f"User(ID: {self.user_id}, Username: {self.username}, Role: {self.role})"
