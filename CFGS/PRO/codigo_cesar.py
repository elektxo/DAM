mensaje=input("Introduzca su mensaje secreto: ")
mensaje=mensaje.lower()
abc="abcdefghijklmnñopqrstuvwxyz"
contador=0
clave=int(input("Intrudoduzca clave numerica: "))
mensajefinal=""
i=0
letradigito=abc.find(mensaje[i])
for i in range(len(mensaje)):
    if mensaje[i]==" ":
        mensajefinal=mensajefinal+" "
    else:             
        letradigito=abc.find(mensaje[i])+clave
        if letradigito>=len(abc):
            letradigito=letradigito%len(abc)
        
        letracaracter=abc[letradigito]
        mensajefinal=mensajefinal+letracaracter
print(mensajefinal)