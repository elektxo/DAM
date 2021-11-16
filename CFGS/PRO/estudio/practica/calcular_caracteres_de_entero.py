n=int(input("Introduzca un numero: "))
cantidadcaracteres=0
while n!=0:
    n=n//10
    cantidadcaracteres=cantidadcaracteres+1
    

print("La cantidad de caracteres es de",cantidadcaracteres)