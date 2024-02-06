todo_list = [ ]

while True:
    print("待办事项列表： ")
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task}")

    print("\n选项:")
    print("1.添加待办事项")
    print("2.标记待办事项为已完成")
    print("3.退出")

    choice = input("请选择操作（1/2/3）：")

    if choice == '1':
        task = input('请输入待办事项：')
        todo_list.append(task)
        print("待办事项已添加。")

    elif choice == '2':
        if not todo_list:
            print("没有待办事项。")
        else:
            print("当前待办事项：")
            for index, task in enumerate(todo_list):
                print(f"{index + 1}, {task}")

        task_number = int(input("请选择要标记为已完成的待办事项编号："))
        if 1 <= task_number <= len(todo_list):
            completed_task = todo_list.pop(task_number - 1)
            print(f"'{completed_task}', 已标记为已完成并从列表中删除。")
        else:
            print("无效的待办事项编号。")

    elif choice == '3':
        print("退出应用。")
        break