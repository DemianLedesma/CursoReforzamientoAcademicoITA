monto=float(input("Cantidad en MXN: "))
print("Seleccione la moneda:\n" +
    "1. USD Dólar Estadounidense\n" +
    "2. EUR Euro\n" +
    "3. THB Bath\n" +
    "4. JYP Yen Japonés\n" +    
    "5. KRW Won surcoreano\n" +
    "6. AUD Dólar australiano\n" +
    "7. PEN Sol\n" +
    "8. CAD Dólar canadiense\n" +
    "9. VES Bolívar\n" +
    "10. ARG Peso argentino\n")
opt=int(input("Convertir a: "))
match opt:
    case 1:
        res=monto/19.23
        unit="USD"
    case 2:
        res=monto/22.48
        unit="EUR"
    case 3:
        res=monto/0.57
        unit="THB"
    case 4:
        res=monto/0.14
        unit="JYP"
    case 5:
        res=monto/0.014
        unit="KRW"
    case 6:
        res=monto/13.01
        unit="AUD"
    case 7:
        res=monto/5.88
        unit="PEN"
    case 8:
        res=monto/14.38
        unit="CAD"
    case 9:
        res=monto/0.0000043
        unit="VES"
    case 10:
        res=monto/0.0071
        unit="ARG"
    case _:
        res=False
        print("Opción no válida")

if res: print(f"{monto} MXN = {res} {unit}")