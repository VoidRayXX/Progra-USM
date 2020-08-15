from math import sqrt
def agregar_colegio(arch1, arch2, cod, nombre, religion, arancel, ubicacion, ingles, simce, psu):
	colegios = open(arch1,'a')
	colegios.write('\n' + cod + '-' + nombre)
	colegios.close()
	resultados = open(arch2,'a')
	x,y = ubicacion
	resultados.write('\n' + cod + '@' + religion + '@' + str(arancel) + '@' + str(x) + '#' + str(y) + '@' + str(ingles) + '@' + str(simce) + '@' + str(psu))
	resultados.close()

def actualizar_colegio(archivo, codigo, arancel, ingles, simce, psu):
	arch = open(archivo)
	info = []
	no_entro = True
	posiciones = [0,2,4,5,6]
	variables = [codigo,str(arancel),str(ingles),str(simce),str(psu)]
	for linea in arch:
		line = linea.strip()
		l = linea.strip().split('@')
		cod = l[0]
		if cod == codigo:
			religion,ubicacion = (l[1],l[3])
			no_entro = False
			aux = ''
			j = 0
			datos = []
			for i in posiciones:
				datos.append(l[i].replace(l[i],variables[j]))
				j += 1
			for k in range(len(datos)):
				if datos[k] != datos[-1]:
					if k == 1:
						aux += religion + '@'
					elif k == 2:
						aux += ubicacion + '@'
					aux += datos[k] + '@'
				else:
					aux += datos[k]
			line = aux
		info.append(line)
	arch.close()

	if no_entro:
		return False
	
	arch = open(archivo,'w')
	for linea in info:
		arch.write(linea + '\n')
	arch.close()
	return True

def clasificar(archivo):
	arch = open(archivo)
	dicc = {}
	for linea in arch:
		l = linea.strip().split('@')
		cod,religion,re,ara,ubi,simce,psu = l
		if religion not in dicc:
			dicc[religion] = []
		dicc[religion].append(cod)
	arch.close()
	return dicc

def filtrar(arch1, arch2, religion, apoderado, umbral):
	x1,y1 = apoderado
	colegios = open(arch2)
	religiones = clasificar(arch1)
	candidatos = religiones[religion]
	dicc = {}
	for linea in colegios:
		cod = linea.strip().split('-')[0]
		if cod in candidatos:
			nombre = linea.strip().split('-')[1]
			if cod not in dicc:
				dicc[cod] = []
			dicc[cod].append(nombre)
	colegios.close()
	resultados = open(arch1)
	for linea in resultados:
		cod,rel,ara,ubicacion,ingles,simce,psu = linea.strip().split('@')
		if cod in dicc:
			dicc[cod].append((rel,ara,ubicacion,simce,psu))
	resultados.close()
	arch = open("filtro.txt",'w')
	for key in dicc:
		coord = dicc[key][1][2].split('#')
		x2 = float(coord[0])
		y2 = float(coord[1])
		#print(key,x2,x1,y2,y1)
		distancia = sqrt((x1 - x2)**2 + (y1 - y2)**2)
		#print(distancia,umbral)
		if distancia <= umbral:
			nombre = dicc[key][0]
			rel,ara,ubicacion,ingles,simce,psu = dicc[key][1]
			arch.write(nombre + '#' + ara + '#' + distancia + '#' + psu + '\n')
	arch.close()

#03@Laico@103990@0.9#102.8@4@235@750  !=  03@Laico@149990@0.9#102.8@5@245@758
#agregar_colegio("colegios.txt","resultados.txt","11","Python School","Laico",79990,(-15.3,105.2),4,175,621)
#print(actualizar_colegio("resultados.txt", "03", 149990, 5, 245, 758))
#print(actualizar_colegio("resultados.txt", "63", 49990, 2, 156, 558))
#print(clasificar("resultados.txt"))
filtrar("resultados.txt", "colegios.txt", "Laico", (10,-15), 25)