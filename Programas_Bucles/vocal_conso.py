# bucle while
# mostrar cuando la letra que ingresa el usuario es vocal o consonante
while True:
    letra=input("Ingrese una letra: ").lower()
    if letra==" ": break
    if letra in "aeiou":
        print("La letra", letra, "es una vocal.")
    else:
        print("La letra", letra, "es una consonante.")
print("Programa terminado.")