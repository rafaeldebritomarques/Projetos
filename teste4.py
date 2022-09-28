import PySimpleGUI as sg


layout=[
    [sg.Text('Tenho um número guardado em minha memória:')],
    [sg.Text('Tente advinhar digitando um número logo abaixo:')],
    [sg.Input(key='numero')],
    [sg.Button('Advinhar')],
    [sg.Text('',key ='mensagem')],
]

window = sg.Window('Teste de Advinhação', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Advinhar':
        numero_correto = '50'
       # numero = int(numero_texto)
        chute = values['numero']
    if chute == numero_correto:
            window['mensagem'].update('Show de bola, você acertou o número secreto')
    elif (chute > numero_correto):
            window['mensagem'].update('Poxa vida, o seu chute foi maior que o número gravado em minha memória')
    elif (chute < numero_correto):
            window['mensagem'].update('Poxa vida, o seu chute foi menor que o número gravado em minha memória')
            #window['mensagem'].update('Obrigado por participar!! Tchau!!')
      