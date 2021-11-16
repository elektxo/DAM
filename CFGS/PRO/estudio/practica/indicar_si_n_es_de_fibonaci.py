n=int(input("¿Cuantos numeros desea mostrar? "))
f1=0
f2=1

while f1<n and f2<n:
    
    if f1<=f2:
        if f1==n:
            print(n,"es un numero de fibonaci")
        if f1>n:
            print(n,"no es un numero de fibonaci")
        f1=f1+f2

    else:
        if f2==n:
            print(n,"es un numero de fibonaci")
        if f2>n:
            print(n,"no es un numero de fibonaci")
        f2=f2+f1
    