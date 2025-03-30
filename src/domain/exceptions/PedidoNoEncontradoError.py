class PedidoNoEncontradoError(Exception):
    """Excepción lanzada cuando un pedido no existe en el sistema"""
    
    def __init__(self, pedido_id: str = None, message: str = None):
        """
        Args:
            pedido_id: ID del pedido que no fue encontrado (opcional)
            message: Mensaje personalizado (opcional)
        """
        self.pedido_id = pedido_id
        self.message = message or "El pedido solicitado no fue encontrado"
        
        if self.pedido_id:
            self.message += f" - ID: {self.pedido_id}"
            
        super().__init__(self.message)