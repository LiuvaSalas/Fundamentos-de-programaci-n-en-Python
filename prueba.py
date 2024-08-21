# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import random
import time
import sys
import os

# valores iniciales - 
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

print('Bienvenido a la Trivia')
opcion = input('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
        
    > ''')

while opcion not in ["0", "1"]:
    opcion = input('''Ingrese una opción valida!
        1. Jugar
        0. Salir
        
    > ''')

if opcion == '0':
    print()
    os.system(op_sys)
    # finalizar programa

print("Niveles de preguntas: \n-Basicas \n-Intermedias \n-Avanzadas")
num_preguntas = int(input("Escoge un número de preguntas por nivel (Máximo 3): "))

while num_preguntas not in [1, 2, 3]:
    num_preguntas = int(input("Ingrese un numero valido del 1 - 3: "))

preguntas_basicas = [choose_q('basicas') for i in range(num_preguntas)]
preguntas_intermedias = [choose_q('intermedias') for i in range(num_preguntas)]
preguntas_avanzadas = [choose_q('avanzadas') for i in range(num_preguntas)]

print(preguntas_basicas)
print(preguntas_intermedias)
print(preguntas_avanzadas)

# Funcionamiento de preguntas
while correcto and n_pregunta < 3*p_level:
    if n_pregunta == 0:
        #Mostramos los niveles de la trivia
        print("Niveles de preguntas: \n-Basicas \n-Intermedias \n-Avanzadas")

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
        #Mostramos los niveles de la trivia
        preguntas_basicas = [choose_q("basicas") for i in range(p_level)]
        preguntas_intermedias = [choose_q("intermedias") for i in range(p_level)]
        preguntas_avanzadas = [choose_q("avanzadas") for i in range(p_level)]

        todas_preguntas = preguntas_basicas + preguntas_intermedias + preguntas_avanzadas
        random.shuffle(todas_preguntas)

        pregunta_actual = todas_preguntas[n_pregunta - 1]

        print(f'Pregunta {n_pregunta}:')

        enunciado = pregunta_actual[0]
        alternativas = pregunta_actual[1]

        print(pregunta_actual)

        # Imprimir el enunciado y sus alternativas en pantalla
        print_pregunta(enunciado, alternativas)

        respuesta = input('Escoja la alternativa correcta:\n> ').strip().lower()
        # 7. Validar la respuesta entregada
        respuesta = validate(['a', 'b', 'c', 'd'], respuesta)

        # 8. Verificar si la respuesta es correcta o no
        correcto = verificar(alternativas, respuesta)

        print(correcto)

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
    
