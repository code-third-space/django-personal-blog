from pathlib import Path

filename = "learning_python.txt"
path = Path(filename)

with path.open() as file:
    contents = file.read()
    print(contents)

with path.open() as file:
    lines = file.readlines()
    for line in lines:
        print(line.rstrip())

filename  = "learning_python.txt"

with open(filename) as file:
    lines = file.readlines()
    for line in lines: #把原先的列表也打印出来。
        print(line.rstrip())

lines = [line.replace("Python", "C") for line in lines]

for line in lines:
    print(line.rstrip())

filename = "learning_python.txt"

with open(filename) as file:
    for line in file.read().splitlines():
        print(line.replace("Python", "C"))

