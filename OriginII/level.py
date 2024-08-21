# level.py

def choose_level(n_pregunta, preguntas_por_nivel):
    """
    Determina el nivel de dificultad de la pregunta basado en el número de la pregunta y la cantidad de preguntas por nivel.

    :param n_pregunta: El número de la pregunta actual (1, 2, 3, etc.)
    :param preguntas_por_nivel: La cantidad de preguntas por nivel (2 o 3)
    :return: El nivel de dificultad ('básicas', 'intermedias', 'avanzadas')
    :raises ValueError: Si el número de pregunta está fuera del rango permitido o si preguntas_por_nivel no es 2 o 3.
    """
    
    if preguntas_por_nivel == 2:
        if 1 <= n_pregunta <= 2:
            return 'básicas'
        elif 3 <= n_pregunta <= 4:
            return 'intermedias'
        elif 5 <= n_pregunta <= 6:
            return 'avanzadas'
        else:
            raise ValueError("Número de pregunta fuera del rango permitido para 2 preguntas por nivel.")
    
    elif preguntas_por_nivel == 3:
        if 1 <= n_pregunta <= 3:
            return 'básicas'
        elif 4 <= n_pregunta <= 6:
            return 'intermedias'
        elif 7 <= n_pregunta <= 9:
            return 'avanzadas'
        else:
            raise ValueError("Número de pregunta fuera del rango permitido para 3 preguntas por nivel.")
    
    else:
        raise ValueError("La cantidad de preguntas por nivel debe ser 2 o 3.")

# Ejemplo de uso:
# nivel = choose_level(5, 2)  # Esto retornará 'avanzadas' si se elige 2 preguntas por nivel