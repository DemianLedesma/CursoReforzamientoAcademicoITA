# bucle while
# mostrar los números impares hasta el que ingresa el usuario

n=int(input("INgrese el número tope: "))
i=1
while True:
    if i%2!=0:
        print(i, end=", ")
    i+=1
    if i>n:
        break

print("Se han mostrado todos los números impares hasta", n)