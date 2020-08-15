#link youtube: https://youtu.be/8oDu0BzdRdU

def tiene_restriccion(patente, catalitico, dia):
    if catalitico == True:
        if '-' in patente:
            letra = patente[1]
        else:
            letra = patente[3]
        if dia == "LUNES" and letra <= 'G':
            return True
        elif dia == 'MIERCOLES' and letra <= 'N':
            return True
        elif dia == 'VIERNES' and letra > 'N':
                return True
        else:
            return False
    else:
        dig = int(patente[-1])
        if dia == 'LUNES' and 0 <= dig <= 3:
            return True
        elif dia == 'MIERCOLES' and 4 <= dig <= 6:
            return True
        elif dia == 'VIERNES' and 7 <= dig <= 9:
            return True
        else:
            return False
        
print(tiene_restriccion('CRTJ 32' , True , 'LUNES' ))
print(tiene_restriccion('ZZ-9999 ' , True , 'VIERNES'))
print(tiene_restriccion('RX-2134' , False , 'MIERCOLES'))
