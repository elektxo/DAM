mensaje=input("Escriba su mensaje para encriptar: ") #es el mensaje que se desea encriptar
clave=int(input("Introduzca su clave: ")) #la clave con la que se encripta
mensajeencriptado="" #el mensaje final es el resultado de encriptar el mensaje
abc="abcdefghijklmnñopqrstuvwxyz" #esta es obvio

if clave>13:
    clave=clave%13

for i in range(len(mensaje)):
    if mensaje[i] == "n":
        mensajeencriptado=mensajeencriptado+"n"
    else:
        if abc.find(mensaje[i]) < 14:
            indicadorletra=abc.find(mensaje[i])-clave  #el indicador de letra es un entero que va a apuntar la posicion del abc que tiene que añadirle al mensaje final
            if indicadorletra<0:
                indicadorletra=indicadorletra+13
            mensajeencriptado=mensajeencriptado+abc[indicadorletra]
        else:
            indicadorletra=abc.find(mensaje[i])+clave
            if indicadorletra>27:
                indicadorletra=indicadorletra-13
            mensajeencriptado=mensajeencriptado+abc[indicadorletra]
print(mensajeencriptado)