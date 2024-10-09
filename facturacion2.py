from abc import ABC, abstractmethod
from datetime import datetime


class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


class Cliente:
    def __init__(self, nombre: str, direccion: str, dni: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.dni = dni
        self.telefono = telefono


class Factura:
    def __init__(self, cliente: Cliente, numero_factura: str, fecha: str = None):
        self.cliente = cliente
        self.numero_factura = numero_factura
        self.productos = []
        self.total = 0.0
        self.fecha = fecha if fecha else datetime.now().strftime("%d/%m/%Y")

    def agregar_productos(self, producto: Producto, cantidad: int):
        subtotal = producto.precio * cantidad
        self.productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })
        self.total += subtotal

    def mostrar_factura(self):
        # Formato de encabezado
        print(f"FACTURA: {self.numero_factura}")
        print(f"FECHA: {self.fecha}\n")

        # Información del cliente
        print(f"CLIENTE: {self.cliente.nombre}\t\tDNI: {self.cliente.dni}\t\tTELEFONO: {self.cliente.telefono}")
        print("=" * 76)

        # Títulos de la tabla de productos
        print(f"{'PRODUCTO':<20}{'CANTIDAD':<12}{'COSTO':<12}{'SUBTOTAL':<12}")
        print("=" * 76)

        # Detalles de productos
        for item in self.productos:
            prod = item['producto']
            print(f"{prod.nombre:<20}{item['cantidad']:<12}{prod.precio:<12.2f}{item['subtotal']:<12.2f}")

        print("=" * 76)

        # Cálculo de impuestos y total
        iva = self.total * 0.18
        neto = self.total - iva
        print(f"{'NETO:':>50}{neto:>12.2f}")
        print(f"{'IVA 18%:':>50}{iva:>12.2f}")
        print(f"{'TOTAL A PAGAR:':>50}{self.total:>12.2f}")


class IFacturador(ABC):
    @abstractmethod
    def facturar(self, factura: Factura):
        pass


class FacturadorConsola(IFacturador):
    def facturar(self, factura: Factura):
        factura.mostrar_factura()


class ServicioFacturacion:
    def __init__(self, facturador: IFacturador):
        self.facturador = facturador

    def procesar_factura(self, factura: Factura):
        self.facturador.facturar(factura)


# Productos de ejemplo
producto1 = Producto("001", "Laptop", 1000.00)
producto2 = Producto("002", "Teclado", 10.00)
producto3 = Producto("003", "Monitor", 10.00)
producto4 = Producto("004", "Disco Duro", 20.00)
producto5 = Producto("005", "Memoria", 10.00)
producto6 = Producto("006", "Mouse", 10.00)

# Cliente de ejemplo
cliente1 = Cliente("Jose Manuel Figuera", "Calle Si Numero", "005222222", "9954355511")

# Creación de la factura
factura = Factura(cliente1, "0001")

# Agregar productos a la factura
factura.agregar_productos(producto2, 2)
factura.agregar_productos(producto3, 3)
factura.agregar_productos(producto4, 4)
factura.agregar_productos(producto5, 2)
factura.agregar_productos(producto6, 1)

# Procesar y mostrar la factura
facturador = FacturadorConsola()
servicio = ServicioFacturacion(facturador)
servicio.procesar_factura(factura)
