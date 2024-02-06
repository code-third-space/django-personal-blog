from pathlib import Path

path = Path("guest_book.txt")

while True:
    contents = input(" qing shu ru ")

    if contents == "quit":
        break

    path.write_text(contents + '\n')