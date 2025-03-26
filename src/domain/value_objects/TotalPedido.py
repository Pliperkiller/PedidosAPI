from decimal import Decimal
from dataclasses import dataclass

@dataclass(frozen=True)
class TotalPedido:
    valor: Decimal

    def __str__(self):
        return f'Total Pedido: {self.valor}'