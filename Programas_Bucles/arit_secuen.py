# bucle while
# crear una secuencia aritmética con los parámetros que ingresa el usuario
print("Creador de secuencia aritmética aditiva")
ini=int(input("Ingrese el número inicial de la secuencia: "))
dif=int(input("Ingrese la diferencia entre los términos: "))
lim=int(input("Ingrese el número en que debe terminar la secuencia: "))
n=ini
print(n, end="")
while True:
    n+=dif
    if n>lim:
        print(".")
        print("\nFin del programa.")
        break
    print(", ", n, end="")