numero = int(input("Escriba un numero: ")) #es el numero origen de la susecion de numeros que se va a originar
print(numero, end=" ")

while True:
    if numero == 1:
        break
    else:
        if numero%2 == 0:
            numero=numero//2
            print(numero, end=" ")
        else:
            numero=(numero*3)+1
            print(numero, end=" ")
print()