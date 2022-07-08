# Escriba un programa que pida de forma aleatoria una lista de valores numericos.
# A partir de esta lista se deben generar dos listas mas: una con los valores de
# indice par y otra con los valores de indice impar. Muestre las tres listas

from random import randint
listaAlea = [randint(0,15), randint(0,15), randint(0,15), randint(0,15), randint(0,15), randint(0,15)]

# def modNum(x):
#     return (x%2)
#
# for i in listaAlea:
listaPar = list(filter(lambda x: x%2 == 0, listaAlea))
listaImpar = list(filter(lambda x: x%2 == 1, listaAlea))

print(f'Lista Original: {listaAlea}\nLista Pares: {listaPar}\nLista Impares: {listaImpar}')