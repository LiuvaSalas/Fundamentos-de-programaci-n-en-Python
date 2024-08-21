import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {
    'basicas': [1, 2, 3],
    'intermedias': [1, 2, 3],
    'avanzadas': [1, 2, 3]
}
###############################################

def choose_q(nivel):
    """
    Elige una pregunta aleatoria del nivel especificado.
    :param nivel: str, el nivel de dificultad ('básicas', 'intermedias', 'avanzadas')
    :return: tuple, enunciado y alternativas mezcladas de la pregunta seleccionada
    """
    if nivel not in p.pool_preguntas:
        raise ValueError("Nivel no válido. Debe ser 'básicas', 'intermedias' o 'avanzadas'.")

    # Convertir el pool de preguntas del nivel especificado en una lista
    preguntas = list(p.pool_preguntas[nivel].values())

    # Seleccionar una pregunta aleatoria
    pregunta = random.choice(preguntas)

    # Mezclar las alternativas usando la función del módulo shuffle
    alternativas = shuffle_alt(pregunta['alternativas'])

    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # Ejemplo de uso con nivel 'basicas'
    for _ in range(3):  # Repetir tres veces para demostrar el funcionamiento
        pregunta, alternativas = choose_q('basicas')
        print(f'El enunciado es: {pregunta}')
        print(f'Las alternativas son: {alternativas}')
        print('-' * 50)
