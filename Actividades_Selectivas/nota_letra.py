nota=float(input("ingrese la calificación de 0 a 100: "))
if nota<0 or nota>100:
    print("Error: Calificación fuera de rango (0 a 100)")
else:
    if nota >= 90:
        letra = "A"
    elif nota >= 80:
        letra = "B"
    elif nota >= 70:
        letra = "C"
    elif nota >= 60:
        letra = "D"
    else:
        letra = "F"
    print(f"La nota obtenida es {letra}")