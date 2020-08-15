from random import randint
def med_fecha():
	dat_emp = {}
	archivo = open('datos.txt')
	for linea in archivo:
		datos = linea.strip().split(',')
		nom = datos[0]
		fecha = datos[1]
		if fecha not in dat_emp:
			dat_emp[fecha] = []
		gas = {'SO2':int(datos[3])}
		gas['MP10'] = int(datos[5])
		gas['NO2'] = int(datos[7])
		dat_emp[fecha].append((nom,gas))
	archivo.close()
	return dat_emp

def mas_cont(fecha, gas):
	dicc = med_fecha()
	maxi = float("-inf")
	for tuplas in dicc[fecha]:
		if int(tuplas[1][gas]) > maxi:
			maxi = int(tuplas[1][gas])
			empresa = tuplas[0]
		elif int(tuplas[1][gas]) == maxi:
			if randint(1,2) == 2:
				maxi = int(tuplas[1][gas])
				empresa = tuplas[0]
	return empresa,maxi

def estadisticas(dat_hos):
	arch = open("estadisticas.txt",'w')
	for tupla in dat_hos:
		fecha,gas = tupla
		info = mas_cont(fecha,gas)
		empresa = info[0]
		cant = str(info[1])
		arch.write(fecha + ' ' + empresa + ' ' + gas + ' ' + cant + '\n')
	arch.close()






print(med_fecha())
print (mas_cont('07/09/2018', 'NO2'))
dat_hos = [('07/09/2018','NO2'), ('07/09/2018','SO2')]
estadisticas(dat_hos)

