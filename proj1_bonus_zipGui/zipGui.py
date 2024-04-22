import PySimpleGUI as sgui
from zip_creator import make_archive

label1 = sgui.Text("Select files to compress: ")
input1 = sgui.Input()
choose_button1 = sgui.FilesBrowse("Choose",key="files")

label2 = sgui.Text("Select destinatian folder: ")
input2 = sgui.Input()
choose_button2 = sgui.FolderBrowse("Choose",key="folder")

compress_button = sgui.Button("Compress")

output_label = sgui.Text(key="output",text_color="blue")

window = sgui.Window("File Compressor", 
                     layout = [[label1, input1, choose_button1],
                              [label2, input2, choose_button2],
                              [compress_button, output_label]])
while True:
    
    event, values = window.read()
    if(event == sgui.WIN_CLOSED ):
        break
    
    filepath = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepath,folder)
    window["output"].update(value="Compression Completed")
    
    


window.close()
