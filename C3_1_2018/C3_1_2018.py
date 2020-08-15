def leer_perros(na):
	dicc = {}
	arch = open(na)
	for linea in arch:
		fecha,nombre,raza,prob,sol = linea.strip().split(';')
		if nombre not in dicc:
			dicc[nombre] = []
		dicc[nombre].append(sol)
	arch.close()
	return dicc

def leer_raza(nombre_archivo):
	dicc = {}
	arch = open(nombre_archivo)
	for linea in arch:
		fecha,nombre,raza,prob,sol = linea.strip().split(';')
		if raza not in dicc:
			dicc[raza] = []
		dicc[raza].append(nombre)
	arch.close()
	return dicc

def mestizos(raza1,raza2,nombre_archivo):
	dicc = leer_raza(nombre_archivo)
	lista = []
	for nombre in dicc[raza1]:
		if nombre in dicc[raza2]:
			lista.append(nombre)
	return lista

def solucion_mestizos(raza1,raza2,nombre_archivo):
	mesti = mestizos(raza1,raza2,nombre_archivo)
	perros = leer_perros(nombre_archivo)
	contador = {}
	for perro in mesti:
		
		sol = perros[perro][0]
		
		if sol not in contador:
			contador[sol] = 0
		contador[sol] += 1

	return contador


print(leer_perros("perros.txt"))
print(leer_raza("perros.txt"))
print(mestizos("salchicha","san bernardo","perros.txt"))
print(mestizos("pequines","labrador","perros.txt"))
print(mestizos("pequines","pastor aleman","perros.txt"))
print(solucion_mestizos("salchicha","san bernardo","perros.txt"))
print(solucion_mestizos("pequines","labrador","perros.txt"))