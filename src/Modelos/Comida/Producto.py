class Producto:
    def __init__(self, nombre, descripcion, precio):
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion
        self.ingredientes = list() #Lista de ingredientes que conforman el producto

    def eliminar_ingrediente_de_prodcuro(self, indice_ingrediente):
        self.ingredientes.pop(indice_ingrediente)

    def agregar_ingrediente_a_producto(self, ingrediente, cantidad):
        self.ingredientes.append([ingrediente, cantidad])

    def modificar_cantidad_ingrediente_de_producto(self, indice_ingrediente, cantidad):
        self.ingredientes[indice_ingrediente][1] = cantidad #Modifica la cantidad del ingrediente utilizado en la preparacion del producto