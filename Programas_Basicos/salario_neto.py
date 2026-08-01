#calcular el salario neto de un empleado
#usuario debe ingresar su salario bruto mensual, el porcentaje de impuestos y las deducciones adicionales
print("Calcule su Salario Neto")
bruto=float(input("Ingrese la cantidad que recibe por Salario bruto: "))
impuestos_pct=float(input("Ingrese el porcentaje que debe pagar de impuestos: "))
deducciones=float(input("Ingrese el monto de las demás deducciones:"))
impuesto_mnt=bruto*(impuestos_pct/100)
neto=bruto-impuesto_mnt-deducciones
print("Su Salario Neto es de ", neto)