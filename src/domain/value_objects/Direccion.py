from dataclasses import dataclass

@dataclass(frozen=True)
class Direccion:
    alias: str
    pais: str
    ciudad: str
    estado: str
    calle: str
    calle2: str = None
    codigo_postal: str = None
    coordenadas: str = None
    

    def __str__(self):
        return f'Direccion: {self.alias} {self.pais} {self.ciudad} {self.estado} {self.calle} {self.calle2} {self.codigo_postal} {self.coordenadas}'
        
