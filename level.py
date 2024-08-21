def choose_level(n_pregunta, p_level):
    
    # Verificar que la cantidad de preguntas por nivel sea válida
    if p_level not in [1, 2, 3]:
        raise ValueError("La cantidad de preguntas por nivel debe ser 1, 2 o 3")

    # Calcular el nivel de dificultad en función del número de pregunta y la cantidad de preguntas por nivel
    if p_level == 1:
        # Cada pregunta es un nivel diferente
        if n_pregunta == 1:
            return "Básico"
        elif n_pregunta == 2:
            return "Intermedio"
        elif n_pregunta == 3:
            return "Avanzado"
        else:
            raise ValueError("Número de pregunta fuera de rango")
    elif p_level == 2:
        if 1 <= n_pregunta <= 2:
            return "Básico"
        elif 3 <= n_pregunta <= 4:
            return "Intermedio"
        elif 5 <= n_pregunta <= 6:
            return "Avanzado"
        else:
            raise ValueError("Número de pregunta fuera de rango")
    elif p_level == 3:
        if 1 <= n_pregunta <= 3:
            return "Básico"
        elif 4 <= n_pregunta <= 6:
            return "Intermedio"
        elif 7 <= n_pregunta <= 9:
            return "Avanzado"
        else:
            raise ValueError("Número de pregunta fuera de rango")
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias