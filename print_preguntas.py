import preguntas as p

def print_pregunta(enunciado, alternativas):
    """
    Imprime el enunciado de la pregunta y las alternativas en pantalla.

    :param enunciado: str, el enunciado de la pregunta
    :param alternativas: list, lista de alternativas para la pregunta
    """
    # Imprimir enunciado y alternativas
    print(enunciado)

    opciones = ["A", "B", "C", "D"]
    for i, alternativa in enumerate(alternativas):
        print(f"{opciones[i]}. {alternativa[0]}")

if __name__ == '__main__':
    # Prueba para verificar que el enunciado y alternativas se imprimen correctamente
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'][0], pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4