import json
from pathlib import Path

def get_stored_user_info(path):
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None
    
def get_new_username():
    username = input("What is your name? ")
    return username
    
def greet_user():
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)

    if user_info:
        print(f"Your name is: {user_info['username']}")
        if input("Is this your username? (yes/no): ") == 'yes':
            print("Welcome back!")
            print("Here's your information:")
            print(f"Username: {user_info['username']}")
            print(f"Age: {user_info['age']}")
            print(f"City: {user_info['city']}")
        else:
            username = get_new_username()
            user_info['username'] = username
            print("Username updated.")
            contents = json.dumps(user_info)
            path.write_text(contents)
    else:
        print("User information not found.")
        username = get_new_username()
        age = input("How old are you? ")
        city = input("Which city do you live in? ")

        user_info = {
            'username': username,
            'age': age,
            'city': city,
        }

        contents = json.dumps(user_info)
        path.write_text(contents)

        print("We'll remember the following information about you:")
        print(f"Username: {user_info['username']}")
        print(f"Age: {user_info['age']}")
        print(f"City: {user_info['city']}")

greet_user()