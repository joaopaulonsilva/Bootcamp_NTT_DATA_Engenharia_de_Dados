import textwrap

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

def sacar(*, saldo, valor, extrato, LIMITE, numero_saques, LIMITE_SAQUES):
    
    if numero_saques < LIMITE_SAQUES and saldo >= valor and valor <= LIMITE and valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso.")

    elif numero_saques >= LIMITE_SAQUES:
        print("Operação não permitida! Seu limite de saques diários foi atingido.")

    elif saldo < valor:
        print(f"Operação não permitida! Seu saldo é insuficiente. Saldo atual R$ {saldo:.2f}\n")

    elif valor > 500:
        print("Operação não permitida! Seu limite máximo de saque diário é de R$ 500,00.")
    elif valor <=0:
        print("Operação não permitida! Por favor informe um valor positivo.")
    
    return saldo, extrato

def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso.")
    else:
        print("Operação não permitida! Por favor informe um valor positivo.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n========Extrato Detalhado==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n===================================")
    return saldo, extrato

def cadastrar_usuario(usuarios):
    cpf = input("Por favor informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF de usuário já cadastrado!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta cadastrada com sucesso!")
        print(type(usuario))
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não cadastrado, não foi possível criar a conta!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario'][0]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f"""\
            Usuario:\t{usuario['nome']['cpf']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    LIMITE = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:

        opcao = int(menu())

        while opcao == 1: 
            try:
                valor = float(input("Por favor informe o valor que deseja depositar: "))
                saldo, extrato = depositar(saldo, valor, extrato)
                break
            except ValueError:
                print("Operação não permitida! Não é permitido inserir letras") 

        while opcao == 2:
            try:
                valor = float(input("Por favor informe o valor que deseja sacar: "))
                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, LIMITE=LIMITE, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
                break
            except ValueError:
                print("Operação não permitida! Não é permitido inserir letras")
        
        if opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            cadastrar_usuario(usuarios)

        elif opcao == 5:
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta =+ 1

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            listar_usuarios(usuarios)

        elif opcao == 8:
            print("Obrigado por utilizar nossos sistemas! É um prazer te-lo como nosso cliente.")
            break
    else:
        print("Opção inválida, por favor selecione a opção desejada.")

main()