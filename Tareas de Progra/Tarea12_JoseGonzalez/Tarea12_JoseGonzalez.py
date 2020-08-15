def calificar(emails,respuestas,soluciones):
	dicc = {}
	for rolUSM in emails:
		noEntrega = True
		lista = []
		for rol,ejercicio,respuesta in respuestas:
			if rol == rolUSM:
				for i in range(len(soluciones[ejercicio])):
					if respuesta == soluciones[ejercicio][i][0]:
						lista.append(soluciones[ejercicio][i][1])
						noEntrega = False
			if noEntrega:
				lista.append(0)
			for k in range(len(emails[rolUSM])):
				if rolUSM not in lista:
					lista.insert(0,rolUSM)
				dicc[emails[rolUSM][k]] = lista
	
	for correo in dicc:
		promedio = sum(dicc[correo][1:])//(len(dicc[correo][1:]))
		del dicc[correo][1:]
		dicc[correo].append(promedio)
		aux = dicc[correo]
		dicc[correo] = tuple(aux)
	
	return dicc

emails = {
'2020735010':['h@gmail.com','h@usm.cl'],
'202034234k':['k@usm.cl'],
'2020987992':['lost@usm.cl']
}

respuestas = [('2020735010', 1, '1 2 3'), ('202034234k', 2, '3 1 2'),
('2020735010', 2, '1 2 3'), ('202034234k', 1, '1,3,2')]

soluciones = {1:[('1 2 3',50),('1 3 2',100)],2:[('3 1 2',70),('1 2 3',100)]}

print(calificar(emails,respuestas,soluciones))
