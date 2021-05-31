from data import *
import time 
from tqdm.auto import tqdm
import os


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
            #print('Gracias por su compra, regrese pronto')
            break
    return 0

#Metodos de pago
def MetodoPago():

    print('************************************************')
    print("*    Por Favor seleccione un metodo de Pago    *")
    print('************************************************')

    for key in metodos:
       print(metodos[key],'-',key,'\t')

    print("\n*ingrese su metodo de  pago*")
    pago = int(input())
    
    if pago == 1:
        cash()
    
    if pago == 2:
        paypal()

    if pago == 3:
        uphold()

    if pago == 4:    
        debito()

    elif pago==5:
        credito()

    elif pago not in [1,2,3,4,5] :
        print("=> Debe seleccionar un metodo correcto!!")
        
    return 0


def cash():
    print("\n*Entregar el efectivo al delivery en el momento del despacho*")
    print('Gracias por su compra, regrese pronto')
    return 1

def paypal():
    print("\n*por favor ingreser su direccion de correo electronico*")
    print("*a la cual le haremos el cargo del pedido*")
    email = str(input())
    for i in tqdm(range(100000)):
        print(" ",end='\r')
    print("\nel cargo fue efectuado a la siguiente direccion ",email)
    print('Gracias por su compra, regrese pronto')
    return 1

def uphold():
    print("\n*por favor ingreser su direccion de correo electronico*")
    print("\n*a la cual le haremos el cargo del pedido*")
    email = str(input())
    for i in tqdm(range(100000)):
     print(" ",end='\r')
    print("\nel cargo fue efectuado a la siguiente direccion ",email)
    print('Gracias por su compra, regrese pronto')
    return 1

def debito():
    print("\npor favor ingreser los numeros de su tarjeta de debito")
    TDB = str(input())
    print("\npor favor introduzca el codigo de seguridad del reverso de su tarjeta")
    ta = str(input())
    print("\npor favor introduzca el nombre del tarjetahabitante")
    ta2 = str(input())
    for i in tqdm(range(100000)):
     print(" ",end='\r')
    print("\nel cargo fue efectuado a su cuenta")
    print('Gracias por su compra, regrese pronto')
    return 1


def credito():
    print("\npor favor ingreser los numeros de su tarjeta de credito")
    TDC = str(input())
    print("\npor favor introduzca el codigo de seguridad del reverso de su tarjeta")
    ta = str(input())
    print("\npor favor introduzca el nombre del tarjetahabitante")
    ta2 = str(input())
    for i in tqdm(range(100000)):
     print(" ",end='\r')
    print("\nel cargo fue efectuado a su tarjeta de credito")
    print('Gracias por su compra, regrese pronto')
    return 1


def delivery(contadorSand, total):

    print('************************************************')
    print("*************METODO DE ENTREGA******************")
    print('************************************************')
    print('\n 1- Pick-UP')
    print('\n 2- Delivery')

    print("\n*ingrese su metodo de entrega*")
    pago = int(input())
    
    if pago == 1:
        print('El pedido tiene un total de',contadorSand,'sándwich(es) por un monto de ',total,"\n")
        time.sleep(2)
        clearConsole()
        aplicarCupon(contadorSand,total) 
    
    if pago == 2:

        print("\npor favor ingreser su direccion exacta")
        direc = str(input())
        print("\npor favor introduzca el nombre de la persona que recibe")
        nombre = str(input())
        print("\npor favor introduzca un numero de telefono")
        cel = str(input())
        print("\nCosto del envio 800")

        total += 800
        print('El pedido tiene un total de',contadorSand,'sándwich(es) por un monto con delivery de',total,"\n")
        print('Enviado a ',nombre,'en',direc,"\n")
        time.sleep(4)
        #clearConsole()
        aplicarCupon(contadorSand,total) 

    elif pago not in [1,2] :
        print("=> Debe seleccionar un metodo correcto!!")
        time.sleep(1)
        delivery(contadorSand, total)




# Función que imprime 28 asteriscos por pantalla
def printStars():
    return print("*" * 28)


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

