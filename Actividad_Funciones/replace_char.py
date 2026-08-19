def reemplazador(t,v,n):
    if len(v)!=1 or len(n)!=1:
        return t, 0
    r=""
    c=0
    for l in t:
        if l == v:
            r+=n
            c+=1
        else: r+=l
    return r, c

texto = input("Ingrese el texto al que desea reemplazar un caracter: ")
quitar = input("Caracter a reemplazar: ")
poner = input("Caracter con el que se reemplaza: ")

if len(quitar)!=1 or len(poner)!=1:
    print("Debe ingresar un sólo caracter.")
else:
    t_m_1, num=reemplazador(texto, quitar, poner)
    t_m_2=texto.replace(quitar, poner)
    print(f"Reemplazo manual: {t_m_1}\nNúmero de caracteres reemplazados:{num}\n")
    print("Replace del sistema: ",t_m_2)
    print("Los resultados coinciden." if t_m_1==t_m_2 else "Los resultados no coinciden.")