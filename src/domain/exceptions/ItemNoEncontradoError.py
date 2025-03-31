class ItemNoEncontradoError(Exception):
    def __init__(self, item_id: str):
        self.item_id = item_id
        super().__init__(f"Item {item_id} no encontrado en el repositorio")