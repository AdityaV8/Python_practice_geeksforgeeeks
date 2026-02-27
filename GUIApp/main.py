import functions
import FreeSimpleGUI as SG

label = SG.Text("Type in a todo")
input_box = SG.InputText(tooltip="Enter todo")

window = SG.Window("The TO-DO App",layout=[[label,input_box]])
window.read()
window.close()