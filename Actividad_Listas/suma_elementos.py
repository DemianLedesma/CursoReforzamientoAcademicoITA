def sumatoria(lista):
    s=0
    for num in lista:
        s+=num
    return s

nums=[]
for i in range(5):
    n=int(input(f"Ingrese el número {i+1}: "))
    nums.append(n)

t_man=sumatoria(nums)
t_sum=sum(nums)

print(f"Total calculado: {t_man}\nTotal del sistema: {t_sum}")
print("Las sumas coinciden." if t_man==t_sum else "Las sumas no coinciden.")