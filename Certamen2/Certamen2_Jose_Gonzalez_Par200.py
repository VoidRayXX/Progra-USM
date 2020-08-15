# Link video: https://youtu.be/pv47U0XWQbw
# Nombre estudiante: José Miguel González Balmaceda
# Paralelo: 200

# Solución Pregunta 1
# Función filtrar
def filtrar(nombre_archivo, consola, mínima):
	arch = open(nombre_archivo)
	dicc = {consola:[]}
	cant_juegos = 0
	#dispo = dispositivo en el que se juega
	for linea in arch:
		calificacion = int(linea.strip().split(';')[4])
		dispo = linea.strip().split(';')[6]
		if dispo == consola and calificacion >= mínima:
			dicc[consola].append(tuple(linea.strip().split(';')))
			cant_juegos += 1
	arch.close()
	nuevo_arch = open(consola + '.txt', 'w')
	for juego in dicc[consola]:
		#Título;Jugadores;Géneros;Distribuidor;Calificación;Precio;Consola;Edades;Año
		#TÍTULO (GÉNEROS), de DISTRIBUIDOR (AÑO), con nota: CALIFICACIÓN ===== Gears of War (Action), de Microsoft (2006), con nota: 94.
		titulo,jugadores,generos,distribuidor,nota,precio,console,edad,año = juego
		nuevo_arch.write(titulo + ' (' + generos + '), ' +  'de ' + distribuidor + ' (' + año + '), '  + 'con nota: ' + str(nota) + '.\n')
	nuevo_arch.close()
	return cant_juegos

# Solución Pregunta 2
# Función rankear
def rankear(nombre_archivo):
	archivo = open(nombre_archivo)
	dicc_generos = {}
	cant_generos = 0
	for linea in archivo:
		rebanar_generos = linea.strip().split(';')[2]
		generos = rebanar_generos.split(',')
		titulo = linea.strip().split(';')[0]
		calificacion = int(linea.strip().split(';')[4])
		consola = linea.strip().split(';')[6]
		for genero in generos:
			if genero not in dicc_generos:
				dicc_generos[genero] = []
				cant_generos += 1
			dicc_generos[genero].append((calificacion,titulo,consola))
	archivo.close()
	for key in dicc_generos:
		dicc_generos[key].sort()
		dicc_generos[key].reverse()
	
	for llave in dicc_generos:
		nuevo_arch = open(llave + '.txt','w')
		nuevo_arch.write(llave + '\n')
		for juego in dicc_generos[llave][:3]:
			nota,titulo,consola = juego
			nuevo_arch.write('\t' + titulo + ' (' + consola + ')\n')
		nuevo_arch.close()
	return cant_generos


# Ejemplos utilizados en el enunciado
print(filtrar('juegos.txt','X360',90))
print(rankear('juegos.txt'))
