año = int(input("Introduce un año: "))

if año%100==0 and año%400==0:
    print("Es bisiesto")
elif año%4==0 and año%100!=0:
    print("Es bisiesto")
else:
    print("Es bisiesto")