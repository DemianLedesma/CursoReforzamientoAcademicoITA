def max_calc(numeros):
    if len(numeros)==0:
        return None
    m=numeros[0]
    for num in numeros[1:]:
        if num>m:
            m=num
    return m

def min_calc(numeros):
    if len(numeros)==0:
        return None
    m=numeros[0]
    for num in numeros[1:]:
        if num<m:
            m=num
    return m

nums=[]
for i in range(8):
    v=int(input(f"Número {i+1}: "))
    nums.append(v)

maximo, minimo=max_calc(nums),min_calc(nums)
print(f"\nNúmero mayor ingresado \nCalculado: {maximo} \nSistema: {max(nums)}",
 "\nCoinciden los máximos." if maximo==max(nums) else "No coinciden.")

print(f"\nNúmero menor ingresado \nCalculado: {minimo} \nSistema: {min(nums)}",
 "\nCoinciden los mínimos." if minimo==min(nums) else "No coinciden.")
print("\n\nFin del programa.")