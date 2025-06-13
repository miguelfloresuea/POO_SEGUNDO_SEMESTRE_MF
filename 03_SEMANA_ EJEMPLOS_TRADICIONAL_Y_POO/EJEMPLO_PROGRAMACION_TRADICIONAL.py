# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura para cada día de la semana:")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for dia in dias:
        temp = float(input(f"Temperatura del {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Ejecutar el programa
main()
