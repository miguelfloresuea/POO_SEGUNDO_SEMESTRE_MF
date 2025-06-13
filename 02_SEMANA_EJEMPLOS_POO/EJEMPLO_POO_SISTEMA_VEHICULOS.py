# Clase base que representa un vehículo genérico
class Vehiculo:
    # Constructor: inicializa los atributos marca y modelo (encapsulados)
    def __init__(self, marca, modelo):
        self.__marca = marca      # Atributo privado (encapsulación)
        self.__modelo = modelo    # Atributo privado (encapsulación)

    # Getter para obtener la marca
    def get_marca(self):
        return self.__marca

    # Setter para cambiar la marca
    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    # Getter para obtener el modelo
    def get_modelo(self):
        return self.__modelo

    # Setter para cambiar el modelo
    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    # Metodo para mostrar información del vehículo
    # Este metodo puede ser sobrescrito por las clases hijas (polimorfismo)
    def mostrar_info(self):
        print(f"Vehículo: {self.__marca} {self.__modelo}")


# Clase hija que representa un Auto
# Hereda de Vehiculo (herencia)
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase base
        self.__puertas = puertas         # Atributo propio de Auto (encapsulado)

    # Metodo sobrescrito (polimorfismo)
    def mostrar_info(self):
        print(f"Auto: {self.get_marca()} {self.get_modelo()} - Puertas: {self.__puertas}")


# Clase hija que representa una Moto
# También hereda de Vehiculo (herencia)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  # Llama al constructor de la clase base
        self.__tipo = tipo               # Atributo propio de Moto (encapsulado)

    # Metodo sobrescrito (polimorfismo)
    def mostrar_info(self):
        print(f"Moto: {self.get_marca()} {self.get_modelo()} - Tipo: {self.__tipo}")


# Crear objetos de Auto y Moto
auto1 = Auto("Toyota", "Corolla", 4)
moto1 = Moto("Yamaha", "FZ", "Deportiva")

# Lista de vehículos (polimorfismo en acción)
vehiculos = [auto1, moto1]

# Recorrer la lista y mostrar información de cada vehículo
for v in vehiculos:
    v.mostrar_info()  # Se llama al metodo correspondiente según el tipo del objeto





