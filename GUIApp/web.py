import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos)
    print(todo)


st.title("My TODO App")
st.subheader("Add new task")
st.write("This app will improve your productivity ")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add TODO ",placeholder="add new todo",
              on_change=add_todo,key="new_todo")

st.session_state
