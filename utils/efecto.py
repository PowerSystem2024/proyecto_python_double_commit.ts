import sys
import time


def consola(texto: str, retardo = 0.004):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(retardo)