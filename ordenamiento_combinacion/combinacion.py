# Función merge_sort
def merge_sort(lista):

    if len(lista) < 2:              # preguntamos si la cantidad de elementos de la lista es menor q 2 ya q es el caso base
        return lista                # Retornamos la lista
    # De lo contrario, se divide en 2
    else:                                   # Declaramos las variables necesarias para luego enviarlas a la funcion merge 
        middle = len(lista) // 2            # Dividimos el numero de elementos de la lista para 2
        right = merge_sort(lista[:middle])  # tomamos los elementos de Derecha
        left = merge_sort(lista[middle:])   # Tomamos los elementos de Izquierda
        return merge(right, left)

# Función merge
def merge(lista1, lista2):              # Funcion merge que recibe 2 parametros
    """
        merge se encargara de intercalar los elementos de las dos
        divisiones.
    """
    i, j = 0, 0     # Variables de incremento
    result = []     # Lista de resultado

    # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]

    # Retornamos el resultados
    return result

