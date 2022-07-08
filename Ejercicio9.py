# Escriba un programa que almacene, en una variable x la lista obtenida con la
# funcion range(1,4) y, a continuacion, la modifique para que cada componente
# sea igual al cuadrado del componente original. El programa debe mostrar la lista resultante

variableX = range(1, 4)

listCuadrado = list(map(lambda x: x**2, variableX))

print(listCuadrado)