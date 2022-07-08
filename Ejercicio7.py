# Disene un programa que, dad una lista x, sustituya cualquier elemento negativo por cero.
# listaX = [1, 2, -2, -3, -5, 7]
# noNegative = list(map(lambda x: x > 0, listaX))
# print(noNegative)

listaX = [1, 2, -2, -3, -5, 7, -88, 10]
for i in range(len(listaX)):
    if listaX[i] < 0:
        listaX[i] = 0

print(listaX)