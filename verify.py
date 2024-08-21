import preguntas as p


def verificar(alternativas, eleccion):
    """
    Verifica que la eleccion haya sido la correcta.

    Parametros:
    - alternativas: list, listado de alternativas de una pregunta en especifico
    - eleccion: str, valor seleccionado como respuesta.

    Return:
    - Devuelve si la eleccion es correcta
    """
    # Convierte la elección a minúsculas y obtiene el índice
    eleccion = ["a", "b", "c", "d"].index(eleccion.lower())
    # Verifica si la alternativa elegida es la correcta
    correcto = alternativas[eleccion][1] == 1
    if correcto:
        print("Respuesta Correcta")
    else:
        print("Respuesta Incorrecta")
    return correcto


if __name__ == "__main__":
    from print_preguntas import print_pregunta

    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas["basicas"]["pregunta_2"]
    print_pregunta(pregunta["enunciado"], pregunta["alternativas"])
    respuesta = input("Escoja la alternativa correcta:\n> ").lower()
    verificar(pregunta["alternativas"], respuesta)
