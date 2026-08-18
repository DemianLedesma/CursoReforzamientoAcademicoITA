from math import gcd

def mcd(n1,n2):
    a=abs(n1)
    b=abs(n2)
    if a==0 or b==0:
        return 0
    while b!=0:
        a,b=b,a%b
    return a

print(mcd(
    int(input("Ingrese su primer número: ")),
    int(input("Ingrese su segundo número: "))
    ))