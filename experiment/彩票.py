import random

""" lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

selected_numbers = random.sample(lottery_numbers, 4)
print(f"中奖号码是: {selected_numbers}")

if set(selected_numbers) == {'A', 'B', 'C', 'D', 'E'}:
    print("恭喜！中大奖了！")
else:
    print("很遗憾，未中奖。") """

""" my_ticket = ['A', 7, 'B', 3]
count = 0

while True:
    selected_numbers = random.sample(list(range(1, 11)) + ['A', 'B', 'C', 'D', 'E'], 4)
    count += 1

    if selected_numbers == my_ticket:
        break

print(f"恭喜！中大奖了！中奖号码是：{selected_numbers}")
print(f"执行了 {count} 次循环才中了大奖。") """