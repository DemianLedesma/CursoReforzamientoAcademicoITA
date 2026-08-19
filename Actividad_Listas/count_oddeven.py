def count_par_impar(numeros):
    pares=0; impares=0
    for n in numeros:
        if n%2==0: pares+=1
        else: impares+=1
    return pares, impares

nums=[]
for i in range(10):
    n=int(input("Número {}:".format(i+1)))
    nums.append(n)

e, o=count_par_impar(nums)
print("Pares: ", e)
print("Impares: ", o)