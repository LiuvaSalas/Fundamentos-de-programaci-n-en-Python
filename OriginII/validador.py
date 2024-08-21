
def validate(opciones, eleccion):
    # Definir validación de eleccion
    while eleccion not in opciones:
        print(f'Opción no válida, ingrese una de las opciones válidas: A/B/C/D')
        eleccion = input('Ingresa una Opción: ')
        a = 1
        b = 2
        c = 3
        d = 4

        if eleccion == "a":
            eleccion = a
        elif eleccion == "b":
            eleccion = b
        elif eleccion == "c":
            eleccion = c
        elif eleccion == "d":
            eleccion = d
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1','2','3']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(eleccion, numeros)
    
    
