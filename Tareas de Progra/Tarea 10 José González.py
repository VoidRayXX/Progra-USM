#producto=[[Id_modelo, marca, pulgadas, GB de RAM, DD o SSD, GB de DD o SSD, procesador, tarjeta de video], ...]
productos=[
['8475HD','HP',15.6,'8GB','DD','1T','Intel Core i5','Nvidia GTX1050'],
['2175HD','lenovo',14,'4GB','SSD','512GB','Intel Core i5','Nvidia GTX1050'],
['JjfFHD','Asus',14,'16GB','SSD','256GB','Intel Core i7','Nvidia RTX2080Ti'],
['fgdxFHD','HP',15.6,'8GB','DD','1T','Intel Core i3','integrada'],
['GF75HD','Asus',15.6,'8GB','DD','1T','Intel Core i7','Nvidia GTX1050'],
['123FHD','lenovo',14,'6GB','DD','1T','AMD Ryzen 5','integrada'],
['342FHD','lenovo',15.6,'8GB','DD','1T','AMD Ryzen 7','Nvidia GTX1050'],
['UWU131HD','Dell',15.6,'8GB','DD','1T','AMD Ryzen 3','Nvidia GTX1050']]

#stock=[ [ Id_modelo, precio, stock], ...]
stock=[
['8475HD',387990,10],['2175HD',327990,4],['JjfFHD',424990,1],
['fgdxFHD',664990,21],['123FHD',290890,32],['342FHD',444990,7],
['GF75HD',749990,2],['UWU131HD',349990,1],['FS1230HD',249990,0]]

#a)
def stock_marca(marca, lista_productos, lista_stock):
    productos_copia = list(lista_productos)
    stock_copia = list(lista_stock)
    stock = 0
    modelos = []
    for datos in productos_copia:
        if datos[1].lower() == marca.lower():
            modelos.append(datos[0])
    i = 0
    for costo in stock_copia:
        if costo[0] in modelos:
            stock += stock_copia[i][2]
        i += 1
    return stock
    
#b)
def filtrar_equipos(caracteristicas, lista_productos, lista_stock):
    equipos = []
    productos_lista = []

    for lista in lista_productos:
        productos_lista.append(list(lista))
    stock_lista = []
    for info in lista_stock:
        stock_lista.append(list(info))

    requisitos = list(caracteristicas)
    k = 0

    for fila in productos_lista:
        i = 0
        j = 0
        for columna in fila:
            if columna in requisitos:
                i += 1
            if i == 3:
                equipos.append(fila)
                while j < len(requisitos):
                    equipos[k].remove(requisitos[j])
                    j += 1
                k += 1
    for x in equipos:
        aux = x[0]
        x[0] = x[1]
        x[1] = aux
        x[2: ].sort()
        for precio in stock_lista:
            if precio[0] == x[1]:
                x.append(precio[1])
                x.append(precio[2])
    equipos.sort()
    return equipos


# Prueba de las funciones
print('Probando funcion stock_marca (parte a)...')
print(stock_marca('hp', productos, stock))
print(stock_marca('LENOVO', productos, stock))
print(stock_marca('Huawei', productos, stock))

print('Probando funcion filtrar_equipos (parte b)...')
print(filtrar_equipos([15.6, '8GB', '1T'],productos,stock))
print(filtrar_equipos([14, '16GB', '256GB'],productos,stock))
print(filtrar_equipos([15.6, '16GB', '512GB'],productos,stock))

#DESCOMENTAR LAS SIGUIENTES TRES LINEAS PARA PROBAR EL DESAFIO OPCIONAL
#print(filtrar_equipos(['', 15.6, '8GB', 'DD', '1T', '', 'Nvidia GTX1050'], productos, stock))
#print(filtrar_equipos(['lenovo', '', '', '', '', '', ''], productos, stock))
#print(filtrar_equipos(['lenovo', '17', '', '', '', '', ''], productos, stock))
