"""
EJEMPLO: Programa utilizando constructores, destructores y buenas prácticas de POO
"""

# Creación de la clase Auto
class Auto:
    def __init__(self, marca, modelo, año):  # Constructor
        # Inicializar atributos
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False  # Motor comienza apagado
        print(f"Auto {marca} {modelo} ({año}) creado.")

    def __del__(self):  # Destructor
        # Se ejecuta automáticamente cuando el objeto se destruye
        # Si el auto está encendido, lo apaga antes de destruirse
        if self.encendido:
            self.apagar()
        print(f"Auto {self.marca} {self.modelo} destruido.")

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"Auto {self.marca} {self.modelo} encendido.")
        else:
            print(f"¡El auto {self.marca} {self.modelo} ya está encendido!")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"Auto {self.marca} {self.modelo} apagado.")
        else:
            print(f"¡El auto {self.marca} {self.modelo} ya está apagado!")

    def mostrar_info(self):
        estado = "ENCENDIDO" si self.encendido else "APAGADO"
        return (f"\nInformación del auto:\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Año: {self.año}\n"
                f"Estado: {estado}\n")


# Ejemplo de uso principal
if __name__ == "__main__":
    # Crear un auto nuevo
    mi_auto = Auto("Chevrolet", "DMAX", 2025)

    # Operaciones con el auto
    mi_auto.encender()
    print(mi_auto.mostrar_info())

    mi_auto.apagar()
    print(mi_auto.mostrar_info())

    # Al finalizar el programa, el destructor __del__ se llamará automáticamente
    # cuando el objeto mi_auto quede sin referencias.
    # NO es necesario llamar explícitamente: del mi_auto

    # Si deseas forzar que se destruya antes, podrías hacerlo así:
    # del mi_auto

    print("Programa terminado.")

"""
Explicación:
1. El constructor (__init__) inicializa el objeto.
2. El destructor (__del__) limpia recursos al destruirse el objeto.
3. Los métodos encender/apagar gestionan el estado del auto.
4. mostrar_info() devuelve una descripción del auto.
5. El bloque if __name__ permite que el ejemplo solo se ejecute si se corre directamente el archivo.
"""
