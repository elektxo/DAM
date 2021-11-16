numero=int(input("Introduzca el numero a analizar: "))
divisor=1
total=0
for i in range(numero):
    if (numero%divisor) == 0:
        total=total+divisor
    if numero//2<i:
        break
    divisor=divisor+1
if total==numero:
    print(numero," es un numero magico")
else:
    print(numero," no es un numero magico")