import random
import sys

if len(sys.argv)==3:
    inicio = int(sys.argv[1])
    final = int(sys.argv[2])
else:
    inicio = 1
    final= 2

random_number = random.randint(inicio, final)

while True:
    try:
        guess = int(input(f"Adivina el número del {inicio} al {final}: "))
        if guess > inicio and guess < final:
             if guess == random_number:
                print("¡Muy bien!")
                break
             elif guess != random_number:
                print("NOP")
                continue
    except ValueError:
        print("Tiene que ser un número entero!")