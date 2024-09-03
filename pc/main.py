tasks = []

def display_tasks():
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")
    print()

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task removed: {removed_task}")
    else:
        print("Invalid task number")

def main():
    while True:
        display_tasks()
        print("Options: 1. Add Task 2. Remove Task 3. Exit")
        option = input("Choose an option: ")

        if option == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif option == '2':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif option == '3':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
