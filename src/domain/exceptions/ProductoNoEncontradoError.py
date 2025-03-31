class ProductoNoEncontradoError(Exception):
    """Excepción lanzada cuando un producto no existe en el sistema"""
    
    def __init__(self, producto_id: str, message: str = None):
        """
        Args:
            producto_id: ID del producto no encontrado
            message: Mensaje personalizado (opcional)
        """
        self.producto_id = producto_id
        self.message = message or f"Producto con ID {producto_id} no encontrado"
        self.error_code = "PRODUCTO_NOT_FOUND"
        
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (Código: {self.error_code})"

    def to_dict(self):
        """Representación del error para respuestas API"""
        return {
            "error": self.message,
            "producto_id": self.producto_id,
            "code": self.error_code
        }