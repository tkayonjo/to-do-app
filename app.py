from tasks import todo_list, task, create_task, delete_task, delete_all_tasks, mark_as_finished
from accounts import accounts, add_account, login

if __name__ == "__main__":

    add_account("name", "password")

    name = input("Enter your name: ")
    password = input("Enter your password: ")

    login(name, password)

    def list_operation():
        print("Choose an Options: ")
        print("1. creating new task")
        print("2. deleting a task")
        print("3. deleting all task")
        print("4. Marking a task finished")

# ..... skipped code
    list_operation()
    selection = input("selection: ")

    if selection is "1":
        create_task(task)

    list_operation()
    selection = input("selection: ")

# Write code that implements the selected option

"""
The above should appear as
    Select Options:
        1. Create Task
        2 ....
        3 ....
        4 ....
    selection:
"""