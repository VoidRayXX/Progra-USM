def filtrar(nombre_archivo,año):
	archivo = open(nombre_archivo, 'r')
	dicc = {}
	for linea in archivo:
		campos = linea.strip().split(':')
		ide,nombre,pais,fecha = campos
		year = int(fecha.split('-')[2])
		if pais not in dicc:
			dicc[pais] = []
		if year == año:
			dicc[pais].append(nombre)
	archivo.close()
	return dicc

def contar_ingresos(nombre_archivo,año):
	dicc = filtrar(nombre_archivo,año)
	for key in dicc:
		dicc[key] = len(dicc[key])
	return dicc

def escribir_ingresos(nombre_archivo,año):
	dicc = contar_ingresos(nombre_archivo,año)
	lista = []
	total = 0
	for pais in dicc:
		total += dicc[pais]
		lista.append((dicc[pais],pais))
	lista.sort()
	lista.reverse()
	arch = open("inmigrantes" + str(año) + ".txt",'w')
	i = 0
	for par in lista:
		if par[0] != 0:
			cant,pais = par
			arch.write(str(i) + '.- ' + pais + ': ' + str(cant) + '\n')
			i += 1
	arch.close()
	return total


print(filtrar('inmigrantes.txt', 2019))
print(contar_ingresos('inmigrantes.txt',2019))
print(escribir_ingresos('inmigrantes.txt',2019))