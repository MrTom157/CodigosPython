#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10],
        '2175HD': [327990,4],
        'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21],
        '123FHD': [290890,32],
        '342FHD': [444990,7],
        'GF75HD': [749990,2],
        'UWU131HD': [349990,1],
        'FS1230HD': [249990,0],
}
            
def stock_marca(marca):
    for modelo in productos:
        if marca in productos[modelo][0]:
            print(f"----------\nModelo Encontrado: {modelo}")
            if modelo in stock:
                print(f"Stock: {stock[modelo][1]}\n----------")

def busqueda_precio(precioMinimo, precioMaximo):
    for modelo in stock:
        
        if stock[modelo][0]>precioMinimo and stock[modelo][0]<precioMaximo:
            print(f"-----ENCONTRADO-----\nModelo: {modelo}\nPrecio: ${stock[modelo][0]}\n--------------------")

def actualizar_precio(modelo):
    for n in stock:
        if modelo in stock:
            actualizarOpcion=input(f"Modelo encontrado, su precio: ${stock[modelo][0]} desea cambiar su precio? (si-no) ")
            if actualizarOpcion=="si":
                nuevoValor=int(input("Ingrese el nuevo valor del modelo: "))
                stock[modelo][0]=nuevoValor
                break
        else:
            break
            


while True:
    print(f"***MENU PRINCIPAL***\n1. Stock Marca\n2. Busqueda por precio\n3. Actualizar precio\n4. Salir")
    try:
        opcion=int(input())
        if opcion>4:
            print("Solo valores admitidos (1-2-3-4)")
        match(opcion):
            case 1:
                marca=input("ingrese marca a consultar (lenovo, Asus, HP, Dell) ")
                stock_marca(marca)
            case 2:
                try:
                    precioMinimo=int(input("Ingrese el precio minimo "))
                    precioMaximo=int(input("Ingrese el precio maximo "))
                    busqueda_precio(precioMinimo, precioMaximo)
                except ValueError:
                    print("----------\nSolo valores enteros\n----------")
            case 3:
                updatePrecio=input("Escriba modelo a actualizar: ")
                actualizar_precio(updatePrecio)
                print("Precio actualizado!!!")

            case 4:
                print("Programa Finalizado.")
                break
    except ValueError:
        print("Solo valores admitidos (1-2-3-4) ")