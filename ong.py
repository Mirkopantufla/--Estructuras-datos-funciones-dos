# Funcion manejadora de entradas
def calcular(**kwargs):
    for key, value in kwargs.items():
        #Por cada iteracion, se evalua si el valor de entrada es un numero o una lista
        if(type(value) == int):
            #Si es numero, ejecuta factorial
            print(factorial(value))
        elif(type(value) == list):
            #Si es numero, ejecuta factorial
            print(productoria(value))
        else:
            #Si no es ninguno de los anteriores, manda mensaje de error
            print("Se ha ingresado un valor invalido")

def productoria(list):
    #Se inicia en 1, ya que al multiplicar, el 0 arruina la multiplicación.
    result = 1
    for num in list:
        #Se guarda la multiplicacion en resultado
        result = result * num
        #Retorna el mensaje con la productoria
    return f"La productoria de {list} es {result}"

def factorial(number):
    result = 1
    for num in range(number):
        #Se guarda la multiplicacion en resultado, se suma 1 a num, ya que este inicia en 0 y arruina la multiplicación.
        result = result * (num + 1) 
        #Retorna el mensaje con la factoria
    return f"El factorial de {number} es {result}"

#Se ejecuta la funcion con todo lo descrito.
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)