from datetime import datetime
import uuid

class Cliente:
    def __init__(self,
                nombre: str,
                correo: str, 
                telefono: str, 
                fecha_registro: datetime, 
                fecha_nacimiento: datetime = None
                ):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.fecha_registro = fecha_registro
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f'Cliente: {self.id} {self.nombre} {self.correo} {self.telefono} {self.fecha_registro} {self.fecha_nacimiento}'