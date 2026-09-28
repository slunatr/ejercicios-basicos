def validar_correo(correo):
    # Enfoque 1: Si solo queremos aceptar correos de Gmail
    if correo.endswith("@gmail.com"):
        print("Enfoque 1: Correo de Gmail válido.")
    else:
        print("Enfoque 1: Rechazado (No es Gmail).")

    # Enfoque 2: Validación general (para cualquier correo como .cl o .com)
    # 1. Contamos cuántas arrobas tiene el texto
    cantidad_arrobas = correo.count("@")
    
    # 2. Buscamos en qué posición está la arroba
    posicion_arroba = correo.find("@")
    
    # 3. Buscamos un punto, pero empezando a buscar DESDE la posición de la arroba hacia adelante
    posicion_punto = correo.find(".", posicion_arroba)

    # Ahora aplicamos las condiciones lógicas con un IF
    if cantidad_arrobas != 1:
        return "Enfoque 2: Inválido. Debe tener exactamente una arroba."
        
    elif posicion_arroba == 0:
        return "Enfoque 2: Inválido. No puede empezar con una arroba (falta el usuario)."
        
    elif posicion_punto == -1:
        return "Enfoque 2: Inválido. Debe haber un punto después de la arroba."
        
    else:
        return "Enfoque 2: ¡Estructura de correo válida!"