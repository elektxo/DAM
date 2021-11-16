x = int(input("Introduce un numero "))
y = x

contador = 0
if y!=0:
    while y != 0:
	    contador=contador+1
	    y = y//int(10)
    pass
else:
    contador+1

print(x,"tiene",contador,"digitos")
