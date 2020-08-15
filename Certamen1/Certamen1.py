def día_de_la_semana(dd,mm,aaaa):
	a = (14 - mm)//12
	y = aaaa - a
	m = mm + 12*a - 2
	d = (dd + y + y//4 - y//100 + y//400 + (31*m)//12)%7

	if d == 0:
		return "Domingo"
	elif d == 1:
		return "Lunes"
	elif d == 2:
		return "Martes"
	elif d == 3:
		return "Miércoles"
	elif d == 4:
		return "Jueves"
	elif d == 5:
		return "Viernes"
	else:
		return "Sábado"

#datos = '16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila'
datos = input("Datos de mis amigos: ")
print("Fecha de nacimiento")
dia = int(input("Día: "))
mes = int(input("Mes: "))
year = int(input("Año: "))
nacimiento_usuario = día_de_la_semana(dia,mes,year)
print("Naciste un " + nacimiento_usuario)
print("Amigos a invitar:")
i = 0
fecha = ''
nombre = ''
Flag_nombre = False
Flag_fecha = True

while i < len(datos):
	
	if datos[i] == ',':
		Flag_nombre = True
		Flag_fecha = False

	if Flag_fecha and datos[i] != ',':
		fecha += datos[i]

	if Flag_nombre and datos[i] != ',' and datos[i] != ';':
		nombre += datos[i]
	
	if datos[i] == ';' or i == len(datos)-1:
		Flag_fecha = True
		Flag_nombre = False
		d = int(fecha[:2])
		m = int(fecha[2:4])
		a = int(fecha[4:])
		if día_de_la_semana(d,m,a) == nacimiento_usuario:
			print(nombre)
		fecha = ''
		nombre = ''

	i += 1
		




