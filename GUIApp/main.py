import functions
import FreeSimpleGUI as SG

#creation of the widgets
label = SG.Text("Type in a todo")
input_box = SG.InputText(tooltip="Enter todo",key= "todo") #key is the id of value that is going to be given in the box
add_button = SG.Button("Add")

list_box = SG.Listbox(values=functions.get_todos(),
                      key = "todos",
                      enable_events=True,size= [45,10])
edit_button = SG.Button("edit")
complete_button = SG.Button("complete",key="Complete")

layouts=[[label],
         [input_box,add_button],
         [list_box,edit_button,complete_button]]

#attaching widgets to the window
window = SG.Window("The TO-DO App",
                   layout=layouts,
                   font = ("Helvetica",15))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"]+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values = functions.get_todos())
        case "edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]+"\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values = todos)
            except IndexError:
                SG.popup("Please select an item first",font=("Helvetica",15))
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value = values["todos"][0])
        case "Exit":
            break
        case SG.WIN_CLOSED:
            break

window.close()