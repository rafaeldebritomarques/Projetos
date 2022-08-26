from ast import Break
from curses import window
from operator import truediv
import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuário')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]
window = sg.Window('Login',Layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
