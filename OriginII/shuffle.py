# shuffle.py
import random

def shuffle_alt(alt):
    random.shuffle(alt)
    return alt

if __name__ == '__main__':
    # Ejemplo de uso
    alternativas = [['a', 0], ['b', 1], ['c', 0]]
    alternativas_aleatorias = shuffle_alt(alternativas)
    print(f'Alternativas aleatorias: {alternativas_aleatorias}')
