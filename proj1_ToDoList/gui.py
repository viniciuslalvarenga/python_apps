import functions
import PySimpleGUI

#remember useful
#comb = PySimpleGUI.Combo(["valor1","valor2"],default_value="unset",size=10)
#c_box = PySimpleGUI.Checkbox("istrue")

label = PySimpleGUI.Text("Type in a to-do")
#Note: key is the index value of the returned dict with out defined key is numerical
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=functions.get_todos(),
                                key="todos", enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("Edit")

complete_button = PySimpleGUI.Button("Complete")

exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window("My To-Do App", 
    layout=[[label], [input_box, add_button],
            [list_box, edit_button, complete_button],
            [exit_button]],
    font=("Helvetica",12))

while True:
    
    event, values = window.read()
    print(event)
    print(values)
    print(values["todos"])
    
    match event:
        case "Add":
        
            todos = functions.get_todos()
            new_todos = values["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
            
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todos = values["todo"]
            
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todos + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
            
        case "Complete":
              todo_to_complete = values["todos"][0]
              todos = functions.get_todos()
              todos.remove(todo_to_complete)
              functions.write_todos(todos)
              window["todos"].update(values=todos)
              window["todo"].update(value="")
            
        case "Exit":
            break
        
        #When we select an item in the list box, it generate an event with the
        #list_box key value
        case "todos":
            window["todo"].update(value=values["todos"][0])
            
        #This event happen when close button "x" is pressed
        case PySimpleGUI.WIN_CLOSED:
            break
    
    
window.close()


