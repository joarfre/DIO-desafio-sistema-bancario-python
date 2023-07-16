'''
Neste novo desafio deve-se criar funções para operações exiistentes, como
sacar, depositar e visualizar histórico.Também precisa
criar as funções 'criar usuário'(cliente do banco) e
'criar conta corrente' (vincular com usuário).

A função saque DEVE receber argumentos APENAS por nome
(KEYWORD ONLY). Sugestões de argumentos: saldo, valor, extrato, limite, 
numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

A função depósiyo DEVE receber argumentos APENAS por posição
(POSITIONAL ONLY). Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno: saldo e extrato

A função exrtrato DEVE receber os argumentos por posição e nome
(positional only e keyword only). 
Argumentos posicionais: saldo,
Argumentos nomeados: extrato.

Os usuários deve ser armazenado em lista, um usuário é composto por:
nome, data de nascimento, cpf e endereço. O endereço é uma string com formato:
logradouro, numero - bairro - cidade/sigla estado. 
Deve ser armazenado somente os números do CPF.
Não podemos cadastrar 2 usuários com o mesmo CPF.

As contas devem ser armazenadas em uma lista, uma conta é composta por:
agência, número da conta e usuário.
O número da conta é sequencial, iniciando em 1. 
O número da agência é fixo: '0001'.
O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário

Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o 
número do CPF informado para da usuário da lista
'''


def criar_usuario(usuarios) :
    cpf = input('Informe o CPF (somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário com esse CPF!')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário criado com sucesso!')

def depositar( saldo, deposito, extrato, /):
    if deposito <= 0:
        print('Não é possível realizar esta operação')
    else:
        saldo += deposito
        extrato += f'''Depósito:\tR${deposito:.2f}
    Saldo:\tR${float(saldo):.2f}

    '''
    print(f'''Depósito de R${(deposito):.2f} realizado com sucesso!
          Saldo atual de R${(saldo):.2f}.
          ''')
    return saldo, extrato
 
def sacar(*, saldo, saque, extrato, LIMITE, numero_saque, LIMITE_SAQUES) :
    if numero_saque < LIMITE_SAQUES and saldo >= saque and saque <= LIMITE and saque > 0:
        saldo -= saque
        numero_saque += 1
        extrato += f'''Saque:\tR${saque:.2f}
    Saldo:\tR${float(saldo):.2f}

    '''
        print(f'''Saque de R${(saque):.2f} realizado com sucesso!
              Saldo atual de R${(saldo):.2f}.''')
    elif saque <= 0:
        print('Não é possível realizar a operação')
    elif numero_saque >= LIMITE_SAQUES:
        print('Operação não permitida. Limite diário de saques atingido.')
    elif saque >= LIMITE:
        print('Valor maior que limite permitido.')
    else:
        print('Seu saldo não é suficiente para realizar esta operação.')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato) :
    print('Não foram realizadas movimentações' if not extrato else extrato)

def filtrar_usuario(cpf, usuarios) :
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuário não encontrado. Criação de conta encerrado!')

def operacoes():
    AGENCIA = '0001'
    usuarios = []
    contas = []
    saldo = 0
    LIMITE = 500
    extrato = ''
    numero_saque = 0
    LIMITE_SAQUES = 3
    
    while True:
        opcao = input(f'''Olá! Tudo bem?
            
            Qual operação deseja realizar?

            [1] Depositar
            [2] Sacar
            [3] Exibir Extrato
            [4] Criar Usuário
            [5] Criar Conta
            [0] Sair
            ''')
        
        if opcao == '1':
            deposito = float(input('Quanto desja depositar? '))
            saldo, extrato = depositar(saldo, deposito, extrato)
        
        elif opcao == '2':
            saque = float(input('Quanto deseja sacar? '))
            
            saldo, extrato = sacar(saldo=saldo, saque=saque, extrato=extrato, LIMITE=LIMITE, numero_saque=numero_saque, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5' :
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '0':
            break

        else:
            print('Operação inválida, favor selecionar novamente a operação desejada.')

operacoes()