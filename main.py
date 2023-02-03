import pickle


todo_list = []
filename = "todo_list.txt"

try:
    with open(filename, "rb") as f:
        todo_list = pickle.load(f)
except FileNotFoundError:
    todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print("Task added: ", task)
    save_list()

def view_tasks():
    if len(todo_list) == 0:
        print("\033[31m" + "No tasks to show" + "\033[0m")
        return
    for index, task in enumerate(todo_list):
        print(index + 1, task["task"], "\033[1;32m" + "(Completed)" + "\033[0m" if task["completed"] else "")

def mark_task_as_completed(index):
    if index <= len(todo_list):
        todo_list[index - 1]["completed"] = True
        print("Task marked as completed: ", todo_list[index - 1]["task"])
        save_list()
    else:
        print("\033[31m" + "Invalid task index" + "\033[0m")


def delete_task(index):
    if index <= len(todo_list):
        task = todo_list[index - 1]["task"]
        todo_list.pop(index - 1)
        print("Task deleted: ", task)
        save_list()
    else:
        print("\033[31m" + "Invalid task index" + "\033[0m")

def save_list():
    with open(filename, "wb") as f:
        pickle.dump(todo_list, f)


def main_loop():
    while True:
        action = input("What would you like to do? (add/view/mark/del/quit): ")
        if action == "add":
            task = input("Enter task description: ")
            add_task(task)
        elif action == "view":
            view_tasks()
        elif action == "del":
            index = int(input("Enter task index: "))
            delete_task(index)
        elif action == "mark":
            index = int(input("Enter task index: "))
            mark_task_as_completed(index)
        elif action == "quit":
            break
        else:
            print("\033[31m" + "Invalid action" + "\033[0m")

if __name__ == "__main__":
    main_loop()
