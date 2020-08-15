ramo = ''
dicc = {}
while ramo != 'SALIR':
	ramo = input("Ingrese una asignatura: ")
	if ramo != 'SALIR':
		asignatura = ramo + '.txt'
		arch = open(asignatura)
		for alumno in arch:
			rut,calificaciones = alumno.strip().split(':')
			calificaciones = calificaciones.split(',')
			notas = []
			for nota in calificaciones:
				nota = int(nota)
				notas.append(nota)
			promedio = round(sum(notas)/len(notas))
			if promedio >= 55:
				estado = 'A'
			else:
				estado = 'R'
			if rut not in dicc:
				dicc[rut] = []
			dicc[rut].append((promedio,ramo,estado))
		arch.close()
			
for key in dicc:
	dicc[key].sort()
	dicc[key].reverse()
	aux = key + '.txt'
	archivo = open(aux,'w')
	for tupla in dicc[key]:
		prom,asig,est = tupla
		texto = asig + ' ' + str(prom) + ' ' + est + '\n'
		archivo.write(texto)
	archivo.close()