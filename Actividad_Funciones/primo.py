def prime(n):
    if n<2: return False
    if n==2: return True
    if n%2==0: return False
    if n>2:
        for i in range(3, int(n**0.5)+1,2):
            if n%i==0:
                return False
        return True

num_usr=int(input("Ingrese el número a verificar: "))
if prime(num_usr): print("Primo")
else: print("No primo")