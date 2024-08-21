# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys
import random


def elegir_preguntas(n_preguntas, level):
    """ Elige preguntas aleatorias del nivel especificado """
    preguntas = list(p.pool_preguntas[level].values())
    return random.sample(preguntas, min(n_preguntas, len(preguntas)))

def jugar_trivia():
    os.system('cls' if sys.platform == 'win32' else 'clear')  # Limpiar pantalla

    print("Bienvenido a la Trivia Interactiva")

    try:
        num_preguntas_basicas = int(input("Número de preguntas básicas (Máximo 3): "))
        num_preguntas_intermedias = int(input("Número de preguntas intermedias (Máximo 3): "))
        num_preguntas_avanzadas = int(input("Número de preguntas avanzadas (Máximo 3): "))

        if not 1 <= num_preguntas_basicas <= 3 or not 1 <= num_preguntas_intermedias <= 3 or not 1 <= num_preguntas_avanzadas <= 3:
            raise ValueError("El número de preguntas debe estar entre 1 y 3.")
    
    except ValueError:
        print("Por favor, ingrese números válidos.")
        return

    preguntas_basicas = elegir_preguntas(num_preguntas_basicas, "basicas")
    preguntas_intermedias = elegir_preguntas(num_preguntas_intermedias, "intermedias")
    preguntas_avanzadas = elegir_preguntas(num_preguntas_avanzadas, "avanzadas")

    todas_preguntas = preguntas_basicas + preguntas_intermedias + preguntas_avanzadas
    random.shuffle(todas_preguntas)  # Mezclar preguntas

    n_pregunta = 0
    preguntas_correctas = 0
    continuar = 'y'
    correcto = True
    op_sys = 'cls' if sys.platform == 'win32' else 'clear'

    while correcto and n_pregunta < len(todas_preguntas):
        if continuar == 'y':
            n_pregunta += 1
            pregunta_actual = todas_preguntas[n_pregunta - 1]

            print(f'Pregunta {n_pregunta}:')

            enunciado = pregunta_actual['enunciado']
            alternativas = pregunta_actual['alternativas']

            # Imprimir el enunciado y sus alternativas en pantalla
            print_pregunta(enunciado, alternativas)

            respuesta = input('Escoja la alternativa correcta (A/B/C/D): ').strip()

            a = 1
            b = 2
            c = 3
            d = 4

            if respuesta == "a":
                respuesta = a
            elif respuesta == "b":
                respuesta = b
            elif respuesta == "c":
                respuesta = c
            elif respuesta == "d":
                respuesta = d
                

            respuesta = validate([1, 2, 3, 4], respuesta)

            # Verificar si la respuesta es correcta
            alternativa_seleccionada = alternativas[int(respuesta) - 1]
            correcto = alternativa_seleccionada[1] == 1

            print("-------------------------------")
            verificar(pregunta_actual['alternativas'],respuesta)
            print("-------------------------------")

            if correcto:
                preguntas_correctas += 1
                print('¡Muy bien, sigue así!')
                continuar = input('¿Desea continuar? [y/n]: ').lower()
                continuar = validate(['y', 'n'], continuar)
                os.system(op_sys)
            else:
                print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas.\n¡Sigue participando!')
                time.sleep(3)
                sys.exit()

        else:
            print('Nos vemos la próxima vez, sigue practicando.')
            time.sleep(3)
            sys.exit()

    # Decidir el nivel basado en el porcentaje de respuestas correctas
    nivel_actual = choose_level(n_pregunta, preguntas_correctas)
    print(f'¡Felicitaciones, alcanzaste el nivel {nivel_actual} con {preguntas_correctas} respuestas correctas!')
    time.sleep(3)
    os.system(op_sys)
    sys.exit()

if __name__ == '__main__':
    jugar_trivia()