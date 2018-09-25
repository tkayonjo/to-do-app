todo_list = []
finished = '[Finished]'
task = ""


def create_task(task):
    """Adds a new task to the todo_list"""

    task = input("Add task to list: ")

    todo_list.append(task)
    print("task has been added")

    return todo_list


def delete_task(task):
    """
    Removes the specified task from the todo_list
    """
    todo_list.remove(task)

    return todo_list


def mark_as_finished(task):
    """ Appends [Finished] to a finished task"""
    task_index = todo_list.index(task)
    todo_list[task_index] = task + finished
    return todo_list


def delete_all_tasks():
    """
    Empties the the todo_lsit
    """
    todo_list.clear()

    return todo_list