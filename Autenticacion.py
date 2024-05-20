# Definir una clase abstracta para la autenticación de usuarios
from abc import ABC, abstractmethod
class Autenticacion(ABC):
    @abstractmethod
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
    
    def autenticar_usuario(self):
        return f'Usuario: {self.usuario}, Contraseña: {self.contraseña}'

import smtplib
from email.mime.text import MIMEText

# Implementar la clase Autenticacion

class ImplementacionAutenticacion(Autenticacion):
    def __init__(self, usuario, contraseña):
        super().__init__(usuario, contraseña)
        self.intentos_fallidos = 0
    
    def autenticar_usuario(self, usuario, contraseña):
        if self.usuario == usuario and self.contraseña == contraseña:
            return f'Usuario autenticado: {self.usuario}'
        else:
            raise ValueError("Credenciales incorrectas")
    
    def autenticacion_usuario(self, usuario, contraseña):  
        if self.usuario == usuario and self.contraseña == contraseña:
            return f'Usuario autenticado: {self.usuario}'
        else:
            self.intentos_fallidos += 1
            if self.intentos_fallidos >= 3:
                self.enviar_correo(usuario)
                raise ValueError("Credenciales incorrectas. Se ha enviado un correo electrónico para restablecer la contraseña.")
            else:
                raise ValueError("Credenciales incorrectas. Inténtalo de nuevo.")
            
    def enviar_correo(self, usuario):
        smtp_server = "smtp.example.com"
        smtp_port = 587
        sender_email = "tu_correo@example.com"
        sender_password = "tu_contraseña"
        receiver_email = "correo_del_usuario@example.com"

        subject = "Restablecimiento de contraseña"
        body = f"Hola {usuario},\n\nTu cuenta ha sido bloqueada debido a intentos fallidos de inicio de sesión. Por favor, restablece tu contraseña."

        message = MIMEText(body, "plain")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

try:
    autenticacion = ImplementacionAutenticacion("nombre_de_usuario", "contraseña_incorrecta")
    autenticacion.autenticar_usuario("nombre_de_usuario", "contraseña_correcta")
except ValueError as e:
    print(f"Error: {e}")

# Definir una clase abstracta para la gestión de productos
class GestionProductos(ABC):
    @abstractmethod
    def __init__(self, productos, precio, codigo):
        self.productos = productos
        self.precio = precio
        self.codigo = codigo

    def listar_productos(self):
       return f'Producto: {self.productos}, Precio: {self.precio}, Codigo: {self.codigo}'

# Implementar la clase GestionProductos
class ImplementacionGestionProductos(GestionProductos):
    def __init__(self, productos, precio, codigo):
        super().__init__(productos, precio, codigo)

    def listar_productos(self):
        return f'Producto: {self.productos}, Precio: {self.precio}, Codigo: {self.codigo}'

# Definir una clase abstracta para la gestión del carrito de compras
class GestionCarritoCompras(ABC):
    @abstractmethod
    def __init__(self, id_item, id_carrito):
        self.id__item = id_item
        self.id_carrito = id_carrito
    
    def agregar_item_carrito(self):
        self.carrito = []

# Implementar la clase GestionCarritoCompras
class ImplementacionGestionCarritoCompras(GestionCarritoCompras):
    def __init__(self, id_item, id_carrito):
       super().__init__(id_item, id_carrito)
    
    def agregar_item_carrito(self, item):
        self.carrito.append(item)
        return f'Item agregado al carrito: {item}'

    def listar_carrito(self):
        if not self.carrito:
            return "El carrito está vacío."
        else:
            return f'Contenido del carrito: {", ".join(self.carrito)}'
        
carrito_compras = ImplementacionGestionCarritoCompras()
item1 = "Producto A"
item2 = "Producto B"
print(carrito_compras.agregar_item_carrito(item1))
print(carrito_compras.agregar_item_carrito(item2))
print(carrito_compras.listar_carrito())
    
    # Uso de las clases e interfaces definidas
autenticacion = ImplementacionAutenticacion()
autenticacion.autenticar_usuario("nombre_de_usuario", "contraseña")

gestion_productos = ImplementacionGestionProductos()
gestion_productos.listar_productos("Producto", "Precio", "Codigo")

gestion_carrito_compras = ImplementacionGestionCarritoCompras()
gestion_carrito_compras.agregar_item_carrito[]