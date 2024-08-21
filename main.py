
# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import random
import time
import os
import sys

# valores iniciales - 
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'


# ----------------------------------------

def trivia():

    # valores iniciales - 
    n_pregunta = 0
    continuar = 'y'
    correcto = True
    p_level = 10
    op_sys = 'cls' if sys.platform == 'win32' else 'clear'

    os.system(op_sys) # limpiar pantalla

    print('Bienvenido a la Trivia')
    opcion = input('''Ingrese una opción para Jugar!
            1. Jugar
            0. Salir
            
        > ''')

    while opcion not in ["0", "1"]:
        time.sleep(1)
        opcion = input('''Ingrese una opción valida!
            1. Jugar
            0. Salir
            
        > ''')

    # 2. Definir el comportamiento de Salir
    if opcion == '0':
        print()
        time.sleep(1)
        os.system(op_sys)
        # finalizar programa   

    # Funcionamiento de preguntas
    while correcto and n_pregunta < 3*p_level:
        
        if n_pregunta == 0:
            #Mostramos los niveles de la trivia
            print("Niveles: \n-Basico \n-Intermedio \n-Avanzado")

            p_level = int(input("¿Cuantas preguntas por nivel (Máximo 3): "))
            # 3. Validar el número de preguntas por nivel
            #Definimos un while para que mientras el usuario no ingrese opciones validas el programa no continue.
            while p_level not in [1, 2, 3]:
                p_level = int(input("Ingrese un numero valido del 1 - 3: "))
                time.sleep(1)
            
            total_preguntas = p_level * 3
            
        if continuar == 'y':
            #contador de preguntas
            n_pregunta += 1
            
            # 4. Escoger las preguntas por nivel.
            level = choose_level(n_pregunta, p_level)
            preguntas = choose_q(level)

            print(f'Pregunta {n_pregunta}:')

            enunciado = preguntas[0]
            alternativas = preguntas[1]

            # Imprimir el enunciado y sus alternativas en pantalla
            print_pregunta(enunciado, alternativas)
            
            respuesta = input('Escoja la alternativa correcta:\n> ').strip().lower()
            # 7. Validar la respuesta entregada
            respuesta = validate(['a', 'b', 'c', 'd'], respuesta)
            # 8. Verificar si la respuesta es correcta o no
            correcto = verificar(alternativas, respuesta)
            
            if correcto and n_pregunta < 3*p_level:
                print('Muy bien sigue así!')
                continuar = input('Desea continuar? [y/n]: ').lower()
                #9. Validar si es que se responde y o n
                continuar = validate(["y", "n"], continuar)
                os.system(op_sys)
            elif correcto and n_pregunta == 3*p_level:
                print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
                time.sleep(3)
                os.system(op_sys)
            else: 
                print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
                time.sleep(3)
                exit()
        else: 
            print('Nos vemos la proxima vez, sigue practicando')
            time.sleep(3)
            exit()
            
if __name__ == '__main__':
    trivia()
            
