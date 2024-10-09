from abc import ABC, abstractmethod
from datetime import datetime


class Products:
    def __init__(self, codigo: str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


class Client:
    def __init__(self, name: str, address: str, dni: str, telephone: str):
        self.name = name
        self.address = address
        self.dni = dni
        self.telephone = telephone


class Invoice:  # Changed to PascalCase
    def __init__(self, client: Client, num_invoice: str, date: str = None):
        self.client = client
        self.num_invoice = num_invoice
        self.date = date if date else datetime.now().strftime("%d/%m/%Y")
        self.total = 0.0
        self.products = []

    def add_products(self, product: Products, cant: int):
        subtotal = product.precio * cant
        self.products.append({
            'producto': product,
            'cantidad': cant,
            'subtotal': subtotal
        })
        self.total += subtotal

    def mostrar_factura(self):
        print(f"CLIENTE: {self.client.name} \n")
        print(f"DIRECCION: {self.client.address} \n")
        print("=" * 50)
        for item in self.products:
            print(
                f"{item['producto'].nombre} - Cantidad: {item['cantidad']} - Precio: {item['producto'].precio} - Subtotal: {item['subtotal']}")
        print(f"Total a pagar: {self.total}")


class Ifacturador(ABC):
    @abstractmethod
    def facturar(self, factura: Invoice):
        pass


class FacturaporConsola(Ifacturador):
    def facturar(self, factura: Invoice):
        factura.mostrar_factura()


class FacturaporCorreo(Ifacturador):
    def facturar(self, factura: Invoice):
        # Aquí simularías el envío por correo electrónico
        print(f"Enviando factura por correo a: {factura.client.telephone}")
        factura.mostrar_factura()
        # En un caso real, usarías una biblioteca de envío de correos para enviar la factura


class FacturadorDB(Ifacturador):
    def facturar(self, factura: Invoice):
        # Aquí implementarías la lógica para guardar la factura en la base de datos
        print(f"Guardando la factura en la base de datos para el cliente: {factura.client.name}")
        # Aquí iría el código para insertar la factura en la base de datos


class FacturadorFactory:
    @staticmethod
    def get_facturador(tipo: str) -> Ifacturador:
        if tipo == "consola":
            return FacturaporConsola()
        elif tipo == "correo":
            return FacturaporCorreo()
        elif tipo == "db":
            return FacturadorDB()
        else:
            raise ValueError("Tipo de facturador no válido.")



# Sample data
producto1 = Products("001", "Laptop", 1000.00)
producto2 = Products("002", "Teclado", 15.00)
producto3 = Products("003", "Mause", 5.00)  # Corrected typo

cliente1 = Client("Jose Manuel Figuera", "Calle si numero, oeste", "00522222", "69464646")

factura = Invoice(cliente1, "INV-001")  # Added invoice number

factura.add_products(producto1, 1)
factura.add_products(producto2, 2)


tipo_factura = "db"
facturador = FacturadorFactory.get_facturador(tipo_factura)
#facturador = FacturaporConsola()
facturador.facturar(factura)  # Added this line to show the invoice


