# Clase que representa a un estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre       # Nombre del estudiante
        self.notas = []            # Lista de notas del estudiante

    def agregar_nota(self, nota):
        # Agrega una nueva nota a la lista de notas
        self.notas.append(nota)

    def calcular_promedio(self):
        # Calcula el promedio de las notas del estudiante
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def mostrar_info(self):
        # Muestra el nombre, notas y promedio del estudiante
        print(f"\nEstudiante: {self.nombre}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.calcular_promedio():.2f}")

# Lista para almacenar todos los estudiantes registrados
estudiantes = []

# Menú principal del programa
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar estudiante")
    print("2. Ingresar nota a un estudiante")
    print("3. Ver información de estudiantes")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Se registra un nuevo estudiante
        nombre = input("Nombre del estudiante: ")
        estudiante = Estudiante(nombre)
        estudiantes.append(estudiante)
        print(f"Estudiante {nombre} agregado.")

    elif opcion == "2":
        # Se agrega una nota a un estudiante existente
        nombre = input("Nombre del estudiante: ")
        encontrado = False
        for e in estudiantes:
            if e.nombre == nombre:
                nota = float(input("Ingrese la nota: "))
                e.agregar_nota(nota)
                print("Nota agregada.")
                encontrado = True
                break
        if not encontrado:
            print("Estudiante no encontrado.")

    elif opcion == "3":
        # Se muestra la información de todos los estudiantes registrados
        if not estudiantes:
            print("No hay estudiantes registrados.")
        for e in estudiantes:
            e.mostrar_info()

    elif opcion == "4":
        print("Programa finalizado. ¡Gracias por usar el sistema!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")