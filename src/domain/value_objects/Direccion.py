
class Direccion:
    def __init__(self,
                 alias: str,
                 pais: str,
                 ciudad: str,
                 estado: str,
                 calle: str,
                 calle2: str = None,
                 codigo_postal: str = None,
                 coordenadas: str = None
                 ):
        
        self.alias = alias
        self.pais = pais
        self.ciudad = ciudad
        self.estado = estado
        self.calle = calle
        self.calle2 = calle2
        self.codigo_postal = codigo_postal
        self.coordenadas = coordenadas

    

    def __str__(self):
        return f'Direccion: {self.alias} {self.pais} {self.ciudad} {self.estado} {self.calle} {self.calle2} {self.codigo_postal} {self.coordenadas}'
        
