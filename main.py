from data import *
from functions import *


printStars()
print("*      SANDWICHES UCAB     *")
printStars()

condicion = 's'
contadorSand = 1
total = 0


while condicion == 's' or condicion == 'S':

    print("Sandwich número ", contadorSand, "\n")
    print("Opciones:")

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

    total = total + subtotal
    
    printStars()
    condicion = str(input("Desea continuar [s/n]? "))
    printStars()
    
    if condicion == 's' or condicion == 'S':
        contadorSand += 1
    else:
        print('El pedido tiene un total de',contadorSand,'sándwich(es) por un monto de ',total,"\n")   
        aplicarCupon(contadorSand,total) # Funcionalidad cupones de descuento
        
print("Fin del pedido")