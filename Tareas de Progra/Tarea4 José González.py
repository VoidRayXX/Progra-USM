from math import sqrt
from random import randint
rondas = int(input("Cantidad de rondas: "))
jugadores = 3
i = 1
distancia = 0
mayor_ronda = float("inf")
ganador_ronda = ''
ganador_final = ''
mejor_tiro = float("inf")
while rondas >= i:
    print("Ronda "+str(i))
    jugadores = 3
    ganador_ronda= ''
    mayor_ronda = float("inf")
    while jugadores >= 1:
        nombre = input("Nombre: ")
        x = int(input("Coordenada x: "))
        y = int(input("Coordenada y: "))
        if -20 <= x <= 20 and -20 <= y <= 20:
            distancia = round(sqrt(x**2 + y**2),4)
            print(distancia)
            if distancia < mayor_ronda:
                mayor_ronda = distancia
                ganador_ronda = nombre
            elif distancia == mayor_ronda:
                desempate = randint(1,2)
                if desempate == 1:
                    ganador_ronda = nombre
                else:
                    ganador_ronda = ganador_ronda
        else:
            print("Disparo inválido.",nombre, "pierde el turno")
        jugadores -= 1
    print("Mejor de la ronda:",ganador_ronda,"- Distancia:",mayor_ronda)
    if mayor_ronda < mejor_tiro:
        mejor_tiro = mayor_ronda
        ganador_final = ganador_ronda
    elif mayor_ronda == mejor_tiro:
        desempate = randint(1,2)
        if desempate == 1:
            ganador_final = ganador_ronda
        else:
            ganador_final = ganador_final
    i+=1
print("Ganador(a):", ganador_final ,"- Disparo:", mejor_tiro)
