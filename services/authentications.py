from models.user import User

def is_user(users: list[User], username: str) -> bool:
    for user in users:
        if user.username == username:
            return True
    
    return False

def check_password(password: str) -> bool:
    p1, p2, p3, p4 = False, False, False, False

    for char in password:
        if char.isupper():
            p1 = True
        elif char.islower():
            p2 = True
        elif char.isdigit():
            p3 = True
        elif char in "!@#$%^&*()":
            p4 = True

    return all([p1, p2, p3, p4])


def register(users: list[User]) -> User:
    name = input("Name: ")
    while not name.isalpha():
        print("Name not found")
        name = input("Name: ")

    age = input("Age: ")
    while not age.isdigit() or int(age) < 18:
        print("Age not found")
        age = input("age: ")

    username = input("Username: ")
    while is_user(users, username):
        print("Username not found")
        username = input("username: ")

    password = input("Password: ")
    while not check_password(password):
        print("Password not found")
        password = input("Password: ")

    return User(name, age, username, password)

def login(users: list[User]) -> User | None:
    username = input("Username: ")
    password = input("Password: ")

    if is_user(users, username) and check_password(password):
        for user in users:
            if user.username == username and user.password == password:
                return user
        
    return None

def logout(user: User, session: list[User]) -> list[User] | None:
    session.remove(user)
    return session
    