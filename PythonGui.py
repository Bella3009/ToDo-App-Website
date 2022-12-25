import GUI_Macro as tdm
import PySimpleGUI as psg

psg.theme("DarkBlue4")

clean_list = [clean.strip("\n") for clean in tdm.get_todos()]

label = psg.Text("Type a task to be added:")
input_add = psg.InputText(tooltip="Type a task", key="task_todo")
add_button = psg.Button("Add")
edit_button = psg.Button("Edit")
task_list = psg.Listbox(values=clean_list, key="todo", enable_events=True, size=[100,25])
complete_button = psg.Button("Complete")

window = psg.Window("My To Do App", layout = [[label],[add_button, input_add], [edit_button, complete_button, task_list]], size =[1000,1650])

while True:
    event, value = window.read()
    if event == psg.WIN_CLOSED:
        break
    
    elif event == "Add":
        new_todo = value["task_todo"].title() + "\n"
        
        with open("Tasks.txt", "a") as file:
            file.write(new_todo)
            
        clean_list = [clean.strip("\n") for clean in tdm.get_todos()]
        
        window["todo"].update(values=clean_list)
        window["task_todo"].update(value="")
        
    elif event == "Edit":
        task_edit = value["todo"][0]
        task_edit = task_edit + "\n"
        new_todo = value["task_todo"].title() +"\n"
        
        todo = tdm.get_todos()
        index = todo.index(task_edit)
        todo[index] = new_todo
        todo = tdm.write_todos(todo)
        clean_list = [clean.strip("\n") for clean in tdm.get_todos()]
        
        window["todo"].update(values=clean_list)
    
    elif event == "Complete":
        task_complete = value["todo"][0]
        task_complete = task_complete + "\n"
        
        todo = tdm.get_todos()
        todo.remove(task_complete)
        todo = tdm.write_todos(todo)
        clean_list = [clean.strip("\n") for clean in tdm.get_todos()]
        
        window["todo"].update(values=clean_list)
        window["task_todo"].update(value="")
        
    elif event == "todo":
        task_todo = value["todo"]
        window["task_todo"].update(value=value["todo"][0])
        
window.close()
