# Modulo que contiene las funciones/metodos de la app

from data import *
import time 
from tqdm.auto import tqdm
import os


# Función que imprime 28 asteriscos por pantalla
def printStars():
    return print("*" * 28)

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
        inputCupon = str(input("¿Desea aplicar un cupón de descuento? [s/n]\n"))
        if inputCupon == 's' or inputCupon == 'S':
            totalDescuento = total - agregarCuponDescuento(total)            
            if(totalDescuento == total):
                continue
            else:
                print('\nEl pedido tiene un total de: ',contadorSand,'sándwich(es) por un monto (con descuento) de: ',totalDescuento,"\n")
                break            
        else:
            break
    return 0

# Métodos de pago
def MetodoPago():

    printStars()
    print("*      Método de Pago      *")
    printStars()

    for key in metodos:
       print(metodos[key],'-',key,'\t')

    print("\n*Ingrese su metodo de  pago* ")
    pago = int(input())
    
    if pago == 1:
        cash()
    
    if pago == 2:
        paypal()

    if pago == 3:
        uphold()

    if pago == 4:    
        debito()

    elif pago == 5:
        credito()

    elif pago not in [1,2,3,4,5] :
        print("=> Debe seleccionar un metodo correcto!!")
        
    return 0

# Método que procesa los pagos (Librería externa)
def paymentProcess(process = False, address = ""):
    
    if process:
        print("\n Cargando pago... \n")        
        for i in tqdm(range(100000)):
            print(" ",end='\r')
        if address:
            print("\nEl cargo fue efectuado a la siguiente direccion: ", address)
        else:
            print("\nEl cargo fue efectuado a su cuenta.\n")            
        
    print("Gracias por su compra, regrese pronto")
    return 0

# Metodo de pago en efectivo
def cash():
    print("\n*Entregar el efectivo al delivery en el momento del despacho*")   
    paymentProcess()
    return 0

# Metodo de pago con paypal
def paypal():
    email = input("Por favor, ingrese su direccion de correo electrónico al cual le haremos el cargo del pedido: \n --> ")
    paymentProcess(True, email) 
    return 0

# Metodo de pago con uphold
def uphold():
    email = input("Por favor, ingrese su direccion de correo electrónico al cual le haremos el cargo del pedido: \n --> ")
    paymentProcess(True, email) 
    return 0

# Metodo de pago con tarjeta debito
def debito():   
    input("Por favor, ingrese los números de su tarjeta de débito  -->  ")
    input("Por favor, introduzca el código de seguridad del reverso de su tarjeta  -->  ")
    input("Por favor, introduzca el nombre del tarjetahabitante  -->  ")
    paymentProcess(True)
    return 0

# Metodo de pago con tarjeta credito
def credito():   
    input("Por favor, ingrese los números de su tarjeta de crédito  -->  ")
    input("Por favor, introduzca el código de seguridad del reverso de su tarjeta  -->  ")
    input("Por favor, introduzca el nombre del tarjetahabitante  -->  ")
    paymentProcess(True)
    return 0

# Metodo para el delivery
def delivery(contadorSand, total):
    clearConsole()
    printStars()
    print("*    Método de Entrega    *")
    printStars()
    
    print('\n1- Pick-Up')
    print('\n2- Delivery')

    print("\n*Ingrese su metodo de entrega* ")
    pago = int(input())
    
    if pago == 1:
        print('\nEl pedido tiene un total de: ',contadorSand,'sándwich(es) por un monto de: ',total,"\n")
        time.sleep(2)
        aplicarCupon(contadorSand,total) 
    
    if pago == 2:

        print("\nPor favor, ingrese su direccion exacta")
        direc = str(input())
        print("\nPor favor, introduzca el nombre de la persona que recibe")
        nombre = str(input())
        print("\nPor favor, introduzca un numero de telefono")
        cel = str(input())
        print("\nCosto del envio 800")

        total += 800
        print('\nEl pedido tiene un total de: ',contadorSand,'sándwich(es) por un monto con delivery de: ',total,"\n")
        print('Enviado a ',nombre,'en ',direc,"\n")
        time.sleep(2)
        aplicarCupon(contadorSand,total) 

    elif pago not in [1,2] :
        print("=> Debe seleccionar un metodo correcto!!")
        time.sleep(1)
        delivery(contadorSand, total)

# Funcion para limpiar la consola
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

