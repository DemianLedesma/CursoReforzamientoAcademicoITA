# bucle while
# contar los dígitos de cada número que inigresa el usuario hasta ingresar 0
print("Contador de dígitos de los números que ingrese (el programa termina cuando ingrese 0)")
while True:
    n=int(input("Número entero:"))
    if n==0: break
    else:
        cont=0
        n=abs(n)
        while n>0:
            n//=10
            cont+=1
        print("Dígitos: ",cont)