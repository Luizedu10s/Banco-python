import PySimpleGUI as sg

sg.theme('Darkblack')

banco = {}

# FUNÇÃO PARA CRIAR CONTA
def CriarConta():
    global banco
    sg.theme('Darkblack')
    tela = [
        [sg.Text("Digite seu nome: ")],
        [sg.Input(key='nome')],
        [sg.Text('Digite o número da conta a ser criada: ')],
        [sg.Input(key='numero_da_conta')],
        [sg.Button('Criar conta')]
    ]
    janela = sg.Window("Cadastro de conta", tela)
    while True:
        events, values = janela.read()
        new_conta_number = int(values['numero_da_conta'])
        if events == 'Criar conta':
            banco += new_conta_number
            banco[new_conta_number] += 0
            janela.close()
# FUNÇÃO PARA FAZER DEPÓSITO
def Deposito():
    sg.theme('Darkblack')
    tela = [
        [sg.Text("Digite o número da conta para deposito: ")],
        [sg.Input(key='numero_conta')],
        [sg.Text("Digite o valor que irá depositar: ")],
        [sg.Input(key='valor_deposito')]
    ]
    janela = sg.Window('Deposito', tela)
    while True:
        events, values = janela.read()
        num_conta = values['numero_conta']
        valor_do_deposito = values['valor_deposito']
        if events == sg.WINDOW_CLOSED:
            break
# FUNÇÃO PARA REALIZAR SAQUE
def FazerSaque():
    sg.theme('Darkblack')
    tela = [
        [sg.Text('Digite o número da conta: ')],
        [sg.Input(key='numero_da_conta')],
        [sg.Text('Digite o valor do saque: ')],
        [sg.Input(key='valor_do_saque')],
        [sg.Button('Sacar', key='saque_realizado')]
    ]
    janela = sg.Window('Tela de saque', janela)
    while True:
        events, values = janela.read()
        number_conta = values['numero_da_conta']
        valor_do_saque = values['valor_do_saque']
        if events == sg.WINDOW_CLOSED:
            break

# TELA PRINCIPAL DO PROGRAMA.
tela = [
    [sg.Button('1 - Criar Nova conta no banco')],
    [sg.Button('2 - Fazer um saque')],
    [sg.Button('3 - Fazer um depósito')],
    [sg.Button('4 - Tirar Extrato')],
    [sg.Button('5 - Sair do banco')],
    [sg.Text('Deseja Sair?')],
    [sg.Button('Sim'), sg.Button('Não')]
]

janela = sg.Window("Banco Python", tela)

while True:
    events, values = janela.read()
    if events == 'Sim':
        break
    if events == '1 - Criar Nova conta no banco':
        CriarConta()
