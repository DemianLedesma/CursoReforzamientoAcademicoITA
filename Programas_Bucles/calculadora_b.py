# bucle while
# calculador básica con menú
print("Calculadora básica")
while True:
    print("\nMenú de opciones:")
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
    opcion=int(input("Opción: "))
    if opcion==5:
        e=input("¿Abandonar la calculadora? (s/n): ")
        if e.lower()=="s":
            print("Fin del programa.")
            break
    n1=float(input("Ingrese el primer número: "))
    n2=float(input("Ingrese el segundo número: "))
    match opcion:
        case 1:
            print("El resultado de la suma es:", n1+n2)
        case 2:
            print("El resultado de la resta es:", n1-n2)
        case 3:
            print("El resultado de la multiplicación es:", n1*n2)
        case 4:
            if n2==0:
                print("Error: No se puede dividir entre cero.")
            else:
                print(f"El resultado de la división es: {n1/n2:.10f}")
                print(f"El resultado de la división entera es: {n1//n2} con residuo {n1%n2}")