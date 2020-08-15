#des es el desfase que hay que aplicar, por ejemplo: un desfase de 2 letras, aplicado a h, es j
seguir = True
while seguir:
    msj = input("Ingrese mensaje: ")
    des = int(input("Ingrese desfase del cifrado: "))
    i = 0
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = abc.upper()
    cifrado = ''
    #op representa la operación que se realiza con el string, letra por letra, lo que se va acumulando en la variable cifrado
    #check sirve para aplicar el desfase, y se usa para hacer que se recorra el abecedario de forma cíclica
    #n y N representan la posición de la letra en el abecedario de minusculas y mayusculas respectivamente
    #cifrado va juntando lo obtenido por op (si se trata de una letra) junto con los espacios y números que haya tenido el mensaje original
    while i < len(msj):
        op = ''
        if msj[i] in abc:
            n = abc.index(msj[i])
            check = n+des
            if check >= 26:
                check %= 26
            op = abc[check]
            cifrado += op
        elif msj[i] in ABC:
            N = ABC.index(msj[i])
            check = N+des
            if check >= 26:
                check %= 26
            op = ABC[check]
            cifrado += op
        else:
            cifrado += msj[i]
        i+=1
    print(cifrado)
    continuar = input("¿Desea seguir(si/no)?: ")
    if continuar.lower() != 'si' and continuar.lower() != 'sí':
        seguir = False