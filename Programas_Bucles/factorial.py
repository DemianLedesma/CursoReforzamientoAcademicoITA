# bucle for
# calcular el factural del numero que ingresa el usuario
num = int(input("Número a factorizar: "))
fact=1
if num<0:
    print("El factorial de los números negativos es indefinido")
else:
    for i in range(1, num+1):
        fact*=i
    print("El factorial de", num, "es", fact)