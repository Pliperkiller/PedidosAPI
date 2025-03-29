from dataclasses import dataclass

@dataclass
class DireccionEntregaDTO:
    alias: str
    pais: str
    ciudad: str
    estado: str
    calle: str
    calle2: str
    codigo_postal: str
    coordenadas: str