def decifrar(simbolo,morse):
    deco = ''
    for text,codigo in morse:
        if simbolo == codigo:
            deco += text.lower()
    return deco

morse = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
    ('F', '..-.'), ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'),
    ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'), ('0', '-----'), ('1', '.----'), ('2', '..---'),
    ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'),
    ('7', '--...'), ('8', '---..'), ('9', '----.'), (' ', ' ')
    ]

seguir = True
while seguir:
    print("1)Transformar mensaje a Código Morse")
    print("2)Decifrar mensaje en Código Morse")
    eleccion = int(input("Seleccione una opción: "))
    while eleccion != 1 and eleccion != 2:
        print("Opción inválida")
        eleccion = int(input("Seleccione una opción: "))
    
    #se le pide elegir una opción al usuario
    
    
    if eleccion == 1:
        msj = input("Ingrese mensaje a convertir a código morse: ")
        cod = ''
        for letra in msj:
            for tupla in morse:
                if letra.upper() == tupla[0]:
                    cod += tupla[1] + ' '
        print(cod)
    #cod representa el mensaje convertido a código morse
    
    else:
        msj2 = input("Ingrese mensaje a descifrar: ")
        msj2 += ' '
        seg_msj = []
        a = ''
        i = 0
        while i < len(msj2):
            if msj2[i] != ' ':
                a += msj2[i]
            else:
                seg_msj.append(a)
                a = ''
            i += 1
        decifrado = ''
        for k in range(len(seg_msj)):
            decifrado += decifrar(seg_msj[k],morse)
        print(decifrado)
    continuar = input("¿Desea seguir(si/no)?: ")
    if continuar.lower() != 'si' and continuar.lower() != 'sí':
        seguir = False