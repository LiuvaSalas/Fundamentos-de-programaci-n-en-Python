def validate(opciones, eleccion):
    """
    Valida que la eleccion sea parte del listado de opciones.

    Parametros:
    - opciones: list, listado de opciones dispponibles a escoger.
    - eleccion: str/int,valor escogido que posteriormente se compara con el listado de opciones.

    Return:
    - devuelve la eleccion validada.
    """
    while eleccion not in opciones:
        print(f"Opción no válida, ingrese una de las opciones válidas: {opciones}")
        eleccion = input("Ingrese una nueva opcion: ")
    return eleccion


if __name__ == "__main__":

    eleccion = input("Ingresa una Opción: ").lower()
    letras = [
        "a",
        "b",
        "c",
        "d",
    ]  # pueden probar con letras también para verificar su funcionamiento.
    # numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(letras, eleccion)
