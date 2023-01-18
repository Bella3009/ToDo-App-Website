import streamlit as st
import GUI_Macro as gm

todos = gm.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    gm.write_todos(todos)
    
st.title("My Todo App")
st.subheader("This is my ToDo List")
st.write("<b>This app is to improve your productivity.</b>",unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    
    if checkbox:
        todos.pop(index)
        gm.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
        # or st.rerun() according to which work 
st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
