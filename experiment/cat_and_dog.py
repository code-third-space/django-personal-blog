from pathlib import Path

try:
    cats_file = Path("cats.txt")
    dogs_file = Path("dogs.txt")

    with cats_file.open() as file:
        cats_contents = file.read()
        print("Cats:")
        print(cats_contents)

    with dogs_file.open() as file:
        dogs_contents = file.read()
        print("Dogs:")
        print(dogs_contents)

except FileNotFoundError:
    pass