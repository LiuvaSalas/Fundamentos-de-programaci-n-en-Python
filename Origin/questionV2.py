import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(nivel):
    """
    Elige una pregunta aleatoria del nivel especificado.
    :param nivel: str, el nivel de dificultad ('básicas', 'intermedias', 'avanzadas')
    :return: tuple, enunciado y alternativas de la pregunta seleccionada
    """
    if nivel not in p.pool_preguntas:
        raise ValueError("Nivel no válido. Debe ser 'básicas', 'intermedias' o 'avanzadas'.")
    
    preguntas = list(p.pool_preguntas[nivel].values())
    pregunta = random.choice(preguntas)
    return pregunta['enunciado'], pregunta['alternativas']
    
    
    # escoger enunciado y alternativas mezcladas
    pregunta = 1
    alternativas = 1
    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')