import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {"basicas": [1, 2, 3], "intermedias": [1, 2, 3], "avanzadas": [1, 2, 3]}
###############################################


def choose_q(dificultad):
    """
    Escoge la pregunta segun su dificultad, y elimina la pregunta del listado para no mostrarla nuevamente.

    Parametros:
    - dificultad: str, la dificultad de la pregunta
    - pool_preguntas: list, lista con las preguntas y sus alternativas

    Return:
    - Elimina la pregunta seleeccionada en la vuelta del listado.
    - Enunciado con alternativas mezcladas, para que no se consiga un patron.
    """

    # Verificar si la dificultad existe en el pool
    if dificultad not in p.pool_preguntas:
        print(f"Error: Dificultad '{dificultad}' no es válida.")
        return None, None

    # Pool preguntas según la dificultad
    preguntas = p.pool_preguntas[dificultad]

    # Verificar si hay preguntas disponibles
    if not preguntas:
        print(f"Error: No hay preguntas disponibles para la dificultad '{dificultad}'.")
        return None, None

    # Selección de la pregunta
    pregunta_clave = random.choice(list(preguntas.keys()))
    pregunta = preguntas.pop(pregunta_clave)  # Eliminar la pregunta del pool

    enunciado = pregunta["enunciado"]

    # Mezcla de las alternativas
    alternativas_mezcladas = shuffle_alt(pregunta)

    return enunciado, alternativas_mezcladas


if __name__ == "__main__":
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    nivel = input("Escoge un nivel:").strip().lower()
    pregunta, alternativas = choose_q(nivel)
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")

    pregunta, alternativas = choose_q("basicas")
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")

    pregunta, alternativas = choose_q("basicas")
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")
