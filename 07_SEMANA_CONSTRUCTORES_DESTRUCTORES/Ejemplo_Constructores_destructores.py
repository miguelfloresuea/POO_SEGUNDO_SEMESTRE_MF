
"""
EJEMPLO, PROGRAMA UTILIZANDO CONSTRUCTORES, DESTRUCTORES Y USO DE BUENAS PRACTICAS DE POO
"""

#Creacion de la clase Auto
class Auto:
    def __init__(self, marca, modelo, año):  #Constructor de la clase Auto

        # Atributos inicializados:
        self.marca = marca  # - marca, modelo, año: características del auto
        self.modelo = modelo
        self.año = año
        self.encendido = False  # encendido: estado del motor (True/False), Motor comienza apagado
        print(f"Auto {marca} {modelo} ({año}) creado.")  # Mensaje de creación

    def __del__(self):  #Destructor de la clase Auto
        #Se ejecuta automáticamente cuando el objeto es eliminado.

        # Funcionamiento:
        # 1. Verifica si el auto está encendido
        # 2. Si está encendido, lo apaga
        # 3. Muestra mensaje de destrucción
        if self.encendido:
            self.apagar()  # Asegura que el auto se apague antes de destruirse
        print(f"Auto {self.marca} {self.modelo} destruido.")

    def encender(self): #Metodo para encender el auto

        # Comportamiento:
        # - Si el auto está apagado, lo enciende
        # - Si ya está encendido, muestra mensaje
        if not self.encendido:
            self.encendido = True
            print(f"Auto {self.marca} {self.modelo} encendido.")
        else:
            print(f"¡El auto {self.marca} {self.modelo} ya está encendido!")

    def apagar(self):   #Metodo para apagar el auto

        # Comportamiento:
        # - Si el auto está encendido, lo apaga
        # - Si ya está apagado, muestra mensaje
        if self.encendido:
            self.encendido = False
            print(f"Auto {self.marca} {self.modelo} apagado.")
        else:
            print(f"¡El auto {self.marca} {self.modelo} ya está apagado!")

    def mostrar_info(self): #Muestra información detallada del auto

        # Retorna:
        # Cadena  con marca, modelo, año y estado
        estado = "ENCENDIDO" if self.encendido else "APAGADO"
        return (f"\nInformación del auto:\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Año: {self.año}\n"
                f"Estado: {estado}\n")


# Ejemplo de uso principal
if __name__ == "__main__":
    # Creación de un auto nuevo
    mi_auto = Auto("Chevrolet", "DMAX", 2025)

    # Operaciones con el auto
    mi_auto.encender()  # Encender el auto
    print(mi_auto.mostrar_info())  # Mostrar información

    mi_auto.apagar()  # Apagar el auto
    print(mi_auto.mostrar_info())  # Mostrar información

    # El destructor se llamará automáticamente al eliminar el objeto
    del mi_auto

    # Este mensaje aparecerá después de que el auto sea destruido
    print("Programa terminado.")

"""
Explicación del funcionamiento:
1. El constructor (__init__) establece los valores iniciales del auto
2. El destructor (__del__) se asegura de limpiar recursos antes de eliminar el objeto
3. Los métodos encender/apagar controlan el estado del motor
4. mostrar_info() proporciona una vista detallada del estado actual
5. El bloque if __name__ , permite ejecutar el ejemplo solo cuando se ejecuta este archivo directamente
"""