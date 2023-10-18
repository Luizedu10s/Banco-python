import PySimpleGUI as sg
from time import sleep

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
        [sg.Text(key='sucess', text_color='white')],
        [sg.Button('Criar conta')], [sg.Button('Voltar para tela inicial')]
    ]
    janela = sg.Window("Cadastro de conta", tela)
    while True:
        events, values = janela.read()
        if events == 'Voltar para tela inicial' or events == sg.WIN_CLOSED:
            janela.close()
        if events == 'Criar conta':
            banco[int(values['numero_da_conta'])] = 0
            janela['sucess'].Update('Conta criada com sucesso!')
            sleep(2)
            if events == 'Voltar para tela inicial' or events == sg.WIN_CLOSED:
                break
        if events == sg.WIN_CLOSED:
            break
# FUNÇÃO PARA FAZER DEPÓSITO
def Deposito():
    global banco
    tela = [
        [sg.Text("Digite o número da conta para deposito: ")],
        [sg.Input(key='numero_conta')],
        [sg.Text("Digite o valor que irá depositar: ")],
        [sg.Input(key='valor_deposito')],
        [sg.Text(key='deposito_feito')],
        [[sg.Button('Depositar')], [sg.Button('Voltar ao menu inicial')]]
    ]
    janela = sg.Window('Deposito', tela)
    while True:
        events, values = janela.read()
        if events == 'Depositar':
            banco[int(values['numero_conta'])] += float(values['valor_deposito'])
            janela['deposito_feito'].Update('Depósito feito com sucesso!')
        if events == 'Voltar ao menu inicial':
            janela.close()
        if events == sg.WIN_CLOSED:
            break
# FUNÇÃO PARA REALIZAR SAQUE
def FazerSaque():
    global banco
    tela = [
        [sg.Text('Digite o número da conta: ')],
        [sg.Input(key='numero_da_conta')],
        [sg.Text('Digite o valor do saque: ')],
        [sg.Input(key='valor_do_saque')],
        [sg.Text(key='saque_realizado')],
        [sg.Button('Sacar')], [sg.Button('Sair')]
    ]
    janela = sg.Window('Tela de saque', tela)
    while True:
        events, values = janela.read()
        if events == 'Sacar':
            conta = int(values['numero_da_conta'])
            valor_saque = float(values['valor_do_saque'])
            if conta in banco:
                if banco[conta] > valor_saque:
                    banco[conta] -= valor_saque
                    janela['saque_realizado'].Update('Saque realizado com sucesso!')
                else:
                    janela['saque_realizado'].Update('Saldo Insuficiente.')
                    sleep(2)
            else:
                janela['saque_realizado'].Update('Conta Inexistente no banco!')
        if events == 'Sair':
            janela.close()
        if events == sg.WIN_CLOSED:
            break
# FUNÇÃO PARA RETIRAR EXTRATO
def Extrato():
    global banco
    tela = [
        [sg.Text('Digite o número da conta: ')],
        [sg.Input(key='numero_da_conta')],
        [sg.Text('Saldo: ')],
        [sg.Text(key='saldo_da_conta')],
        [sg.Button('Retirar Extrato')], [sg.Button('Cancelar')],
    ]
    janela = sg.Window('Retirar extrato', tela)
    while True:
        events, values = janela.read()
        if events == 'Retirar Extrato':
            conta = int(values['numero_da_conta'])
            if conta in banco:
                saldo = banco[conta]
                janela['saldo_da_conta'].Update(f'R$ {saldo:.2f}')
            else:
                janela['saldo_da_conta'].Update('Conta inexistente!')
                janela.close()
        if events == 'Cancelar':
            janela.close()
        if events == sg.WIN_CLOSED:
            break
# TELA PRINCIPAL DO PROGRAMA.
tela = [
    [sg.Button('1 - Criar Nova conta no banco')],
    [sg.Button('2 - Tirar Extrato')],
    [sg.Button('3 - Fazer um depósito')],
    [sg.Button('4 - Fazer um saque')],
    [sg.Button('5 - Sair do banco')],
]

janela = sg.Window("Banco Python", tela)

while True:
    events, values = janela.read()
    if events == 'Sim':
        break
    if events == '1 - Criar Nova conta no banco':
        CriarConta()
    if events == '2 - Tirar Extrato':
        Extrato() 
    if events == '3 - Fazer um depósito':
        Deposito()
    if events == '4 - Fazer um saque':
        FazerSaque()
    if events == '5 - Sair do banco':
        janela.close()
    if events == sg.WIN_CLOSED:
        break