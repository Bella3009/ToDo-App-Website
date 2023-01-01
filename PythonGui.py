import GUI_Macro as tdm
import PySimpleGUI as psg

psg.theme("DarkBlue4")

clean_list = [clean.strip("\n") for clean in tdm.get_todos()]

label = psg.Text("Type a task to be added:", (50,1))
empty = psg.Text("")
input_add = psg.InputText(tooltip="Type a task", key="task_todo", size=(25,1))
add_button = psg.Button("Add")
edit_button = psg.Button("Edit")
task_list = psg.Listbox(values=clean_list, key="todo", enable_events=True, size=[50,20])
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")

col1 = [[task_list]]
col2 = [[empty], [edit_button],[complete_button]]
 
window = psg.Window("My To Do App", layout = [[label], [input_add, add_button], [psg.Column(col1, size=(700,1350)), psg.Column(col2, element_justification="c")], [exit_button]], size =[1000,1650], element_justification="c")

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
        try:
            task_edit = value["todo"][0]
            task_edit = task_edit + "\n"
            new_todo = value["task_todo"].title() +"\n"
            
            todo = tdm.get_todos()
            index = todo.index(task_edit)
            todo[index] = new_todo
            todo = tdm.write_todos(todo)
            clean_list = [clean.strip("\n") for clean in tdm.get_todos()]
            
            window["todo"].update(values=clean_list)
            
        except IndexError:
            psg.popup("First select an item from the list, type the new task in the text box and then press the 'Edit' button", title="Invalid selection")
    
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
        
    elif event == "Exit":
        break
        
window.close()
