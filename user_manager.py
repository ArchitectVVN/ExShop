from user import User
from user_exceptions import UserAlreadyExistsError, UserNotFoundError

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User):
        if user.username in self.users:
            raise UserAlreadyExistsError(user.username)
        self.users[user.username] = user

    def remove_user(self, username: str):
        if username not in self.users:
            raise UserNotFoundError(username)
        del self.users[username]

    def find_user(self, username: str) -> User:
        if username not in self.users:
            raise UserNotFoundError(username)
        return self.users[username]
