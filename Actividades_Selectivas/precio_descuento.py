#calcular el precio final luego de aplucar un descuento
precio =float(input("Precio original del producto: "))
if precio <= 100:
    descuento=0
elif precio <=200:
    descuento=0.1
elif precio <=500:
    descuento=0.2
else:
    descuento=0.25
precio_final=precio-(precio*descuento)
print(f"Precio con descuento: {precio_final}")