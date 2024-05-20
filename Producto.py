class Producto():
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.stock = 0  

    def vender_por_menor(self, cantidad):
        if self.stock >= cantidad:
           self.stock -= cantidad
            return f"Se vendieron {cantidad} unidades de {self.nombre} por menor."
        else:
            return f"No hay suficiente stock de {self.nombre} para vender por menor."

    def vender_por_mayor(self, cantidad):
        # Implementar la lógica para vender por mayor
        # aplicar descuentos o condiciones específicas

    def compras_a_proveedores(self, cantidad):
        # Implementar la lógica para registrar compras a proveedores
        # Actualizar el stock según la cantidad recibida

    def envios(self, direccion):
        # Implementar la lógica para gestionar envíos
        # usar la dirección proporcionada como parámetro

    def devoluciones(self, cantidad):
        # Implementar la lógica para procesar devoluciones
        # Actualizar el stock según la cantidad devuelta

    def cambios(self, cantidad):
        # Implementar la lógica para gestionar cambios
        # Actualizar stock según la cantidad cambiada

    def formas_de_pago(self):
        # Implementar la lógica para mostrar las formas de pago disponibles
        # lista de opciones o un mensaje informativo

    def agregar_al_carrito(self, cantidad):
        # Implementar la lógica para agregar productos al carrito
        # usar una lista para almacenar los productos seleccionados


producto1 = Producto("", 20.0, "")
producto1.compras_a_proveedores(100) 
producto1.vender_por_menor(5)  
producto1.envios("Calle Principal, 123")  
# agregar más funcionalidades 