from dataclasses import dataclass

@dataclass(frozen=True)
class Direccion:
    pais: str
    ciudad: str
    estado: str
    calle: str
    calle2: str = None
    codigo_postal: str = None
    coordenadas: str = None        
