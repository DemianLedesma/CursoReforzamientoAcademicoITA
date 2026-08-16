# bucle while
# mostrar cuando la letra que ingresa el usuario es vocal o consonante
while True:
    l= input("Letra:")
    if l==" ":
        print("Programa terminado.")
        break
    letra= l.lower() if len(l)==1 and l.isalpha() else (False if l.isalpha()==False else None)
    if letra:
        if letra in "aeiou":
            print("La letra", letra, "es vocal.")
        else:
            print("La letra", letra, "es consonante.")
    elif letra==False:
        print("Por favor, ingrese un caracter alfabético.")
    elif letra==None:
        print("Por favor, ingrese sólo una letra.") 