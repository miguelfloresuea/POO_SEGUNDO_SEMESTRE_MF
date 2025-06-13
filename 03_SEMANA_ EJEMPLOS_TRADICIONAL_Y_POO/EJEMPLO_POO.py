# Clase que representa el clima diario
class ClimaDiario:
    def __init__(self, dia, temperatura):
        self.dia = dia                # Encapsulamiento de atributos
        self.__temperatura = temperatura  # Atributo privado

    def obtener_temperatura(self):
        return self.__temperatura

    def __str__(self):
        return f"{self.dia}: {self.__temperatura}°C"

# Clase que representa la semana de clima
class SemanaClimatica:
    def __init__(self):
        self.dias_clima = []

    # Método para agregar datos diarios
    def agregar_dia(self, dia, temperatura):
        clima = ClimaDiario(dia, temperatura)
        self.dias_clima.append(clima)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        total = sum(dia.obtener_temperatura() for dia in self.dias_clima)
        return total / len(self.dias_clima)

    # Método para mostrar todos los datos
    def mostrar_datos(self):
        for dia in self.dias_clima:
            print(dia)

# Función principal
def main():
    semana = SemanaClimatica()
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("Ingrese la temperatura para cada día de la semana:")
    for dia in dias:
        temp = float(input(f"Temperatura del {dia}: "))
        semana.agregar_dia(dia, temp)

    print("\nTemperaturas ingresadas:")
    semana.mostrar_datos()

    promedio = semana.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Ejecutar el programa
main()
