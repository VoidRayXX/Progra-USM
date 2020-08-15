peli = ''
while peli != '0':
	peli = input("Película: ")
	if peli != '0':
		arch = open("clientes.txt")
		clientes = []
		for linea in arch:
			cliente = linea.strip().replace(' ', '_')
			clientes.append(cliente)
		arch.close()
		ganancia = 0
		dicc = {}
		for cliente in clientes:
			nombre = cliente.replace('_', ' ')
			precio = 2000
			arch = open(cliente + '.txt')
			for linea in arch:
				if peli == linea.strip() and precio >= 125:
					ganancia += precio
					precio /= 2
					if peli not in dicc:
						dicc[peli] = []
					if nombre not in dicc[peli]:
						dicc[peli].append(nombre)
			arch.close()
		print(ganancia)
		arch_peli = open(peli + '.txt', 'w')
		for view in dicc[peli]:
			arch_peli.write(view + '\n')
		arch_peli.close()







