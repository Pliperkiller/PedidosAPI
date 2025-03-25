from datetime import datetime

class Cliente:
    def __init__(self,
                id: int,nombre: str,
                correo: str, 
                telefono: str, 
                fecha_registro: datetime, 
                fecha_nacimiento: datetime = None
                ):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.fecha_registro = fecha_registro
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f'Cliente: {self.id} {self.nombre} {self.correo} {self.telefono} {self.fecha_registro} {self.fecha_nacimiento}'