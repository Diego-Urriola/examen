
#FUNCIONES

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}


#opc1 entregar stock ingresado
def stock_marca(stock):
    nom_marca = input("Ingrese el codigo del producto:  ")
    for stock in nom_marca:
        print(f"stock: 6" )
        if (nom_marca not in stock):
            print("NO esta en stock!")
        else:
            print("error!")
            return 

        
#validar opc2 busqueda de precio

def buscar_por_peso(precio_min, precio_max):
    resultados = []
    for nom_marca, datos in productos.items():
        precio= datos[5]
        if (precio>= precio_min and precio<= precio_max) and (productos[nom_marca][1]>0):
            resultados.append(nom_marca +"__" + datos[5])
            if resultados:
                resultados.sort()
                print("productos encontrados correctamenrte!:", resultados)
            else:
                print("no existe el producto!")
                return

    


#opc 3 listado de productos!

def ordenar_productos(orden_listado):
    if (orden_listado not in productos):
        print("Producto no encontrado!")
        if(len(orden_listado in productos)):
            print(orden_listado)
            return None;
        



#total = 0
    #total+= stock[precio][1]
    #print(f"Modelos que estan en el rango!" {precio} "es" {total})
#funcion principal

def main():
    while True:
        print("1) Stock marca")
        print("2) Búsqueda por precio")
        print("3) Listado de productos")
        print("4) Salir")

        opc = int(input("Ingrese una opcion: "))

        if (opc == 1):
            nom_marca = input("Ingrese el codigo del producto:  ")
            stock_marca(productos)
        elif(opc == 2):
            try:
                precio_min = float(input("Ingrese precio minimo:  "))
                precio_max = float(input("Ingese precio como maximo!: "))
                buscar_por_peso(precio_min, precio_max)
            except ValueError:
                print("debes ingresr valores numericos!!")

        elif(opc==3):
            orden_listado = input("Ingrese la marca: ")
            
        elif(opc == 4):
            print("programa finalizado!")
            break
        else:
            print("Debes seleccionar una opcion!")
            return 
        


if __name__ == "__main__":

    main()
