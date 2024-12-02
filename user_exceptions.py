class UserAlreadyExistsError(Exception):
    def __init__(self, username):
        super().__init__(f"Пользователь с именем '{username}' уже существует.")

class UserNotFoundError(Exception):
    def __init__(self, username):
        super().__init__(f"Пользователь с именем '{username}' не найден.")
