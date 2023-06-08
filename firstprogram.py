tasks = []
while True:
    print("1. add a task")
    print("2. remove a task")
    print("3. mark as completed")
    print("4. exit ")

    choice = int(input("enter your choice"))
    if choice == 1:
        task = input("enter a task:")
        tasks.append(task)
        print("tasks added successfully")
    elif choice == 2:
        print("enter the task or index of the task:")
        if task.isdigit():
            index = int(task)
            if 0 <= index < len(tasks):
                tasks.pop(index)
                print("removed the task")
        else:
            if task in tasks:
                tasks.remove(task)
                print("Task removed successfully")
            else :
                print("invalid task")
    elif choice == 3:
        print("enter the task or index of task that should be marked as completed")
        if task.isdigit():
            index = int(task)
            if 0<=index<len(task):
                task[index] += "(completed)"
                print("task marked as completed")
            else:
                if task in tasks :
                    tasks[tasks.index[task]] += "(completed)"
                    print("task marked")
                else:
                    print("Task not found")
    elif choice == 4:
        print("exiting the porgram...")
        break
    else:
        print("invalid choice,please enter correct choice")
    print("current tasks")
    for index,task in enumerate(tasks):
        print(f"{index}. {task}")

    print()
