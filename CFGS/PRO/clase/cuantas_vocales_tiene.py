frase = input()
vocales=0

for i in frase:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vocales += 1
print(vocales)

