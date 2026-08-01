#calcular la nota final de un estudiante
print("Ingrese las tres calificaciones del estudiante")
ps=float(input("Parciales (0 a 100): "))
pj=float(input("Proyecto (0 a 100): "))
ef=float(input("Examen final (0 a 100): "))

st_ps= ps<0 or ps>100
st_pj= pj<0 or pj>100
st_ef= ef<0 or ef>100

if st_ps or st_pj or st_ef:
    print("Error: Calificación fuera de rango (0 a 100)")
else:
    calif_final=ps*.4+pj*.3+ef*.3
    print(f"Calificación final: {calif_final}")