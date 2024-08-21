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

def jugar_trivia():
    os.system('cls' if sys.platform == 'win32' else 'clear') # Limpiar pantalla
    
    print("Bienvenido a la Trivia Interactiva")
    
    try:
        num_preguntas_basicas = int(input("Número de preguntas básicas (Máximo 3): "))
        num_preguntas_intermedias = int(input("Número de preguntas intermedias (Máximo 3): "))
        num_preguntas_avanzadas = int(input("Número de preguntas avanzadas (Máximo 3): "))
        
        # Validar el número de preguntas
        num_preguntas_basicas = validate(num_preguntas_basicas, 'int', 1, 3)
        num_preguntas_intermedias = validate(num_preguntas_intermedias, 'int', 1, 3)
        num_preguntas_avanzadas = validate(num_preguntas_avanzadas, 'int', 1, 3)
        
    except ValueError:
        print("Por favor, ingrese números válidos.")
        return

    preguntas_basicas = elegir_preguntas(num_preguntas_basicas, "básicas")
    preguntas_intermedias = elegir_preguntas(num_preguntas_intermedias, "intermedias")
    preguntas_avanzadas = elegir_preguntas(num_preguntas_avanzadas, "avanzadas")

    todas_preguntas = preguntas_basicas + preguntas_intermedias + preguntas_avanzadas
    random.shuffle(todas_preguntas)  # Mezclar preguntas

    n_pregunta = 0
    continuar = 'y'
    correcto = True
    op_sys = 'cls' if sys.platform == 'win32' else 'clear'

    while correcto and n_pregunta < len(todas_preguntas):
        if continuar == 'y':
            # Contador de preguntas
            n_pregunta += 1
            pregunta_actual = todas_preguntas[n_pregunta - 1]
            
            print(f'Pregunta {n_pregunta}:')
            
            enunciado = pregunta_actual['enunciado']
            level = (pregunta_actual['level'])
            
            # Imprimir el enunciado y sus alternativas en pantalla
            print_pregunta(enunciado, level)
            
            respuesta = input('Escoja la alternativa correcta (1/2/3/4): ').strip()
            
            # Validar la respuesta entregada
            respuesta = validate(respuesta, 'int', 1, 4)
            
            # Verificar si la respuesta es correcta
            level_seleccionada = level[respuesta - 1]
            correcto = level_seleccionada[1] == 1
            
            if correcto and n_pregunta < len(todas_preguntas):
                print('¡Muy bien, sigue así!')
                continuar = input('¿Desea continuar? [y/n]: ').lower()
                continuar = validate(continuar, 'str', 'y', 'n')  # Validar si es que se responde y o n
                os.system(op_sys)
            elif correcto and n_pregunta == len(todas_preguntas):
                print(f'¡Felicitaciones, has respondido {n_pregunta} preguntas correctas!\n¡Has ganado la Trivia!\nGracias por jugar, ¡hasta luego!')
                time.sleep(3)
                os.system(op_sys)
                sys.exit()
            else:
                print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas.\n¡Sigue participando!')
                time.sleep(3)
                sys.exit()
        else:
            print('Nos vemos la próxima vez, sigue practicando.')
            time.sleep(3)
            sys.exit()

if __name__ == '__main__':
    jugar_trivia()