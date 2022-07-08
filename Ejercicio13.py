# Escriba un programa que dados n numeros enteros, determine cual de los n-1 ultimos numeros es
# el mas cercano al primero. Por ejemplo, si el usuario introduce los numeros 2, 6, 4, 1 y 10
# el programa respondera que el numero mas cercano al 2 es el 1.

cantNumeros = int(input('Cuantos numeros va a escribir? '))
listNumeros = list(range(0, cantNumeros))

for i in listNumeros:
    num = int(input('Ingrese su numero: '))
    listNumeros[i] = num

listaCerca = []
for s in range(len(listNumeros)):
# for s in listNumeros:
    listaCerca.append(abs(listNumeros[0] - listNumeros[s]))

zipLists = list(zip(listNumeros, listaCerca))
filt = min(zipLists[1::], key=lambda x:x[-1])

print(f'La distancia mas cercana con respecto a {listNumeros[0]}\n'
      f'(Numero mas cercano, Distancia): '
      f'\n{filt}')