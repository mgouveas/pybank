import textwrap
from abc import ABC, ABCMeta, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Pessoa_Juridica(Cliente):
    def __init__(self, razao_social, cnpj, endereco):
        super().__init__(endereco)
        self.razao_social = razao_social
        self.cnpj = cnpj

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo

        if valor > saldo:
            print("Operação negada. Você não tem saldo suficiente em sua conta.")
        
        elif valor > 0:
            self._saldo -= valor
            print("""
                Saque autorizado!

                Aguarde a contagem das notas....

                Operação concluída. Retire seus notas da máquina. 
            """);
            return True
        
        else:
            print("Falha na operação. O valor informado é inválido.")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("""
                Insira as notas no local indicado.

                Aguarde a contagem das notas....

                Operação concluída. Depósito realizado com sucesso. 
            """);
        else:
            print("Valor inválido. O valor mínimo de depósito é de R$1!")
            return False
        
        return True

class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, limite, limite_saque):
        super().__init__(numero, cliente)
        self._limite = limite
        limite = 500 
        self._limite_saque = limite_saque
        limite_saque = 3 
        #Numa atualização futura será implementada uma regra para valdiar o tipo de conta para ter o valor limite de saque e o número de saques definidos mais dinamicamente

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes in transacao["tipo"] == Saque.__name__]
        )

        if valor > self._limite:
            print("Operação negada! Valor do saque excede o limite de saque diário.")
        
        elif numero_saques >= self._limite_saque:
            print("Operação negada! Quantidade de saques diárias atingida.")
        
        else:
            return super().sacar(valor)
    
        return False

    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractclassmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
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

    print(menu)

    opcao = int(input("Escolha a operação que deseja realizar: "));

    return opcao

def sacar():
    numero_saque = 0;
    qnt_saque_dia = 3;
    limite_saque = 500
    print('SAQUE.\n');
    saque = int(input('Valor do saque: '));
    if numero_saque < qnt_saque_dia:
        if saque <= saldo and saque <= limite_saque:
            numero_saque +=1
            saldo -= saque
            
            print(f'\n Saldo da conta: {saldo}');
            extrato_saque.append(f'R${saque},00');
            #print(extrato_saque)
           
    else:
        print("Operação Negada. Limite de saque diário atingido.")

    return saldo, numero_saque

def recurperar_conta_cliente(cliente):
    if not cliente.conta:
        print("Falha na operação! Cliente informado não possui nenhuma conta registrada.")
        return
    # FIXME:
    return cliente.conta[0]

def depositar(clientes):
    print('DEPÓSITO \n');

    cpf = input("Digite seu CPF: ")
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print("Cliente não encontrado. Vefique o CPF digitado e tente novamente.")
        return
    
    valor_deposito = int(input("Digite o valor a ser depositado: "))
    transacao = Deposito(valor_deposito)

    conta = recurperar_conta_cliente(cliente):
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def extrato(extrato_saque, extrato_deposito, saldo):
    print("EXTRATO \n");
    print("""
        Registro das últimas operações realizadas nessa conta.

        Aguarde a exibição das informações em tela....

        Operação concluída. Confira abaixo o seu extrato. 
    """);
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

def main():

    extrato_saque = []

    extrato_deposito = []
    clientes = []
    contas = []


    while True:
        opcao = menu();

        match opcao:
            case 1:
                sacar()                

            case 2:
                depositar()

            case 3:
                extrato(extrato_saque, extrato_deposito, saldo)

            case 4:
                cria_usuario(clientes)
            
            case 5:
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, clientes)

                if conta:
                    contas.append(conta)
            
            case 6:
                listar_contas(contas)

            case 0:
                break

        print("Opção inválida. \n\n")


    print("\n\nSistema sendo encerrado. Volte sempre!\n")

main()
