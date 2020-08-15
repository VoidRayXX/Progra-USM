def traducir(archivo):
	arch = open("english.txt")
	dicc = {}
	for linea in arch:
		pal,trad = linea.strip().split(':')
		dicc[pal] = trad
	arch.close()
	book = open(archivo)
	doc = open("traducido.txt",'w')
	for line in book:
		l = line.strip().split()
		for palabra in l:
			palabra = palabra.lower()
			if palabra in dicc:
				if palabra == l[-1]:
					doc.write(dicc[palabra] + '\n')
				else:
					doc.write(dicc[palabra] + ' ')
			else:
				if palabra == l[-1]:
					doc.write(palabra + '\n')
				else:
					doc.write(palabra + ' ')
	book.close()
	doc.close()

traducir("libro.txt")

