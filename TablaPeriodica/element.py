import periodictable

numero_atomico = int(input('ingresa el numero atomico de un elemento: \n'))
elemento = periodictable.elements[numero_atomico]

print('Numero Atomico :', elemento.number)
print('Simbolo :', elemento.symbol)
print('Nombre :', elemento.name)
print('Masa Atomica :', elemento.mass)
print('Densidad :', elemento.density)