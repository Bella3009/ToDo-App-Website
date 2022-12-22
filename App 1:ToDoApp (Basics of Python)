def get_todos(filepath="Tasks.txt"):
    with open(filepath, "r") as file_local:
        todo_local = file_local.readlines()
    return todo_local

def write_todos(todos_arg, filepath = "Tasks.txt"):
    with open(filepath,"w") as file_local:
        file_local.writelines(todos_arg)

def int_input(question,error_message):
    while True:
        user_test = input(question)
        if (user_test.isdigit()):
            ans = int(user_test)
            return ans
        else:
            print(f"Invalid input. {error_message}")
    

while True:
     user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ").lower()
     user_action = user_action.strip()
     
     if user_action == "add":
         
         task = int_input("How many tasks you want to add: ","You need to enter the number of tasks you want to add ")
             
         print("Write what to add in your 'To Do List':")
         
         for n in range(task):
           input_task= input() + '\n'
           
         with open("Tasks.txt", "a") as file:
               file.write(input_task)
         
         if task == 1:
             print("Item added succesfully")
         else:
             print("Items added succesfully")
        
     elif user_action == "show":
         
         todo_list = get_todos()
          
         new_todo = [task.strip("\n") for task in todo_list]
         
         for index, tasks in enumerate(new_todo):
             tasks = tasks.title()
             print(f"{index+1}. {tasks}")
            
     elif user_action == "edit":
         
         todo_list = get_todos()
         
         task_list = int_input("Type the number of the task you want to edit: ","You need to enter the number of the task to edit it.")
         
         task_list -= 1
             
         old_todo = todo_list[task_list].strip("\n")
             
         todo_list[task_list] = input("You want to edit the task to: ") + "\n"
             
         print(f"The task {old_todo.title()} was edited successfully to {todo_list[task_list].title()}")
             
         write_todos(todo_list)
             
     elif user_action == "complete":
         
         todo_list = get_todos()
         
         task_list = int_input("Type the number of the task you want to mark as complete: ","You need to enter the number of the task to mark it as complete.")
             
         task_list -= 1
         
         old_todo = todo_list[task_list].strip("\n")
             
         todo_list.pop(task_list)
         
         print(f"Task {old_todo.title()} has been as complete successfully.")
             
         write_todos(todo_list)
             
     elif user_action == "exit":
          break
     
     else:
         print("Input not valid. Try again")
         
print("Thank you for using and bye")
