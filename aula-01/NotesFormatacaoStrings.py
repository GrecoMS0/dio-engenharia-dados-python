'''

* Strings de múltiplas linhas

'''
nome = "Guilherme"

mensagem = f"""
Olá meu nome é {nome}
Eu estou aprendendo Python
"""

print(mensagem)

nome2 = "Guilherme"

mensagem2 = f'''
   Olá meu nome é {nome2}
 Eu estou aprendendo Python
     Essa mensagem tem diferentes recuos
'''

print(mensagem2)

print("""
    ==================== MENU ====================
    1 - Iniciar
    2 - Configurações
    3 - Sair
""")


'''

* Fatiamento de Strings

nome = "Kleber Almeida de Souza"

print(nome[0])
print("\n")
print(nome[:6])
print("\n")
print(nome[7:])
print("\n")
print(nome[7:17])
print("\n")
print(nome[7:17:2])
print("\n")
print(nome[:])
print("\n")
print(nome[::-1])
'''

'''

* Formatar Strings com f-string

pi = 3.14159

print(f"Valor de PI: {pi}")
print("\n")
print(f"Valor de PI: {pi:.2f}")
print("\n")
print(f"Valor de PI: {pi:10.2f}")
'''

'''

* Interpolação de variáveis

nome = "Marcos"
idade = 25
profissao = "Programador"
linguagem = "Python"

pessoa = {"nome": "Kleber", "idade": 28, "profissao": "Programador", "linguagem": "Python"}

print("Nome é %s. %d anos, trabalho como %s em %s" % (nome, idade, profissao, linguagem))
print("\n")
print("Nome é {}. {} anos, trabalho como {} em {}".format(nome, idade, profissao, linguagem))
print("\n")
print("Nome é {3}. {1} anos, trabalho como {0} em {2}".format(profissao, idade, linguagem, nome))
print("\n")
print("Nome é {nome}. {idade} anos, trabalho como {profissao} em {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("\n")
print("Nome é {nome}. {idade} anos, trabalho como {profissao} em {linguagem}".format(**pessoa))
print("\n")
print(f"Nome é {nome}. {idade} anos, trabalho como {profissao} em {linguagem}")
'''

'''

* Formatação de Strings

curso = "pYtHon"

print(curso.upper())
print(curso.lower())
print(curso.title())
print("\n")

curso2 = "   Python "

print(curso2.strip())
print(curso2.lstrip())
print(curso2.rstrip())
print("\n")

curso3 = "Python"

print(curso3.center(10, "#"))
print("_".join(curso3))
print("\n")

for letra in curso3:
    print(letra, end="_")
'''