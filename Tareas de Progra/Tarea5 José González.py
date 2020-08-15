from random import randint

#II-A
def es_cara():
    azar = randint(1,2)
    if azar == 1:
        return True
    else:
        return False

#II-B
def lanzamiento(monedas):
    caras = 0
    contador = 0
    while contador < monedas:
        if es_cara():
            caras += 1
        contador += 1
    return caras

#II-C
def maquina(monedas):
    rondas = 0
    while monedas > 0 :
        monedas -= lanzamiento(monedas)
        rondas += 1
    return rondas

#II-D
def intentos(monedas, pruebas):
    contador = 0
    suma = 0
    while contador < pruebas:
        suma += maquina(monedas)
        contador += 1
    promedio = float(suma/pruebas)
    return promedio

#Demostración del funcionamiento de las funciones
monedas = 10
pruebas = 1000
print(es_cara())
print(lanzamiento(monedas))
print(maquina(monedas))
print(intentos(monedas,pruebas))

#Líneas que nos permiten calcular los promedios:
monedas = 100
print(intentos(monedas,pruebas))
monedas = 1000
print(intentos(monedas,pruebas))
monedas = 10000
print(intentos(monedas,pruebas))

#Promedios de rondas para ganar el juego, en base a 1000 pruebas cada uno:
    #Promedio 10 monedas = 4.746
    #Promedio 100 monedas = 7.935
    #Promedio 1000 monedas = 11.254
    #Promedio 10000 monedas = 14.66


    
