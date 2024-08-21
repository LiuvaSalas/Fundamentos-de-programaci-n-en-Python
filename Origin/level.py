
  
def choose_level(n_pregunta, p_level):
  
    # Calcula el porcentaje de respuestas correctas
    porcentaje_correctas = (n_pregunta / p_level) * 100

    # Elige el nivel según el porcentaje
    if porcentaje_correctas >= 80:
        level = 'avanzadas'
    elif porcentaje_correctas >= 60:
        level = 'intermedias'
    else:
        level = 'básicas'
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias