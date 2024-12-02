from user import User
from user_manager import UserManager
from user_exceptions import UserAlreadyExistsError, UserNotFoundError

def main():
    manager = UserManager()

    # Пробуем добавить пользователей
    try:
        user1 = User(username="Alice", email="alice@example.com", age=25)
        user2 = User(username="Bob", email="bob@example.com", age=30)
        user3 = User(username="Alice", email="alice2@example.com", age=28)  # Дубликат

        manager.add_user(user1)
        manager.add_user(user2)
        print("Пользователи добавлены.")
        
        # Попробуем добавить пользователя с существующим именем
        manager.add_user(user3)
    except UserAlreadyExistsError as e:
        print(e)

    # Пробуем удалить пользователей
    try:
        manager.remove_user("Charlie")  # Пользователя не существует
    except UserNotFoundError as e:
        print(e)

    # Пробуем найти пользователей
    try:
        user = manager.find_user("Alice")
        print(f"Найден пользователь: {user}")
        user = manager.find_user("Charlie")  # Пользователя не существует
    except UserNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
