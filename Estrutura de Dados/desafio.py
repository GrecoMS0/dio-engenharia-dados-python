import textwrap
from datetime import datetime

def menu():
    menu = """
        [d] -- Depositar
        [s] -- Sacar
        [e] -- Extrato
        [nc] - Nova Conta
        [lc] - Listar contas
        [nu] - Novo Usuário
        [q] -- Sair
    ==>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
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
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedidos = numero_saques >= limite_saques

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

        saques_restantes = limite_saques - numero_saques
        print(f"""
                Saque realizado com sucesso!

                Número de saques restantes: {saques_restantes}
        """)
    else:
        print("""
                Falha na Operação!
            Valor informado é inválido!
        """)
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("╔═══════════ Extrato Bancário ═══════════╗")
    print("╠════════════════════════════════════════╣")
    print("║  Não foram encontradas movimentações!  ║" if not extrato else extrato)
    print("╠════════════════════════════════════════╣")
    print(f"║Saldo.....................: R$ {saldo:8.2f} ║")
    print("╚════════════════════════════════════════╝")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Apenas números): ")

    while len(cpf) != 11 or not cpf.isdigit():
        print("""
                       CPF Inválido!
                    TENTE NOVAMENTE!!!
        """)
        cpf = input("Informe o CPF (Apenas números): ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("""
                    CPF já cadastrado!
                    TENTE NOVAMENTE!!!
        """)
        return

    nome = input("Informe o nome completo: ")
    while not nome.replace(" ","").isalpha() or not nome.strip():
        print("""
                       Nome Inválido!
                    TENTE NOVAMENTE!!!
        """)
        nome = input("Informe o nome completo: ")

    data_nascimento = input("Informe a data de nascimento (Formato dd-mm-aaaa): ")
    while True:
        try:
            data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y")
            break
        except ValueError:
            print("""
                    Data de Nascimento Inválida!
                        TENTE NOVAMENTE!!!
            """)
            data_nascimento = input("Informe a data de nascimento (Formato dd-mm-aaaa): ")

    endereco = input("Informe o endereço completo (Rua, Número e Bairro): ")


    cep = input("Informe o CEP (Apenas números): ")
    while len(cep) != 8:
        print("""
                       CEP Inválido!
                    TENTE NOVAMENTE!!!
        """)
        cep = input("Informe o CEP (Apenas números): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "cep": cep})

    print("""
                    Usuário criado com sucesso!
        """)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    while len(cpf) != 11 or not cpf.isdigit():
        print("""
                       CPF Inválido!
                    TENTE NOVAMENTE!!!
        """)
        cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("""
                    Conta criada com sucesso!
        """)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("""
                    Usuário não encontrado!
                Encerrando a criação de conta!!!
        """)

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
    """
    print("═" * 100)
    print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor a ser sacado: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("""
                                Operação Inválida!
                Por favor, selecione novamente a operação desejada.
            """)

main()