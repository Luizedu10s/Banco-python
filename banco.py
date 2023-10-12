import PySimpleGUI as sg

sg.theme('Darkblack')

banco = {}

# FUNÇÃO PARA CRIAR CONTA
def CriarConta():
    global banco
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
        conta_number = janela['numero_da_conta']
        new_conta = int(conta_number)
        if events == 'Criar conta':
            banco = new_conta
            janela.close()
# FUNÇÃO PARA FAZER DEPÓSITO
def Deposito():
    global banco
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
    global banco
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
# FUNÇÃO PARA RETIRAR EXTRATO
def Extrato():
    global banco
    tela = [
        [sg.Text('Digite o número da conta: ')],
        [sg.Input(key='numero_da_conta')],
        [sg.Text('Saldo: ')],
        [sg.Input(key='saldo_da_conta')]
        [sg.Button('Retirar Extrato')], [sg.Buton('Cancelar')],
    ]
    janela = sg.Window('Retirar extrato', tela)
    while True:
        events, values = janela.read()
        conta = values['numero_da_conta']
        if events == 'Retirar Extrato':
            if conta in banco:
                saldo = banco[conta]
                janela['saldo_da-conta'].Update(saldo)
            else:
                janela['saldo_da_conta'].Update('Conta inexistente!')
                janela.close()
        if events == 'Cancelar':
            janela.close()

# TELA PRINCIPAL DO PROGRAMA.
tela = [
    [sg.Button('1 - Criar Nova conta no banco')],
    [sg.Button('2 - Fazer um saque')],
    [sg.Button('3 - Fazer um depósito')],
    [sg.Button('4 - Tirar Extrato')],
    [sg.Button('5 - Sair do banco')],
]

janela = sg.Window("Banco Python", tela)

while True:
    events, values = janela.read()
    if events == 'Sim':
        break
    if events == '1 - Criar Nova conta no banco':
        CriarConta()
    if events == '2 - Fazer um saque':
        FazerSaque()
    if events == '3 - Fazer um depósito':
        Deposito()
    if events == '4 - Tirar Extrato':
        Extrato()
    if events == '5 - Sair do banco':
        janela.close()