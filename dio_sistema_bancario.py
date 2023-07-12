'''
Na opção 'saque', só pode ser permitido 3 diários,
com limite de R$5000,00 por saque
'''

USUARIO = 'Jonathan Freitas'
saldo = 0
LIMITE = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3
MENSAGEM_SEM_SALDO = f'''Caro {USUARIO}, 
Seu saldo não é suficiente para realizar esta operação.'''
MENSAGEM_OPERAÇÃO_REALIZADA = 'Operação realizada com sucesso!'

while True:
    opcao = input(f'''Olá {USUARIO}! Tudo bem?
          
          Qual operação deseja realizar?

          [1] Depositar
          [2] Sacar
          [3] Exibir Extrato
          [0] Sair
          ''')
    
    if opcao == '1':
        print('Depósito')
        deposito = float(input('Quanto desja depositar? '))
        if deposito < 0:
            print('Não é possível realizar esta operação')
        else:
            saldo += deposito
            extrato += f'''Depósito - R${deposito:.2f}
Saldo - R${float(saldo):.2f}

'''
            print(MENSAGEM_OPERAÇÃO_REALIZADA)
    
    elif opcao == '2':
        print('Sacar')
        saque = float(input('Quanto deseja sacar? '))
        if numero_saque < LIMITE_SAQUES and saldo >= saque and saque <= LIMITE and saque > 0:
            saldo -= saque
            numero_saque += 1
            extrato += f'''Saque - R${saque:.2f}
Saldo - R${float(saldo):.2f}

'''
            print(MENSAGEM_OPERAÇÃO_REALIZADA)
        elif saque <= 0:
            print('Não é possível realizar a operação')
        elif numero_saque >= LIMITE_SAQUES:
            print('Operação não permitida. Limite diário de saques atingido.')
        elif saque >= LIMITE:
            print('Valor maior que limite permitido.')
        else:
            print(MENSAGEM_SEM_SALDO)

    elif opcao == '3':
        print('Exibir Extrato')
        print('Não foram realizadas movimentações' if not extrato else extrato)


    elif opcao == '0':
        break

    else:
        print('Operação inválida, favor selecionar novamente a operação desejada.')