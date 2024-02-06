import json
number = input("qing shu ru ")
filename = 'number.json'

with open(filename, 'w') as file:
    json.dump(number, file)