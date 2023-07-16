# Sistema Bancário para o Desafio 1 DIO

Neste desafio 1 (arquivo 'dio_sistema-bancario.py'), foi criado um sistema bancário com um único usuário respeitando algumas ***regras***

### Regras do desafio 1
- São permitidos apenas 3 saques diários
- Limite de R$ 500,00 por saque
- Informar quando não há saldo para saque
- Todas as operações devem ser registradas no Extrato
- Se o extrato estiver em branco, apresentar mensagem *Não foram realizadas movimentações*
- Valores exibidos no extrato no formato *R$ xxx.xx*

# Sistema Bancário para o Desafio 2 DIO

Neste desafio 2 (arquivo 'evoluindo_sistema_bancario.py'), deve-se criar funções para operações exiistentes, como
sacar, depositar e visualizar histórico.Também precisa
criar as funções 'criar usuário'(cliente do banco) e
'criar conta corrente' (vincular com usuário).

### Regras do desafio 2
- A função saque DEVE receber argumentos APENAS por nome
(KEYWORD ONLY). Sugestões de argumentos: saldo, valor, extrato, limite, 
numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

- A função depósiyo DEVE receber argumentos APENAS por posição
(POSITIONAL ONLY). Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno: saldo e extrato

- A função exrtrato DEVE receber os argumentos por posição e nome
(positional only e keyword only). 
Argumentos posicionais: saldo,
Argumentos nomeados: extrato.

- Os usuários deve ser armazenado em lista, um usuário é composto por:
nome, data de nascimento, cpf e endereço. O endereço é uma string com formato:
logradouro, numero - bairro - cidade/sigla estado. 
Deve ser armazenado somente os números do CPF.
Não podemos cadastrar 2 usuários com o mesmo CPF.

- As contas devem ser armazenadas em uma lista, uma conta é composta por:
agência, número da conta e usuário.
O número da conta é sequencial, iniciando em 1. 
O número da agência é fixo: '0001'.
O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário

Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o 
número do CPF informado para da usuário da lista