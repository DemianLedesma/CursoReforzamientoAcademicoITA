# bucle while (emulación de do while) (emulación de for)
# mostrar los cuadrados de los números previos al que ingresa el usuario
n=int(input("Ingrese el número tope: "))
i=1
while i<n:
    print(f"El cuadrado de {i} es {i**2}")
    i+=1
    if i>n:
        print("Se han mostrado todos los cuadrados hasta", n)
        break