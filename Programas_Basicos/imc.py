#calcular el índice de masa corporal del  usuario con los datos que ingresa
print("Calculadora de Índice de Masa Corporal")
peso= float(input("Ingrese su peso en kilogramos: "))
altura=float(input("Ingrese su altura en metros (2 decimales): "))
imc=round(peso/(altura**2),2)
print("Su Índice de Masa Corporal es ", imc)