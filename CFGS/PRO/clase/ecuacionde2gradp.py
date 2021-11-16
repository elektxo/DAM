a = int(input("Escriba el coeficiente a: "))
b = int(input("Escriba el coeficiente b: "))
c = int(input("Escriba el coeficiente c: "))

discriminante = b ** 2 -4 * a * c

if discriminante >= 0:
    x1 = (-b + discriminante ** 0.5) / 2 * a
    x2 = (-b - discriminante ** 0.5) / 2 * a
    print("La ecuacion tiene solucions x1 = ", x1, "x2 = ", x2)

else:
    print("La ecuacion no tiene soluciones reales")

