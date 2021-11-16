import random

# (A,2,3,4,5,6,7,8,9,10,J,Q,K)
#(P)icas, (T)rebol, (C)orazones, (D)imante
#
#Baraja debe tener 52 cartas
#
#Repartir cartas

numero=("A",2,3,4,5,6,7,8,9,10,"J","Q","K")
palos=("P", "T", "C", "D")
baraja=[]

for i in numero:
    for j in palos:
        baraja+=[[i,j]]
random.shuffle(baraja)

while True:
    lista_jugador=[]
    puntos_jugador=0
    while True:
        carta=baraja.pop[0]
        lista_jugador += [carta]
        match carta[0]:
            case "J" | "K" | "Q":
                puntos_jugador+=10
            case "A":
                if puntos_jugador>10:
                    print("")

                valor=input("Quieres que valga 1 o 10? ")

for i in baraja:
    print(i)