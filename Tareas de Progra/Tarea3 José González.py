from random import randint
n = randint(65,90)
letra = chr(n)
victoria = False
letra_jugador = input("Ingresa una letra mayúsucula: ")
if letra == letra_jugador:
    print("Ganaste")
    victoria = True
elif letra < letra_jugador:
    print ("Está antes")
else:
    print("Está después")
if victoria == False:
    letra_jugador = input("Segunda oportunidad: ")
    if letra == letra_jugador:
        print("Ganaste")
        victoria = True
    elif letra < letra_jugador:
        print ("Está antes")
    else:
        print("Está después")
if victoria == False:
    letra_jugador = input("Último intento: ")
    if letra == letra_jugador:
        print("Ganaste")
    else:
        print("Lo siento, era:",letra)

