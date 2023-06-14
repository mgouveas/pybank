import textwrap

menu = """
====================PyBank====================

===========Seja Bem-Vindo ao Pybank===========

   Escolha uma das Opções do nosso sistema

   1 - SAQUE
   2 - DEPOSITO
   3 - EXTRATO
   4 - NOVO USUÁRIO
   5 - NOVA CONTA
   6 - LISTAR CONTAS
   0 - SAIR

   Informações Importantes:
    * Você pode realizar até 3 saques/dia
    * Seu limite por saque é de R$500,00

==============================================
""";

msg_saque = """
Saque autorizado!

Aguarde a contagem das notas....

Operação concluída. Retire seus notas da máquina. 
""";

msg_deposito = """
Insira as notas no local indicado.

Aguarde a contagem das notas....

Operação concluída. Depósito realizado com sucesso. 
""";

msg_extrato = """
Registro das últimas operações realizadas nessa conta.

Aguarde a exibição das informações em tela....

Operação concluída. Confira abaixo o seu extrato. 
""";

print(menu);

limite_saque = 500;
numero_saque = 0;
qnt_saque_dia = 3;

saldo = 0;

extrato_saque = []

extrato_deposito = []

clientes = []
contas = []

AGENCIA = "0001"

opcao = int(input("Escolha a operação que deseja realizar: "));


def sacar(limite_saque, numero_saque):
    global saldo
    print('SAQUE.\n');
    saque = int(input('Valor do saque: '));
    if saque <= saldo and saque <= limite_saque:
        numero_saque +=1
        saldo -= saque
        print(msg_saque);
        print(f'\n Saldo da conta: {saldo}');
        extrato_saque.append(f'R${saque},00');
        #print(extrato_saque)
    else:
        print("Operação negada. Você não tem saldo suficiente em sua conta.");

    return saldo, numero_saque

def depositar():
    global saldo
    print('DEPÓSITO \n');
    deposito = int(input("Digite o valor a ser depositado: "));
    if deposito > 0:
        print(msg_deposito);
        saldo += deposito
        extrato_deposito.append(f'R${deposito},00')
        #print(extrato_deposito)
    else:
        print("Valor inválido. O valor mínimo de depósito é de R$1")

    return saldo

def extrato():
    print("EXTRATO \n");
    print(msg_extrato);
    print(f'Saldo atual: R${saldo}.\n\n');
    print(f'Depositos: {extrato_deposito}\n');
    print(f'Saques: {extrato_saque}\n');

def cria_usuario(clientes):
    print("Criação de usuário")
    cpf = input("Digite seu CPF (somente números): ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("Já existe um usuário com esse CPF cadastrado em nosso sistema.")
        return

    nome = input("Digite seu nome completo: ").upper()
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço completo: ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso! Bem Vindo ao PyBank.")

def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Digite seu CPF (somente números): ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    else:
        print("Cliente não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['cliente']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))


while (opcao != 0):

    match opcao:
        case 1:
            if numero_saque < qnt_saque_dia:
                sacar(limite_saque, numero_saque)
            else:
                print("Operação Negada. Limite de saque diário atingido.")

        case 2:
            depositar()

        case 3:
            extrato()

        case 4:
            cria_usuario(clientes)
        
        case 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)
        
        case 6:
            listar_contas(contas)
        
        case _:
            print("Opção inválida. \n\n")
    
    _ = str(input("Obrigado por usar nosso banco. Deseja fazer outra operação: [S] SIM | [N] Não > ")).upper()
    
    if _ == 'S':
        opcao = int(input("\n\n Escolha a operação que deseja realizar: "));
    else:
        opcao = 0;
        print("\n\nSistema sendo encerrado. Volte sempre!\n")
