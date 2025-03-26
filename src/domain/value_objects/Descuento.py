from decimal import Decimal
from dataclasses import dataclass

@dataclass(frozen=True)
class Descuento:
    def __init__(self, descripcion, valor):
        self.descripcion: str = descripcion
        self.valor: Decimal = valor
    

    def __str__(self):
        return f'Descuento: {self.descripcion} {self.valor}'