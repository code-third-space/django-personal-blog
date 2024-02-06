from pathlib import Path

path = Path("guest_book.txt")

while True:
    first_number = input("\nfirst_number:")
    if first_number == "q":
        break

    second_number = input("\nsecond_number:")
    if second_number == 'q':
        break

    try:
        anwer = int(first_number) + int(second_number)
    except ValueError:
        print("chongxin:")

    else:
        print(anwer)

    path.write_text(anwer)