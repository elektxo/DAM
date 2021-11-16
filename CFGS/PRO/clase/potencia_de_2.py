n = int(input())
potencia=0
ict=0

if n != 0:
    while n > ict:
        ict=2^potencia
        potencia=potencia+1
        if ict == n:
            print(ict)
            print(potencia)
            print("Es potencia")

else:
    print("No es potencia")