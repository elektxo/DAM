print("1")
i=2
comprobante=True
while contador<=150:
    for j in range(1, i):
        resultado=i/j
        if resultado==0:
            if j!=2 or j!=3 or j!=5:
                comprobante=False
        i=i+1
    if comprobante:
        contador=contador+1
        print(i)