n=int(input("¿Cuantos numeros desea mostrar? "))
f1=0
f2=1

for i in range(n):
    if f1<=f2:
        print(f1)
        f1=f1+f2
    else:
        print(f2)
        f2=f2+f1