# Programa: Ejemplo de POO en Python
# (Semana 06) Tarea: Clases, objetos, herencia, encapsulamiento y polimorfismo

class Vehiculo:
    # Clase base que representa un vehículo genérico
    def __init__(self, marca, modelo, anio):
        self.marca = marca          # atributo público
        self.modelo = modelo        # atributo público
        self.anio = anio            # atributo público
        self.__kilometraje = 0      # atributo privado (encapsulación)

    def describir(self):
        # Metodo que describe el vehículo
        print(f"Vehículo: {self.marca} {self.modelo} ({self.anio})")

    def conducir(self, kms):
        # Metodo para aumentar el kilometraje
        if kms > 0:
            self.__kilometraje += kms
            print(f"Has conducido {kms} km. Kilometraje actual: {self.__kilometraje} km")
        else:
            print("La distancia debe ser mayor que cero.")

    def obtener_kilometraje(self):
        # Metodo público para acceder al kilometraje privado
        return self.__kilometraje


class Automovil(Vehiculo):
    # Clase derivada que representa un automóvil
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)  # herencia
        self.puertas = puertas                 # nuevo atributo específico de Automovil

    def describir(self):
        # Metodo sobrescrito para describir el automóvil
        print(f"Automóvil: {self.marca} {self.modelo} ({self.anio}) con {self.puertas} puertas\n") #\n agrega salto de lineaa


# Instancia de Vehiculo
vehiculo_generico = Vehiculo("Toyota", "Corolla", 2015)
vehiculo_generico.describir()
vehiculo_generico.conducir(150)
print(f"Kilometraje del vehículo genérico: {vehiculo_generico.obtener_kilometraje()} km\n")



# Instancia de Automovil
mi_auto = Automovil("Honda", "Civic", 2020, 4)
mi_auto.describir()  # Aquí se usa el metodo sobrescrito
mi_auto.conducir(200)
print(f"Kilometraje de mi automóvil: {mi_auto.obtener_kilometraje()} km")
