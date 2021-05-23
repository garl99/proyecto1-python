#Funcion para recorrer lista de ingredientes y devolver 
#cada ingrediente separados por coma
def listarIngredientes(ingredientesAgregados):
    ingredientes=''
    for ingrediente in ingredientesAgregados:
        ingredientes+=ingrediente.strip() +','
    return ingredientes[:-1]

#Funcion que pide el ingrediente y valida que sea correcto
def inputIngrediente():
    flag=True

    while(flag):
        ingredienteClave = str(input("Indique ingrediente (enter para terminar): "))
        if ingredienteClave not in ingredientes.keys() and ingredienteClave != '':
            print("=> Debe seleccionar un ingrediente correcto!!")
        else:
            break
    return ingredienteClave

#Funcion que pide el tamano y valida que sea correcto
def inputTamano():
    flag = True
    while(flag):
        tamano = str(input("Tamanos: Triple ( t ) Doble ( d ) Individual ( i ): "))
        if tamano not in opcionesValidas or tamano == '':
            print("=> Debe seleccionar un ingrediente correcto!!")
        else:
            print("Tamaño seleccionado: ", tamanos[tamano][0])
            break
    return tamano 

def printStars():
    return print("*" * 28)

printStars()
print("*      SANDWICHES UCAB     *")
printStars()

tamanos = {
    't': ['Triple', 580],
    'd': ['Doble', 430],
    'i': ['Individual', 280]
}

ingredientes = {
    'ja': ['Jamón  ', 40], 
    'ch': ['Champinones', 35], 
    'pi': ['Pimentón', 30], 
    'dq': ['Doble Queso', 40], 
    'ac': ['Aceitunas', 57.5], 
    'pp': ['Pepperoni', 38.5],
    'sa': ['Salchichón', 62.5]
}

condicion = 's'
contadorSand = 1
total = 0

while condicion == 's' or condicion == 'S':

    print("Sandwich número ", contadorSand, "\n")

    print("Opciones:")

    opcionesValidas = 'tdi'

    tamanoSand = inputTamano()

    print("\nIngredientes:")
    for key in ingredientes:
        print(ingredientes[key][0], '\t(', key, ')')

    subtotal = int(tamanos.get(tamanoSand)[1])
    cantidadIngrediente = 0
    ingredientesAgregados = []
    ingredienteClave = inputIngrediente()

    while ingredienteClave in ingredientes.keys() or ingredienteClave == '':
        
        if cantidadIngrediente != 0:
            ingredienteClave = inputIngrediente()

        if ingredienteClave == '' and cantidadIngrediente == 0:
            ingredientesAgregados.append('Queso')
            costoIngrediente = 0
            subtotal += costoIngrediente
            break
        elif ingredienteClave == '' and cantidadIngrediente > 0:
            break

        datos = ingredientes.get(ingredienteClave)
        ingredientesAgregados.append(datos[0])
        subtotal += datos[1]
        
        cantidadIngrediente += 1
    
    tamano = str(tamanos.get(tamanoSand)[0])

    print("Usted seleccionó un sandwich", tamano , "con", listarIngredientes(ingredientesAgregados))
    print("\nSubtotal a pagar por un sandwich", tamano, ": ", subtotal)

    total = total+subtotal
    
    printStars()
    condicion = str(input("Desea continuar [s/n]? "))
    printStars()
    
    if condicion == 's' or condicion == 'S':
        contadorSand += 1
    else:
        print('El pedido tiene un total de',contadorSand,'sándwich(es) por un monto de ',total,"\n")
        print('Gracias por su compra, regrese pronto')
        
print("Fin del pedido")