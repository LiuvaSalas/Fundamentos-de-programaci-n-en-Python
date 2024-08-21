
  
def choose_level(total_preguntas, preguntas_correctas):
  
    # Calcula el porcentaje de respuestas correctas
    porcentaje_correctas = (preguntas_correctas / total_preguntas) * 100

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