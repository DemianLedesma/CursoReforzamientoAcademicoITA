# bucle while
# adivinar número
import random
maq= random.randint(1, 100)
while True:
    usr=int(input("Adivine el número entre 1 y 100: "))
    if usr==maq:
        print("¡Felicidades por tu puntería, Odiséo!")
        break
    elif usr<maq:
        print("¡Sigue hacia arriba, Sísifo!")
    elif usr>maq:
        print("¡No tan arriba, Ícaro!")