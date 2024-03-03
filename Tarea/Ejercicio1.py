#1.Una tienda de autopartes necesita un programa para catalogar sus productos,crear la clase catalogo
# y producto, realizar un objeto dentro de un catalgo de productos el cual debe tener un metodo para agregar
# productos el cual debe tener un metodo para agregar productos y otra para mostrar toda la lista de productos.

class Producto:
    codigo: None
    nombre: None
    precio: None

    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}"

    def __repr__(self):
        return f"Producto({self.codigo}, {self.nombre}, {self.precio})"
  

class Catalgo:
    productos: None

    def __init__(self):
        self.productos = []
    
    def agregar_productos(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
            print(f"Producto '{producto.nombre}' agregado al catálogo")
        else: 
            print("Error, se espera un objeto de la clase Productos")
    
    def mostrar_productos(self):
        if self.productos:
            print("Lista de Productos")
            for producto in self.productos:
                print(producto)
        else:
            print("El catálogo está vacío")

catalogo = Catalgo()

producto1 = Producto("001", "Batería de Auto", 89.99)
producto2 = Producto("002", "Batería de Moto", 79.99)

catalogo.agregar_productos(producto1)
catalogo.agregar_productos(producto2)

catalogo.mostrar_productos()