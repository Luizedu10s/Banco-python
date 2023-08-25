from time import sleep 

banco = {}

def novo_cliente():
    nome = input('Digite seu nome: ')
    numero = int(input(f'{nome} Digite o número da conta a ser criada: '))
    banco[numero] = 0
    print(f'Perfeito {nome}, sua conta foi criada com sucesso!')
    print(' ')
    sleep(5)

def deposito():
    conta = int(input('Digite o número da conta: '))
    if conta in banco:
        valor = float(input('Digite o valor do depósito: '))
        banco[conta] += valor
        print('Deposito realizado com sucesso!')
    else:
        print('A conta digitada não existe em nosso banco!')
    print(' ')
    sleep(5)

def sacar():
    valor_de_saque = float(input('Digite o valor do saque: '))
    conta = int(input('Digite o número da sua conta: '))
    if conta in banco:
        if banco[conta] > valor_de_saque:
            banco[conta] -= valor_de_saque
            print(f'Saque de R${valor_de_saque} efetuado com sucesso!')
        else:
            print('Saldo insuficiente!')
    else:
        print('Essa conta não existe em nosso sistema!')
    print(' ')
    sleep(5)


def extrato():
    conta = int(input('Digite o número da conta: '))
    if conta in banco:
        valor_na_conta = banco[conta]
        print(f'Saldo da conta {conta}: R${valor_na_conta}')
    if conta not in banco:
        print('Essa conta não existe em nosso sistema!')   
    print(' ')
    sleep(5)

# Executando a aplicação!

while True:
    print('*' * 50)
    print('MENU'.center(50))
    print('*' * 50)
    print(' ')
    print('1 - Criar nova conta no banco'.center(50))
    print('2 - Fazer um saque'.center(50))
    print('3 - Fazer um depósito'.center(50))
    print('4 - Tirar Extrato'.center(50))
    print('5 - Sair do banco'.center(50))
    print(' ')
    print('*' * 50)
    print(' ')
    opc = int(input('Digite aqui: '))
    if opc == 1:
        novo_cliente()
    if opc == 2:
        sacar()
    if opc == 3:
        deposito()
    if opc == 4:
        extrato()
    if opc == 5:
        break



 
