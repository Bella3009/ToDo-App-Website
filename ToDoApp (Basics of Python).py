import time
import ToDo_Macro
import Error_Handling

now = time.strftime("%d/%b/%Y  %T")
print(f"The date is {now}")
     
while True:
     
     user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ").lower()
     user_action = user_action.strip()
     
     if user_action == "add":
         task = Error_Handling.int_input("How many tasks you want to add: ","You need to enter the number of tasks you want to add ")  
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
         ToDo_Macro.show_todos()
            
     elif user_action == "edit":
         ToDo_Macro.show_todos()
         todo_list = ToDo_Macro.get_todos() 
         task_list = Error_Handling.int_input("Type the number of the task you want to edit: ","You need to enter the number of the task to edit it.")
         
         task_list -= 1 
         old_todo = todo_list[task_list].strip("\n")   
         todo_list[task_list] = input("You want to edit the task to: ") + "\n"
         
         new_todo = todo_list[task_list].strip("\n")
         print(f"The task {old_todo.title()} was edited successfully to {new_todo.title()}")
         
         ToDo_Macro.write_todos(todo_list)
             
     elif user_action == "complete":
         ToDo_Macro.show_todos()
         todo_list = ToDo_Macro.get_todos()
         task_list = Error_Handling.int_input("Type the number of the task you want to mark as complete: ","You need to enter the number of the task to mark it as complete.") 
         
         task_list -= 1
         old_todo = todo_list[task_list].strip("\n")
         todo_list.pop(task_list)
         print(f"Task {old_todo.title()} has been marked as complete successfully.")
           
         ToDo_Macro.write_todos(todo_list)
             
     elif user_action == "exit":
          break
     
     else:
         print("Input not valid. Try again")
         
print("Thank you for using and bye")
