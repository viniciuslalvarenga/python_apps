import PySimpleGUI as sgui

label1 = sgui.Text("Select files to compress: ")
input1 = sgui.Input()
choose_button1 = sgui.FilesBrowse("Choose")

label2 = sgui.Text("Select destinatian folder: ")
input2 = sgui.Input()
choose_button2 = sgui.FolderBrowse("Choose")

compress_button = sgui.Button("Compress")

window = sgui.Window("File Compressor", 
                     layout = [[label1, input1, choose_button1],
                              [label2, input2, choose_button2],
                              [compress_button]])

window.read()
window.close()
