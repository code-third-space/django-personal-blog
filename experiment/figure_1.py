import json

filename = 'number.json'

try:
    with open(filename) as file:
        number = json.load(file)
        print("I know your favorite number! It's", number)

except FileNotFoundError:
    print("无法找到存储的喜欢的数。")