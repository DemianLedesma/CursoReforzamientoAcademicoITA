# bucle for
# contar los negativos, positivos y ceros entre los números ingresados por el usuario
n=int(input("Ingrese la cantidad de números a evaluar: "))
negativos=0
positivos=0
ceros=0
for i in range(n):
    num=int(input("Ingrese un número: "))
    if num<0:
        negativos+=1
    elif num>0:
        positivos+=1
    else:
        ceros+=1
print("Números negativos (menores a cero):", negativos)
print("Números positivos (mayores a cero):", positivos)
print("Números cero (iguales a cero):", ceros)