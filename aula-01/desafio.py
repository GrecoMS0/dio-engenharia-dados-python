menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"║ Operação: DEPÓSITO ║ Valor: R${valor:8.2f} ║\n"
            print("""
                      Depósito realizado com sucesso!
            """)
        else:
            print("""
                      Falha na Operação!
                  Valor informado é inválido!
            """)

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saques_excedidos = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("""
                         Falha na Operação!
                  Valor informado excede saldo atual!
            """)
        elif limite_excedido:
            print("""
                            Falha na Operação!
                  Valor informado excede limite de saque!
            """)
        elif saques_excedidos:
            print("""
                         Falha na Operação!
                  Número de saques diários excedido!
            """)
        elif valor > 0:
            saldo -= valor
            extrato += f"║ Operação: SAQUE    ║ Valor: R${valor:8.2f} ║\n"

            numero_saques += 1

            saques_restantes = LIMITE_SAQUES - numero_saques
            print(f"""
                      Saque realizado com sucesso!
                  
                      Número de saques restantes: {saques_restantes}
            """)
        else:
            print("""
                      Falha na Operação!
                  Valor informado é inválido!
            """)

    elif opcao == "e":
        print("╔═══════════ Extrato Bancário ═══════════╗")
        print("╠════════════════════════════════════════╣")
        print("║  Não foram encontradas movimentações!  ║" if not extrato else extrato)
        print("╠════════════════════════════════════════╣")
        print(f"║Saldo.....................: R$ {saldo:8.2f} ║")
        print("╚════════════════════════════════════════╝")

    elif opcao == "q":
        break

    else:
        print("""
                             Operação Inválida!
              Por favor, selecione novamente a operação desejada.
        """)
