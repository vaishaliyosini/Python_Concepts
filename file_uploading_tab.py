#Pip import PySimpleGUI should be made
import PySimpleGUI as sg

#Define the parameters to be displayed  
layout = [[sg.Text('Filename')],      
          [sg.Input(), sg.FileBrowse()],      
          [sg.OK(), sg.Cancel()] ]

#Define window with file name and give the input to read  
event, (number,) = sg.Window('Get filename example').Layout(layout).Read()

#Make pop up  
sg.Popup(event, number)  
