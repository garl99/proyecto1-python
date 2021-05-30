# 
# Modulo encargado de almacenar los datos de la app


# Tamaños de los sandwich con su precio base
tamanos = {
    't': ['Triple', 580],
    'd': ['Doble', 430],
    'i': ['Individual', 280]
}

# Ingredientes con su precio adicional
ingredientes = {
    'ja': ['Jamón  ', 40], 
    'ch': ['Champinones', 35], 
    'pi': ['Pimentón', 30], 
    'dq': ['Doble Queso', 40], 
    'ac': ['Aceitunas', 57.5], 
    'pp': ['Pepperoni', 38.5],
    'sa': ['Salchichón', 62.5]
}

# Cupones con el porcentaje de descuento
cupones = {
    'XNSS10': 10,
    'NHLE15': 15,
    'GETI20': 20,
    'SXFP30': 30,
    'FARD50': 50
}

#METODO DE PAGO
metodos = {
    'CASH': 1,
    'PAYPAL': 2,
    'UPHOLD': 3,
    'DEBIDO': 4,
    'CREDITO': 5
}


opcionesValidas = 'tdi'