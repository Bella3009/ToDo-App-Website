import ToDo_Macro
import PySimpleGUI as psg

label = psg.Text("Type a Task to be added:")
input_add = psg.InputText(tooltip="Type a task")
add_button = psg.Button("Add")
window = psg.Window("My To Do App", layout = [[label],[input_add], [add_button]], size =(1000,250))

window.read()
window.close()
