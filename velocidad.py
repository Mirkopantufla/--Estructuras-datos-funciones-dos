#Listar las posiciones de los mayores al promedio

velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

def sobrePromedio(list):
    # Inicializo variables
    promedio = 0
    posicionesFiltradas = []

    # Calculo el promedio antes de filtrar
    for num in list:
        promedio += num

    promedio = promedio/len(list)

    for index, num in enumerate(list):
        # Si el numero es mayor al primedio
        if(num > promedio):
            # Guardo las posiciones filtradas en un arreglo
            posicionesFiltradas.append(index)
    # Retorno las posiciones
    return posicionesFiltradas

print(sobrePromedio(velocidad))