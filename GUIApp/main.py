import functions
import FreeSimpleGUI as SG

#creation of the widgets
label = SG.Text("Type in a todo")
input_box = SG.InputText(tooltip="Enter todo",key= "todo") #key is the id of value that is going to be given in the box
add_button = SG.Button("Add")

#attaching widgets to the window
window = SG.Window("The TO-DO App",
                   layout=[[label],[input_box,add_button]],
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
        case SG.WIN_CLOSED:
            break

window.close()