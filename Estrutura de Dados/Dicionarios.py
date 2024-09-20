# Criando dicionários

pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3415-5847"
print(pessoa)

# Acessando valores

pessoa["nome"]

# Sobrescrevendo valores

pessoa["nome"] = "Maria"
pessoa["idade"] = 18
pessoa["telefone"] = "6958-1547"

print(pessoa)

# Dicionario Aninhado


contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)

extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)

# Iterando Dicionário

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# Items

print(contatos.items())

# Get

contatos.get("chave")
contatos.get("chave", {})
print(contatos.get("guilherme@gmail.com", {}))