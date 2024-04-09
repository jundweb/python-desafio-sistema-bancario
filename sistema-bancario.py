def obter_opcao():
    """Solicita e retorna uma opção válida do menu."""
    while True:
        opcao = input(menu).strip().lower()
        if opcao in ("1", "2", "3", "4"):
            return opcao
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def depositar(saldo, extrato):
    """Realiza a operação de depósito."""
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    """Realiza a operação de saque."""
    valor = float(input("Informe o valor do saque: "))
    if valor > 0:
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES        

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print ("Você sacou R$", valor)
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    """Exibe o extrato e o saldo."""
    print("\n::::::::::::::: EXTRATO BANCO DO RAPOSO :::::::::::::::")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

# Constantes e variáveis globais
menu = """
Menu:
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal
while True:
    opcao = obter_opcao()

    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
    elif opcao == "4":
        break