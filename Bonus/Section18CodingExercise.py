import PySimpleGUI as sg
from convertor import feet_to_inches


label1 = sg.Text("Enter feet")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches")
input2 = sg.Input(key="inches")

compress_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color='red')

window = sg.Window('Convertor',
                   layout=[[label1, input1],
                           [label2, input2],
                            [compress_button,output_label]])

while True:
    event, values = window.read()
    input1 = float(values["feet"])
    input2 = float(values["inches"])
    result = feet_to_inches(input1, input2)
    window["output"].update(value=f"{result}")

window.close()
