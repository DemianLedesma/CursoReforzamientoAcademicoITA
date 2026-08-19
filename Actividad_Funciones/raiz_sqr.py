from math import sqrt

def rzqd_nwt(n,tol=1e-10):
    if n<0:
        raise ValueError("Número imaginario. No existen las raíces de números negativos en los números reales.")
    estim=n/2.0
    while True:
        nv = 0.5 *(estim+n/estim)
        if abs(nv-estim)<tol:
            return nv
        estim=nv

try:
    num = float(input("Ingrese el número:  √"))
    r1=sqrt(num)
    r2=rzqd_nwt(num)
    print(f"Raíz obtenida por math.sqrt: {r1}\nRaíz calculada: {r2}")
    if abs(r1-r2)<1e-9:
        print("Los resultadso coinciden.")
    else: 
        print("Existe una diferencia significativa entre los resultados.")
except ValueError as e:
    print("Error: ", e)