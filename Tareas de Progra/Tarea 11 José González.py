#NO BORRE ESTE CODIGO
import os
os.system('color')

colores = [('negro','\033[0;37;48m'),
           ('blanco','\033[0;37;47m'),
           ('rojo','\033[0;37;41m'),
           ('verde','\033[0;37;42m'),
           ('amarillo','\033[0;37;43m'),
           ('azul','\033[0;37;44m'),
           ('magenta','\033[0;37;45m'),
           ('celeste','\033[0;37;46m')]

lienzo= [
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco']
]

nativo='\033[m'
#COMIENCE A PROGRAMAR ABAJO DE ESTA LINEA (NO BORRE EL CODIGO ANTERIOR)
def bits():
    bits = list(range(8))
    n1 = ' '
    for horizontal in bits:
        n1 += str(horizontal)
    return n1

def copiar_lienzo(lienzo):
    copia = []
    for b in lienzo:
        copia.append(list(b))
    return copia

def asignar_color(colores,palabra):
    for color,codigo in colores:
        if color == palabra:
            y = codigo
            return y+' '+nativo

def crear_lienzo(lienzo,colores):
    i = 0
    k = 0
    pizarra = []
    for lista in lienzo:
        pr = str(i)
        for sublista in lista:
            pr += asignar_color(colores,sublista)
            k += 1
            if k == 8:
                pizarra.append(pr)
                pr = ''
                k = 0
                i += 1
    return pizarra


decision = True

while decision:
    print("1)Crear nuevo dibujo")
    print("2)Salir")
    opcion = int(input("Seleccione una opción: "))
    while opcion != 1 and opcion != 2:
        print("¡Opción inválida!")
        print("1)Crear nuevo dibujo")
        print("2)Salir")
        opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        decision = True
    else:
        decision = False
    if decision:
        horz = bits()
        print(horz)
        fondo = crear_lienzo(lienzo,colores)
        for tramo in fondo:
            print(tramo)
        print("1)Dibujar un punto")
        print("2)Volver al menú principal")
        eleccion = int(input("Seleccione una herramienta: "))
        conservar_dibujo = True
        while eleccion == 1:
            fila = int(input("Ingrese fila: "))
            columna = int(input("Ingrese columna: "))
            color = input("Ingrese color: ")
            if conservar_dibujo:
                nuevo_lienzo = copiar_lienzo(lienzo)
                conservar_dibujo = False
            nuevo_lienzo[fila][columna] = color
            nuevo_fondo = crear_lienzo(nuevo_lienzo,colores)
            print(horz)
            for n in nuevo_fondo:
                print(n)
            print("1)Dibujar un punto")
            print("2)Volver al menú principal")
            eleccion = int(input("Seleccione una herramienta: "))
    
