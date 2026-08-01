#Estaciones del año según el mes
mes=int(input("Ingrese el número de mees (1 a 12): " ))
match mes:
    case 12 | 1 | 2:
        estacion="invierno"
    case 3 | 4 | 5:
        estacion="primavera"
    case 6 | 7 | 8:
        estacion="verano"
    case 9 | 10 | 11:
        estacion="otoño"
    case _:
        estacion="mes inválido"

print(estacion if estacion=="mes inválido" else f"{mes} pretenece a {estacion}")