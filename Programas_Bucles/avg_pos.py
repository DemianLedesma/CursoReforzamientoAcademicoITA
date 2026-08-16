# bucle while
# promedio de números positivos ingresador por el usuario
# el programa termina cuando el usuario ingresa un negativo
suma=0
contador=0
while True:
    n=int(input("Ingrese un número (el cero no se tomará en cuenta): "))
    if n<0:
        break
    if n>0:
        suma+=n
        contador+=1
if contador>0:
    print(f"El promedio de los números que ingresó es {suma/contador:.2f}")
else:
    print("No se ingresaron números positivos para calcular el promedio.")
print("Fin del programa.")