from math import gcd

def mcd(n1,n2):
    a=abs(n1)
    b=abs(n2)
    if a==0 and b==0:
        return 0
    while b!=0:
        a,b=b,a%b
    return a

print("Calcular el Mínimo Común Divisor")
a=int(input("Ingrese su primer número: "))
b=int(input("Ingrese su segundo número: "))
mcdc=mcd(a,b)
mcdm=gcd(a,b)
print(f"\nMCD({a}, {b}) = {mcdc}")

print("\nComparar con la función de MATH")
print("MCDc : MCD calculado \nMCDm : MCD de 'math'\n")
print(f"MCDc={mcdc} \nMCDm={mcdm}")
print("Los resultados coinciden." if mcdc==mcdm else "Los resultados no coinciden.")
print("Fin del programa")