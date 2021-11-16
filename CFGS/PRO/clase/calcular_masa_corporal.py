print("Escriba su peso en kg")
peso=int(input)
print("Escriba su estatura en m")
estatura=int(input)

imc=peso/(estatura*estatura)

if imc>=18.5 and imc<25:
	print("Estas mamada jode de puta")

if imc<18.5:
	print("Come algo que te quedas en los huesos")

if imc>=25 and imc<30:
	print("No te pases que te pones gordito")

if imc>=30:
	print("Tienes hacks puedes bajar rodando")