#LA VARIABLE MENSAJE VA A CONTENER EL MENSAJE DE LA ACUMULACION DE TODOS LOS CARACTERES
mensaje=""

while True:
    caracter=input("Caracter a caracter de su palabra/frase: ") #la variable caracter es la guarda cada caracter que se va introduciendo el usuario
    if caracter=="@":
        break
    mensaje=mensaje+caracter
    
print(mensaje+(mensaje[::-1]))
