#===================================
#Sitema de gestion de inventario de una libreria
#===================================
#lista de almacen

inventario=[]
def registrar_libro():
    codigo=input("Ingrese el codigo del libro: ")
    
    #validar codigo repetido
    for libro [i] in inventario:
        if libro["codigo"]==codigo:
            print("el libro ya existe")
            return
        
    titulo=input("Ingrese titulo: ")
    autor=input("Ingrese autor: ")

    try:
        cantidad=int(input("Ingrese cantidad: "))
        precio=int(input("Ingrese precio: "))
    except ValueError:
        print(
            "codigo":codigo,
            "titulo":titulo,
            "autor":autor,
            "cantidad":cantidad,
            "precio":precio
            
        )
        inventario.append(libro)
        print("Libro registrado con exito")

def buscar_libro():
    codigo=int(input("Ingrese el codigo del libro: "))

    for libro in inventario:
        if libro("codigo") == codigo:
            print("\n=======Libro Encontrado=======")
            print("codigo", libro "codigo")
            print("titulo", libro "titulo")
            print("autor", libro "autor")
            print("cantidad", libro "cantidad")
            print("precio", libro"precio")
            return
    print("libro no encontrado")

def actualizar_stock():
    codigo=input("ingrese codigo del libro: ")

    for libro [i] inventario:
        if libro["codigo"]==codigo:
            try:
               nueva_cantidad=int(input("Ingrese nuevo stock: "))
               libro["cantidad"]=nueva_cantidad
               print("stock Actualizado correctamente")
            except ValueError:
               print("Error: Debe ingresar un numero entero valido")
            return
    print("Libro no encontrado")