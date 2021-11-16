lista_alumnos=[]

while True:
    nombre=input("Escriba un nombre: ")
    if nombre=="*":
        break
    edad=int(input("Escriba una edad: "))
    lista_alumnos += [[nombre, edad]]
print(lista_alumnos)

#pregunta 1

for i in lista_alumnos:
    if i[1]>= 18:
        print(i)

#preunta 2

for i in range(len(lista_alumnos)-1):
    for j in range(i+1, len(lista_alumnos)):
        if i[1] < j[i]:
            