'''
Incluya sus funciones a continuación
'''
def horas_ingresos(ingresos,nombre,fecha):
    i = 0
    a = 0
    hora1 = ''
    hora2 = ''
    msj = ''
    Flag1 = True
    Flag2 = True
    texto1 = ''
#i,aux,c y a son contadores
    if nombre in ingresos and fecha in ingresos:
        while i < len(ingresos):
            aux = i + 1
            
            if ingresos[i] == nombre[0] and i == 0:
                c = i
                while ingresos[c] != "," and Flag1:
                    texto1 += ingresos[c]
                    c += 1
                    if texto1 == nombre:
                        Flag1 = False
                        c+=12
                        while a < 5:
                            hora1 += ingresos[c]
                            c+=1
                            a+=1
                        hora1 += ' '
                        a = 0
                
            
            elif ingresos[i]==";" and ingresos[aux]==nombre[0]:
                texto2 = ''
                while ingresos[aux] != "," and Flag2:
                    texto2 += ingresos[aux]
                    aux += 1
                    if texto2 == nombre:
                        Flag2 = False
                        aux+=12
                        while a < 5:
                            hora2 += ingresos[aux]
                            aux+=1
                            a+=1
                        hora2 += ' '
                        a = 0
                        Flag2 = True
                        aux = i + 1
            i+=1
    else:
        msj = 'Ingresos de '+nombre+' en '+fecha+': Sin ingresos'
        return msj
    hora_final = hora1 + hora2
    msj = 'Ingresos de '+nombre+' en '+fecha+': '+hora_final
    return msj

def ingresos_en_dia(ingresos,dia):
    acumulador = ''
    if dia not in ingresos:
        return acumulador
    i = 0
#i,aux,a y c son contadores
    while i < len(ingresos):
        if ingresos[i]==dia[0]:
            aux = i
            a = 0
            Flag = False
            c = -1
            nombre_invertido = ''
            nombre = ''
            checkeo = ''
            while a < 10 and aux < len(ingresos):
                checkeo += ingresos[aux]
                aux+=1
                a+=1
            if checkeo == dia:
                aux -= 12
                while ingresos[aux] != ";" and ingresos[aux] != "," and aux > -1:
                    nombre_invertido += ingresos[aux]
                    aux -= 1
                Flag = True
            if Flag:
                while c >= -len(nombre_invertido):
                    nombre += nombre_invertido[c]
                    c-=1
                if nombre not in acumulador:
                    acumulador += nombre + ';'
        i+=1
    return acumulador

    




'''
No modifique nada de aquí en adelante
'''

'''
Ejemplos con string del enunciado. Salida esperada (incluida la línea en blanco):
Ingresos de Juan Gallardo en 2020-04-01: 08:30 10:15
Ingresos de Ana Carmona en 2020-04-05: Sin ingresos

Juan Gallardo;Ana Carmona;
'''
ingresos = 'Juan Gallardo,2020-04-01,08:30;Ana Carmona,2020-04-01,08:35;Juan Gallardo,2020-04-01,10:15'
print(horas_ingresos(ingresos, 'Juan Gallardo', '2020-04-01'))
print(horas_ingresos(ingresos, 'Ana Carmona', '2020-04-05'))
print(ingresos_en_dia(ingresos,'2020-04-05'))
print(ingresos_en_dia(ingresos,'2020-04-01'))

'''
Pruebas adicionales. Salida esperada (incluida la línea en blanco):
Ingresos de Ada Lovelace en 2020-05-11: 11:30 15:30
Ingresos de Leonhard Euler en 2020-05-05: Sin ingresos
Ingresos de Alan Turing en 2020-05-10: 09:30
Ada Lovelace;Pythonio Algoritmio;Guido van Rossum;

Ada Lovelace;
'''
ingresos = 'Perico de los Palotes,2020-05-10,08:30;Ada Lovelace,2020-05-11,11:30;Pythonio Algoritmio,2020-05-11,08:35;Alan Turing,2020-05-10,09:30;Covidio Pandemio,2020-05-08,10:15;Ada Lovelace,2020-05-12,08:30;Guido van Rossum,2020-05-10,15:30;Leonhard Euler,2020-05-10,08:45;Ada Lovelace,2020-05-11,15:30;Pythonio Algoritmio,2020-05-02,17:35;Guido van Rossum,2020-05-11,20:30'
print(horas_ingresos(ingresos, 'Ada Lovelace', '2020-05-11'))
print(horas_ingresos(ingresos, 'Leonhard Euler', '2020-05-05'))
print(horas_ingresos(ingresos, 'Alan Turing', '2020-05-10'))
print(ingresos_en_dia(ingresos,'2020-05-11'))
print(ingresos_en_dia(ingresos,'2020-05-15'))
print(ingresos_en_dia(ingresos,'2020-05-12'))
