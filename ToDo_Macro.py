def get_todos(filepath="Tasks.txt"):
    """This function is to get the list of To Do tasks to run the program"""
    with open(filepath, "r") as file_local:
        todo_local = file_local.readlines()
    return todo_local

def write_todos(todos_arg, filepath = "Tasks.txt"):
    """This function is to update the tasks of the file Tasks.txt"""
    with open(filepath,"w") as file_local:
        file_local.writelines(todos_arg)
 
def show_todos():
    """This function is only a procedure to print the tasks"""
    todo_local = get_todos()
    
    new_todo = [task.strip("\n") for task in todo_local]
    
    for index, tasks in enumerate(new_todo):
        tasks = tasks.title()
        print(f"{index+1}. {tasks}")       

if __name__ == "__main__":
    print(help(get_todos))
    print(help(write_todos))
    print(help(show_todos))
