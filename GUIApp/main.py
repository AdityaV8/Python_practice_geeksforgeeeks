import functions
import FreeSimpleGUI as SG

# individual widget creation
label = SG.Text("Type in a todo")
input_box = SG.InputText(tooltip="Enter todo")
add_button = SG.Button("Add")

#adding the widgets to the window
window = SG.Window("The TO-DO App",layout=[[label,input_box,add_button]]) # the content should be python GUI widget type
window.read()
print("Hello")
window.close()