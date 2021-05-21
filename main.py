print("SANDWICHES UCAB")

tamaños = {
    't': ['Triple', 580],
    's': ['Doble', 430],
    'i': ['Individual', 280]
}

ingredientes = {
    'ja': ['Jamón  ', 40], 
    'ch': ['Champiñones', 35], 
    'pi': ['Pimentón', 30], 
    'dq': ['Doble Queso', 40], 
    'ac': ['Aceitunas', 57.5], 
    'pp': ['Pepperoni', 38.5],
    'sa': ['Salchichón', 62.5]
}

condicion = 's'
contadorSand = 1

while condicion == 's' or condicion == 'S':

    print("Sandwich número ", contadorSand)

    print("Opciones:")

    opcionesValidas = 'tdi'

    tamañoSand = str(input("Tamaños: Triple ( t ) Doble ( d ) Individual ( i ): "))

    while tamañoSand not in opcionesValidas:
        print("=> Debe seleccionar un tamaño correcto!!")
        tamañoSand = str(input("Tamaños: Triple ( t ) Doble ( d ) Individual ( i ): "))

    print("Ingredientes:")
    for key in ingredientes:
        print(ingredientes[key][0], '\t(', key, ')')

    ingrediente = str(input("Indique ingrediente (enter para terminar) "))

    while ingrediente not in ingredientes.keys() and ingrediente != '':
        print("Error")
        ingrediente = str(input("Indique ingrediente (enter para terminar) "))

    
    datos = ingredientes.get(ingrediente)
    
    if ingrediente == '':
        ingrediente = 'Queso'
        costoIngrediente = 0
    else:
        ingrediente = datos[0]
        costoIngrediente = datos[1]

    
    tamaño = str(tamaños.get(tamañoSand)[0])

    subtotal = int(tamaños.get(tamañoSand)[1]) + costoIngrediente

    print("Usted seleccionó un sandwich", tamaño , "con", ingrediente)


    print("Subtotal a pagar por un sandwich", tamaño, ": ", subtotal)
    
    condicion = str(input("Desea continuar [s/n]? "))
    
    if condicion == 's' or condicion == 'S':
        contadorSand += 1

print("finish")