import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"""\
            Titular:\t{self.nome}
        """

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

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
        excedeu_saldo = valor > saldo
    
        if excedeu_saldo:
            print(f"\nOperação não permitida! Seu saldo é insuficiente. Saldo atual R$ {saldo:.2f}\n")

        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso.")
            return True
        
        else:
            print("\nOperação não permitida! Por favor informe um valor positivo.")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDeposito realizado com sucesso.")
        else:
            print("\nOperação não permitida! Por favor informe um valor positivo.")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print("Operação não permitida! Seu limite máximo de saque diário é de R$ 500,00.")

        elif excedeu_saques:
            print("Operação não permitida! Seu limite de saques diários foi atingido.")
        
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C\C:\t\t{self.numero}
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
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
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
    
    def registrar(self, conta):
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
    
    menu = """\n
    =============MENU=============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExibir Extrato
    [4]\tNovo Usuário
    [5]\tNova conta
    [6]\tListar contas
    [7]\tListar usuários
    [8]\tSair
    => """
    return input(textwrap.dedent(menu))

def exibir_extrato(clientes):
    cpf = input("Por favor informe o CPF do cliente:")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("O CPF informado não foi encontrato!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n========Extrato Detalhado==========")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"


    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("\n===================================")

def cadastrar_cliente(clientes):
    cpf = input("Por favor informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Já existe um cliente cadastrado com o CPF informado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome,
    data_nascimento=data_nascimento, cpf=cpf,
    endereco=endereco)

    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("O cliente informado não possui conta!")
        return
    
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def cadastrar_conta(numero_conta, clientes, contas):
    cpf = input("Por favor informe o CPF do cliente:")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Usuário não cadastrado, não foi possível criar a conta!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente,
    numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("\nConta cadastrada com sucesso!")

def depositar(clientes):
    cpf = input("Por favor informe o CPF do cliente:")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("O CPF informado não foi encontrato!")
        return
        
    valor = float(input("Por favor informe o valor que deseja depositar: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Por favor informe o CPF do cliente:")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("O CPF informado não foi encontrato!")
        return
    
    valor = float(input("Por favor informe o valor que deseja sacar: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def listar_clientes(clientes):
    for cliente in clientes:
        print("=" * 100)
        print(textwrap.dedent(str(cliente)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = int(menu())

        while opcao == 1:
            try:
                depositar(clientes)
                break
            except ValueError:
                print("Operação não permitida! Não é permitido inserir letras") 

        while opcao == 2:
            try:
                sacar(clientes)
                break
            except ValueError:
                print("Operação não permitida! Não é permitido inserir letras")

        if opcao == 3:
            exibir_extrato(clientes)

        elif opcao == 4:
            cadastrar_cliente(clientes)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            cadastrar_conta(numero_conta, clientes, contas)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            listar_clientes(clientes)

        elif opcao == 8:
            print("Obrigado por utilizar nossos sistemas! É um prazer te-lo como nosso cliente.")
            break
    else:
        print("Opção inválida, por favor selecione a opção desejada.")

main()