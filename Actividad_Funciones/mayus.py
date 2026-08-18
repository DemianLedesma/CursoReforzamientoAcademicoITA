def main():
    count=0
    print("Éste programa capitaliza lo que usted ingrese y muestra al final la cantidad de veces que el programa procesó sus entradas." \
    "\nÉste programa termina cuando usted ingresa un espacio.")
    while True:
        entrada=input("Ingrese algo: ")
        if entrada==" ":break
        try:
            if entrada.isdigit():
                entrada=str(entrada)
            print(entrada.upper())
            count+=1
        except Exception as e:
            print("Error:", e)
    print("Fin del programa.")
    print(f"Cantidad de procesamientos: {count}")

main()