# Link video: https://youtu.be/B9vtSQixxuc
# Nombre estudiante: José Miguel González Balmaceda
# Paralelo: 200

def día_de_la_semana(dd,mm,aaaa):
    a = (14-mm)//12
    y = aaaa - a
    m = mm + (12*a) - 2
    d = (dd + y + (y//4) - (y//100) + (y//400) + ((31*m)//12))% 7
    if d == 0:
        return 'Domingo'
    elif d == 1:
        return 'Lunes'
    elif d == 2:
        return 'Martes'
    elif d == 3:
        return 'Miércoles'
    elif d == 4:
        return 'Jueves'
    elif d == 5:
        return 'Viernes'
    else:
        return 'Sábado'


datos = input("Datos de mis amigos: ")
print("Fecha de nacimeinto")
dd = int(input("Día: "))
mm = int(input("Mes: "))
aaaa = int(input("Año: "))
nacimiento = día_de_la_semana(dd,mm,aaaa)
print("Naciste un",nacimiento)
i = 0
fecha = ''
nombre = ''
Flag_fecha = False
Flag_nombre = False
len_8 = False
Flag4 = False
día = ''
mes = ''
año = ''
ult_nombre = ''
print("Amigos a invitar: ")
while i < len(datos):
    if datos[i] == ';':
        Flag_fecha = True
        Flag_nombre = False
        Flag4 = True
    if datos[i] == ',':
        Flag_nombre = True
        Flag_fecha = False
    if (Flag_fecha or i < 8) and datos[i] != ';':
        fecha += datos[i]
        if len(fecha) == 8:
            len_8 = True
    if Flag_nombre and datos[i] != ',' and datos[i] != ';':
        nombre += datos[i]
    if ',' not in datos[i:]:
        ult_nombre += datos[i]
        
    if len_8 and (Flag4 or i == len(datos)-1):
        día = int(fecha[0:2])
        mes = int(fecha[2:4])
        año = int(fecha[4:])
        if nacimiento == día_de_la_semana(día,mes,año):
            if Flag4:
                print(nombre)
            elif i == len(datos)-1:
                print(ult_nombre)
        fecha = ''
        nombre = ''
        len_8 = False
        Flag4 = False
            
    i += 1


    








    

'''
String de prueba
Si desea probar con los datos de prueba del enunciado, puede copiar y pegar como entrada del programa el siguiente texto:
16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila
'''
