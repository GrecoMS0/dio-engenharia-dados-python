lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20, 30, 30, 1])

print(lista)
l2 = lista.copy()
l2[0] = 2
lista.clear()

print(l2)
print(lista)
l2.count(30)
l2.extend(["Item0", "Item1", "Item2"])
print(l2)
#print(id(l2), id(lista))



##########################################################################

testes = ["teste0", "teste1", "teste2", "teste3", "teste4"]

for indice, teste in enumerate(testes):
    print(f"{indice}: {teste}")

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

"""
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
"""

teste = ["teste0", "teste1", "teste2", "teste3", "teste4"]

print(teste)
print(teste[2])
print(teste[0])
print(teste[-1])

teste = []
print(teste)

letras = list("python")
print(letras)
print(letras[2])

numeros = list(range(10))
print(numeros)

##########################################################################

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

##########################################################################

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

##########################################################################