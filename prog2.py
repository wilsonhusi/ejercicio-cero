# Juego de Adivinar el Número

import random

# Juego de adivinanza
numero_secreto = random.randint(1, 20)
intentos = 0

print("Estoy pensando en un número entre 1 y 20. ¡Adivínalo!")

while True:
    intento = int(input("Introduce tu número: "))
    intentos += 1
    
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta otra vez.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta otra vez.")
    else:
        print(f"¡Felicidades! Acertaste en {intentos} intentos.")
        break
