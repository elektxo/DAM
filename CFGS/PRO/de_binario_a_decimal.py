digito=input("Introduzca su numero binario: ")
digitoinvertido=digito[::-1]
vueltas=len(str(digito))
potencia=len(str(digito))-1
resultado=0

for i in range(vueltas):
    if str(digitoinvertido)[potencia]=="1": 
        resultado=resultado+2**potencia
        potencia=potencia-1
    else:
        potencia=potencia-1

print(resultado)