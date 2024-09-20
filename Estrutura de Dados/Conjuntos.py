# Exemplos básicos de 'set'

teste1 = set([1, 2, 1, 1, 3, 4])
print(teste1)

teste2 = set("teste")
print(teste2)

teste3 = set(("palio", "gol", "celta", "palio"))
print(teste3)

# Convertendo set para lista

num = {1, 2, 3, 4}
num = list(num)
print(num[0])

# Iterar conjuntos

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Union

conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))

# Intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.intersection(conjunto_b))

# Difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# Symmetric_Difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.symmetric_difference(conjunto_b))

# Issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

# Issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

# Isdisjoint

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_b.isdisjoint(conjunto_a))

# Add

sorteio = {1, 23}

print(sorteio)
sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25)
print(sorteio)

# Clear\Copy

sorteio = {1, 23}

print(sorteio)
sorteio.clear()
print(sorteio)

sorteio = {1, 23}

print(sorteio)
sorteio2 = sorteio.copy()
sorteio.clear()
print(sorteio)
print(sorteio2)

# Discard\Pop

numeros = {1, 2, 3, 4, 5, 6, 7}
numeros.discard(5)
print(numeros)
numeros.pop()
numeros.pop()
print(numeros)
numeros.remove(4)
print(numeros)