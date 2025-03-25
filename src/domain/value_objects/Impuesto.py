import decimal
from enum import Enum

class TipoImpuesto(Enum):
    porcentual = 1
    fijo = 2


class Impuesto:
    def __init__(self, nombre: str,valor: decimal, tipo_impuesto: TipoImpuesto):
        self.nombre = nombre
        self.valor = valor
        self.tipo_impuesto = tipo_impuesto

    def __str__(self):
        return f'Impuesto: {self.nombre} {self.valor}'