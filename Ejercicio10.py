# Escriba un programa que pida de forma aleatoria 20 numeros (entre el 1 y el 10), y los almacene en una lista.
# El programa debe mostrar la lista original y la lista en onrden inverso
from random import randint

listaRandom = []

for i in range(0, 20):
    listaRandom.append(randint(1, 10))

# [START:STOP:STEP]
# el reverse() no me servia y quisiera saber por que
# Me gustaria que me indique si lo que hice esta bien o podria ser mejor
listaInvertida = listaRandom[::-1]

print(f'Lista Original: {listaRandom}\nLista Invertida: {listaInvertida}')