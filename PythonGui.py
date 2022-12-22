import ToDo_Macro as tdm
import PySimpleGUI as psg

label = psg.Text("Type a task to be added:")
input_add = psg.InputText(tooltip="Type a task", key="task_todo")
add_button = psg.Button("Add")

window = psg.Window("My To Do App", layout = [[label],[input_add], [add_button]], size =(1000,250))

while True:
    event, value = window.read()
    if event == psg.WIN_CLOSED:
        break
    
    elif event == "Add":
        new_todo = value["task_todo"] + "\n"
        new_todo = new_todo.title()
        
        with open("Tasks.txt", "a") as file:
            file.write(new_todo)

window.close()
