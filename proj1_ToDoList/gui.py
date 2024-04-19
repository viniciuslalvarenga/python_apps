import functions
import PySimpleGUI

#remember useful
#comb = PySimpleGUI.Combo(["valor1","valor2"],default_value="unset",size=10)
#c_box = PySimpleGUI.Checkbox("istrue")

label = PySimpleGUI.Text("Type in a to-do")
#Note: key is the index value of the returned dict with out defined key is numerical
input_box = PySimpleGUI.InputText(tooltip="Enter todo",key="todo")
add_button = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window("My To-Do App", 
    layout=[[label], [input_box, add_button]],
    font=("Helvetica",12))

while True:
    
    event, values = window.read()
    
    match event:
        case "Add":
        
            todos = functions.get_todos()
            new_todos = values["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            
        #This event happen when close button "x" is pressed
        case PySimpleGUI.WIN_CLOSED:
            break
    
    
window.close()


