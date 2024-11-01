class Persona:
    def __init__(self, nombre, apellido, telefono, direccion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__direccion = direccion

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_telefono(self):
        return self.__telefono
    
    def get_direccion(self):
        return self.__direccion

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido  

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def __str__(self):
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, Teléfono: {self.__telefono}, Dirección: {self.__direccion}"
    
def main():
    persona1 = Persona("Juan", "Pérez", "1234567890", "Calle los dolores 123")
    print(persona1.__str__())

if __name__ == "__main__":
    main()

