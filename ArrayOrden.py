

def ordenar_al_reves(arreglo):
    # 1. Definimos las posiciones de los extremos
    izquierda = 0
    derecha = len(arreglo) - 1
    
    # 2. El bucle corre mientras los extremos no se crucen en el centro
    while izquierda < derecha:
        # 3. Intercambiamos los valores de las dos posiciones
        # Guardamos el valor de la izquierda en una variable temporal para no perderlo
        temporal = arreglo[izquierda]
        
        # Ponemos el número del final en la posición del principio
        arreglo[izquierda] = arreglo[derecha]
        
        # Ponemos el número que guardamos en la posición del final
        arreglo[derecha] = temporal
        
        # 4. Movemos los índices hacia el centro
        izquierda = izquierda + 1
        derecha = derecha - 1
        
    return arreglo

# --- PRUEBA DEL CÓDIGO ---
mi_lista = [10, 20, 30, 40, 50]
print("Original:", mi_lista)

lista_invertida = ordenar_al_reves(mi_lista)
print("Invertida:", lista_invertida) 
# Imprime: [50, 40, 30, 20, 10]