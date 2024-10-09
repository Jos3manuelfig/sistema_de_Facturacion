from abc import ABC, abstractmethod


class Producto:
    def __init__(self, codigo:str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


class Cliente:
    def __init__(self, nombre:str, direccion:str):
        self.nombre = nombre
        self.direccion = direccion


class Factura:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.productos = []
        self.total = 0.0



    def agregar_productos(self, producto: Producto, cantidad:int):
        subtotal = producto.precio * cantidad
        self.productos.append({
            'producto':producto,
            'cantidad':cantidad,
            'subtotal': subtotal

        })
        self.total+= subtotal

    def mostrar_factura(self):
        print(f"Cliente:  {self.cliente.nombre}")
        print(f"Direccion:{self.cliente.direccion} ")
        print("..................................... Productos ....................................................")
        for item in self.productos:
            prod = item["producto"]
            print(f"{prod.nombre}-Cantidad: {item['cantidad']}- Precio: {prod.precio} - Subtotal: {item['subtotal']}")
        print(f"Total a pagar: {self.total}")

class IFacturador(ABC):
    @abstractmethod
    def facturar(self, factura:Factura):
        pass

class FacturadorConsola(IFacturador):
    def facturar(self, factura:Factura):
        factura.mostrar_factura()

class ServicioFacturacion:
    def __init__(self, facturador: IFacturador):
        self.facturador = facturador

    def procesar_factura(self, factura:Factura):
         self.facturador.facturar(factura)


producto1 = Producto("001", "Laptop", 1000.00)
producto2 = Producto("002", "Teclado", 15.00)
prodcuto3 = Producto("003", "Mause", 5.00)
producto4 = Producto("004", "case", 30.00)
producto5 = Producto("005", "memoria", 12.00)
prodcuto6 = Producto("006", "disco duro", 50.00)


cliente1 = Cliente("Juan Perez", "Calle si numero, oeste")


factura = Factura(cliente1)

factura.agregar_productos(producto1,1)
factura.agregar_productos(producto2,2)
 #factura.agregar_productos(producto3,3)
factura.agregar_productos(producto4,4)
factura.agregar_productos(producto5,2)
#factura.agregar_productos(producto6,1)

facturador = FacturadorConsola()
facturador.facturar(factura)

# servicio  = ServicioFacturacion(facturador)
# servicio.procesar_factura(factura)