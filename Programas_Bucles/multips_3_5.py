# bucle for
# mostrar los números que son múltiplos de 3 y de 5 del 1 al 100
print("Múltiplos comunes de 3 y 5 entre 1 y 100: ",end="")
for i in range(1, 101):
    if i%3==0 and i%5==0:
        print(i, end=", " )