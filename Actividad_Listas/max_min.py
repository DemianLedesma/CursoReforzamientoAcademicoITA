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