# bucle for
#contar las letras a en una palabra
palabra=input("Ingrese una palabra: ").lower()
contador=0
if len(palabra.split(" "))>1:
    print("Sólo se tomará la primera palabra escrita en cuenta.")
    palabra=palabra.split(" ")[0]
for l in palabra:
    if l=="a":
        contador+=1
print("La palabra", palabra, "tiene", contador, "letras a.")