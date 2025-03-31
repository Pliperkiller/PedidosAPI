class PedidoInvalidoError(Exception):
    """Excepción lanzada cuando se detecta un pedido inválido según las reglas de negocio."""
    
    def __init__(self, message: str = "Pedido inválido", 
                 pedido_id: str = None,
                 detalles: dict = None):
        """
        Args:
            message (str): Mensaje descriptivo del error
            pedido_id (str): ID del pedido relacionado (opcional)
            detalles (dict): Información adicional del error (opcional)
        """
        self.message = message
        self.pedido_id = pedido_id
        self.detalles = detalles or {}
        
        if self.pedido_id:
            self.message += f" - ID: {self.pedido_id}"
            
        if self.detalles:
            self.message += f" | Detalles: {self.detalles}"
            
        super().__init__(self.message)

    def __str__(self):
        return self.message