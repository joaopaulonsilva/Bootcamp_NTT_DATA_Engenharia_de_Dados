menu = """

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:

        valor = float(input("Por favor informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação não permitida! Por favor informe um valor positivo.")

    if opcao == 2:

        valor = float(input("Por favor informe o valor que deseja sacar: "))
            
        if numero_saques < LIMITE_SAQUES and saldo >= valor and valor <= 500 and valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação não permitida! Seu limite de saques diários foi atingido.")

        elif saldo < valor:
            print(f"Operação não permitida! Seu saldo é insuficiente. Saldo atual R$ {saldo:.2f}\n")

        elif valor > 500:
            print(f"Operação não permitida! Seu limite máximo de saque diário é de R$ 500,00.\n")
        elif valor <=0:
            print("Operação não permitida! Por favor informe um valor positivo.")

    
    if opcao == 3:
        print("\n========Extrato Detalhado==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===================================")
    
    if opcao == 4:
        print(f"Obrigado por utilizar nossos sistemas! É um prazer te-lo como nosso cliente.\n")
        break
else:
    print("Opção inválida, por favor selecione a opção desejada.")