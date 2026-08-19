def invert(lista):
    inv=[]
    for i in range(len(lista)-1, -1, -1):
        inv.append(lista[i])
    return inv

lista=[]
for i in range(6):
    v=int(input(f"Número {i+1}: "))
    lista.append(v)
invertida=invert(lista)
print(f"Lista original: \n{lista} \n\nLista invertida: \n{invertida}")