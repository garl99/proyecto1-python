from data import *

# Funcion para recorrer lista de ingredientes y devolver 
# cada ingrediente separados por coma
def listarIngredientes(ingredientesAgregados):
    ingredientes = ''
    for ingrediente in ingredientesAgregados:
        ingredientes += ingrediente.strip() + ','
    return ingredientes[:-1]

# Funcion que pide el ingrediente y valida que sea correcto
def inputIngrediente():
    flag = True

    while(flag):
        ingredienteClave = str(input("Indique ingrediente (enter para terminar): "))
        if ingredienteClave not in ingredientes.keys() and ingredienteClave != '':
            print("=> Debe seleccionar un ingrediente correcto!!")
        else:
            break
    return ingredienteClave

# Funcion que pide el tamano y valida que sea correcto
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

# Función que agrega un cupon de descuento al pedido final
def agregarCuponDescuento(precioTotal):
    inputCupon = input("Introduzca cupón de descuento: ")
    
    if inputCupon in cupones.keys():
        montoFinalDescuento = precioTotal * cupones[inputCupon] / 100
        print(f"Cupón aplicado correctamente, tiene un {cupones[inputCupon]}% de descuento.\n")
    else:
        montoFinalDescuento = 0
        print("El cupón que ha ingresado no es válido.\n")
    return montoFinalDescuento        

# Función que pregunta al usuario si desea aplicar un cupón de descuento
def aplicarCupon(contadorSand, total):
    inputCupon = 's'
        
    while inputCupon == 's':
        inputCupon = str(input("¿Desea aplicar un cupón de descuento? [s/n] "))
        if inputCupon == 's' or inputCupon == 'S':
            totalDescuento = total - agregarCuponDescuento(total)            
            if(totalDescuento == total):
                continue
            else:
                print('El pedido tiene un total de',contadorSand,'sándwich(es) por un monto (con descuento) de ',totalDescuento,"\n")
                break            
        else:
            print('Gracias por su compra, regrese pronto')
            break
    return 0

# Función que imprime 28 asteriscos por pantalla
def printStars():
    return print("*" * 28)