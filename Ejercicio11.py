# Escriba una funcion llamada sumaEnt que reciba una lista de numeros y
# devuelva el resultado de sumarlos todos
from functools import reduce

sumaNumeros = reduce((lambda x, y: x + y), [2,2,4,4,6,7])

print(f'Sumar todos los numeros de la lista da como resultado: {sumaNumeros}')