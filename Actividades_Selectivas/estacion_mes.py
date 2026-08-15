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

match mes:
    case 1:
        mes_p="Enero"
    case 2:
        mes_p="Febrero"
    case 3:
        mes_p="Marzo"
    case 4:
        mes_p="Abril"
    case 5:
        mes_p="Mayo"
    case 6:
        mes_p="Junio"
    case 7:
        mes_p="Julio"
    case 8:
        mes_p="Agosto"
    case 9:
        mes_p="Septiembre"
    case 10:
        mes_p="Octubre"
    case 11:
        mes_p="Noviembre"
    case 12:
        mes_p="Diciembre"
    case _:
        mes_p=None

print(estacion if estacion=="mes inválido" else f"{mes_p} pretenece a {estacion}")