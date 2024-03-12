import sys
#Filtrado 

precios = {'Notebook': 700000,
 'Teclado': 25000,
 'Mouse': 12000,
 'Monitor': 250000,
 'Escritorio': 135000,
 'Tarjeta de Video': 1500000}

def calculoUmbral(umbral, orden):
    #Inicializo variables
    auxArray = []
    message = ""

    for item in precios.items():
        if(orden == "menor"): #Valido si es menor
            if(item[1] < umbral): #Si es menor al umbral
                auxArray.append(item[0])
            message = f"Los productos menores al umbral son {', '.join(auxArray)}"
        elif(orden == "mayor"): #Valido si es mayor
            if(item[1] > umbral): #Si es mayor al umbral
                auxArray.append(item[0])
            message = f"Los productos mayores al umbral son {', '.join(auxArray)}"
        else:
            # Mensaje en caso de ingresar datos invalidos
            message = "Lo sentimos, no es una operación válida"

    return message

print(calculoUmbral(int(sys.argv[1]), sys.argv[2]))