print("Convertidor de °C a °F y K")
c=float(input("Temperatura en °C: "))
print("1. Fahrenheit\n2.Kelvin")
opt=int(input("Convertir a: "))
match opt:
    case 1:
        resul=c*9/5+32
        unit="°F"
    case 2:
        resul=c+273.15
        unit="K"
    case _:
        resul=None
        print("Opción no válida")
if resul is not None:
    print(f"{c}°C = {resul}{unit}")