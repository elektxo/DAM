n=int(input("¿Cuantos numeros desea mostrar? "))
f1=0
f2=1
total=0

for i in range(n):
    if f1<=f2:
        total=total+f1
        f1=f1+f2
    else:
        total=total+f2
        f2=f2+f1
print("La suma de los ",n," primeros numeros es:",total)