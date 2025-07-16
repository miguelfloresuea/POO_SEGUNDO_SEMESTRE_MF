# Clase que representa a un estudiante
class Estudiante:
    def __init__(self, nombre):
        # Constructor que inicializa el nombre del estudiante y su lista de notas
        self.nombre = nombre       # Nombre del estudiante
        self.notas = []            # Lista vacía donde se almacenarán las notas

    def agregar_nota(self, nota):
        # Metodo que agrega una nueva nota a la lista del estudiante
        self.notas.append(nota)

    def calcular_promedio(self):
        # Metodo que calcula el promedio de las notas del estudiante
        if not self.notas:         # Si no hay notas, retorna 0 para evitar división por cero
            return 0
        return sum(self.notas) / len(self.notas)  # Promedio = suma de notas / cantidad

    def mostrar_info(self):
        # Metodo que muestra el nombre, las notas y el promedio del estudiante
        print(f"\nEstudiante: {self.nombre}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.calcular_promedio():.2f}")  # Promedio con 2 decimales

# Lista para almacenar todos los estudiantes registrados
estudiantes = []

# Bucle del menú principal del programa
while True:
    # Mostrar las opciones del menú
    print("\n--- MENÚ ---")
    print("1. Agregar estudiante")
    print("2. Ingresar nota a un estudiante")
    print("3. Ver información de estudiantes")
    print("4. Salir")

    opcion = input("Elige una opción: ")  # Leer la opción del usuario

    if opcion == "1":
        # Opción para registrar un nuevo estudiante
        nombre = input("Nombre del estudiante: ")
        estudiante = Estudiante(nombre)   # Crear una nueva instancia de Estudiante
        estudiantes.append(estudiante)    # Agregarlo a la lista
        print(f"Estudiante {nombre} agregado.")

    elif opcion == "2":
        # Opción para agregar una nota a un estudiante existente
        nombre = input("Nombre del estudiante: ")
        encontrado = False  # Variable para verificar si se encontró al estudiante

        for e in estudiantes:
            if e.nombre == nombre:  # Buscar por nombre
                nota = float(input("Ingrese la nota: "))
                e.agregar_nota(nota)  # Agregar la nota al estudiante
                print("Nota agregada.")
                encontrado = True
                break  # Salir del ciclo si se encontró

        if not encontrado:
            print("Estudiante no encontrado.")  # Si no se encontró el nombre

    elif opcion == "3":
        # Opción para mostrar la información de todos los estudiantes
        if not estudiantes:
            print("No hay estudiantes registrados.")
        for e in estudiantes:
            e.mostrar_info()  # Llamar al metodo que imprime info del estudiante

    elif opcion == "4":
        # Opción para salir del programa
        print("Programa finalizado. ¡Gracias por usar el sistema!")
        break  # Rompe el bucle infinito y finaliza

    else:
        # Si se ingresa una opción no válida
        print("Opción inválida. Intenta de nuevo."

