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
        inputCupon = str(input("¿Desea aplicar un cupón de descuento? [s/n] "))
        if inputCupon == 's' or inputCupon == 'S':
            totalDescuento = total - agregarCuponDescuento(total)            
            if(totalDescuento == total):
                continue
            else:
                print('El pedido tiene un total de: ',contadorSand,'sándwich(es) por un monto (con descuento) de: ',totalDescuento,"\n")
                break            
        else:
            #print('Gracias por su compra, regrese pronto')
            break
    return 0

# Métodos de pago
def MetodoPago():

    printStars()
    print("*      Método de Pago      *")
    printStars()

    for key in metodos:
       print(metodos[key],'-',key,'\t')

    print("\n *Ingrese su metodo de  pago* ")
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

def cash():
    print("\n *Entregar el efectivo al delivery en el momento del despacho*")
    
    # print('Gracias por su compra, regrese pronto')
    
    paymentProcess()
    return 0

def paypal():
    # print("\n*por favor ingreser su direccion de correo electronico*")
    # print("*a la cual le haremos el cargo del pedido*")
    # email = str(input())

    email = input("Por favor, ingrese su direccion de correo electrónico al cual le haremos el cargo del pedido: \n --> ")
    
    # for i in tqdm(range(100000)):
    #     print(" ",end='\r')
    # print("\nel cargo fue efectuado a la siguiente direccion ",email)
    # print('Gracias por su compra, regrese pronto')
    
    paymentProcess(True, email) 
    return 0

def uphold():
    # print("\n*por favor ingreser su direccion de correo electronico*")
    # print("\n*a la cual le haremos el cargo del pedido*")
    # email = str(input())
    
    email = input("Por favor, ingrese su direccion de correo electrónico al cual le haremos el cargo del pedido: \n --> ")
    
    # for i in tqdm(range(100000)):
    #  print(" ",end='\r')
    # print("\nel cargo fue efectuado a la siguiente direccion ",email)
    # print('Gracias por su compra, regrese pronto')
    
    paymentProcess(True, email) 
    return 0

def debito():
    # print("\n Por favor, ingreser los numeros de su tarjeta de debito")
    # TDB = str(input())
    # print("\n Por favor, introduzca el codigo de seguridad del reverso de su tarjeta")
    # ta = str(input())
    # print("\n Por favor, introduzca el nombre del tarjetahabitante")
    # ta2 = str(input())
    
    input("Por favor, ingrese los números de su tarjeta de débito  -->  ")
    input("Por favor, introduzca el código de seguridad del reverso de su tarjeta  -->  ")
    input("Por favor, introduzca el nombre del tarjetahabitante  -->  ")
    
    # for i in tqdm(range(100000)):
    #  print(" ",end='\r')
    # print("\nel cargo fue efectuado a su cuenta")
    # print('Gracias por su compra, regrese pronto')
    
    paymentProcess(True)
    return 0


def credito():
    # print("\n Por favor, ingrese los numeros de su tarjeta de credito")
    # TDC = str(input())
    # print("\n Por favor, introduzca el codigo de seguridad del reverso de su tarjeta")
    # ta = str(input())
    # print("\n Por favor, introduzca el nombre del tarjetahabitante")
    # ta2 = str(input())
    
    input("Por favor, ingrese los números de su tarjeta de crédito  -->  ")
    input("Por favor, introduzca el código de seguridad del reverso de su tarjeta  -->  ")
    input("Por favor, introduzca el nombre del tarjetahabitante  -->  ")
    
    # for i in tqdm(range(100000)):
    #  print(" ",end='\r')
    # print("\n El cargo fue efectuado a su tarjeta de credito")
    # print('Gracias por su compra, regrese pronto')
    
    paymentProcess(True)
    return 0


def delivery(contadorSand, total):

    printStars()
    print("*    Método de Entrega    *")
    printStars()
    
    print('\n 1- Pick-Up')
    print('\n 2- Delivery')

    print("\n *Ingrese su metodo de entrega* ")
    pago = int(input())
    
    if pago == 1:
        print('El pedido tiene un total de: ',contadorSand,'sándwich(es) por un monto de: ',total,"\n")
        time.sleep(2)
        clearConsole()
        aplicarCupon(contadorSand,total) 
    
    if pago == 2:

        print("\n Por favor, ingrese su direccion exacta")
        direc = str(input())
        print("\n Por favor, introduzca el nombre de la persona que recibe")
        nombre = str(input())
        print("\n Por favor, introduzca un numero de telefono")
        cel = str(input())
        print("\n Costo del envio 800")

        total += 800
        print('El pedido tiene un total de: ',contadorSand,'sándwich(es) por un monto con delivery de: ',total,"\n")
        print('Enviado a ',nombre,'en ',direc,"\n")
        time.sleep(4)
        #clearConsole()
        aplicarCupon(contadorSand,total) 

    elif pago not in [1,2] :
        print("=> Debe seleccionar un metodo correcto!!")
        time.sleep(1)
        delivery(contadorSand, total)

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

