def palindromo(t):
    t=list(str(t).lower())
    clean=""
    for i in range(len(t)):
        if t[i]!=" ":
            clean+=t[i]
    return clean==clean[::-1],clean

frase=input("Ingrese una frase: ")
res, frase_lim=palindromo(frase)
if res:
    print("Su frase es un palíndromo.")
else:
    print("Su frase no es un palíndromo.")
print("Longitud de la cadena limpia: ", len(frase_lim))