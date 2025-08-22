import os
import subprocess


# Función para leer y mostrar el contenido de un script .py
def mostrar_codigo(ruta_script):
    # Obtiene la ruta absoluta del script
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Abre y lee el archivo
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


# Función para ejecutar el script .py en una consola nueva
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Si el sistema es Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Si es Linux o Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


# Menú principal que muestra las carpetas de cada semana
def mostrar_menu():
    # Obtiene la ruta del directorio actual (donde está el dashboard.py)
    ruta_base = os.path.dirname(__file__)

    # Lista con las carpetas principales del proyecto
    carpetas_principales = [
        '02_SEMANA_EJEMPLOS_POO',
        '03_SEMANA_ EJEMPLOS_TRADICIONAL_Y_POO',
        '04_SEMANA_EjemplosMundoReal_POO',
        '05_SEMANA_TIPOS_DE_DATOS_IDENTIFICADORES',
        '06_SEMANA_DEBER_CLASES_OBJETOS_HERENCIA_ENCAPSULAMIENTO_POLIMORFISMO',
        '07_SEMANA_CONSTRUCTORES_DESTRUCTORES'
        '08_SEMANA_DASHBOARD'
        '09_SEMANA_GESTION_INVENTARIO_POO'
        '10_SEMANA_GESTION_INVENTARIO_MEJORADO'
    ]

    while True:
        print("\n Menú Principal - Proyecto POO")
        # Muestra el listado de carpetas con su índice
        for idx, carpeta in enumerate(carpetas_principales, start=1):
            print(f"{idx} - {carpeta}")
        print("0 - Salir")

        eleccion = input("Elige una carpeta o '0' para salir: ")
        if eleccion == '0':
            print("¡Hasta luego!")
            break
        else:
            try:
                idx = int(eleccion) - 1
                # Comprueba que la opción sea válida
                if 0 <= idx < len(carpetas_principales):
                    # Construye la ruta completa a la carpeta elegida
                    ruta_carpeta = os.path.join(ruta_base, carpetas_principales[idx])
                    # Llama a la función para mostrar los scripts de esa carpeta
                    mostrar_scripts(ruta_carpeta)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")


# Función que muestra los scripts .py dentro de una carpeta
def mostrar_scripts(ruta_carpeta):
    # Obtiene una lista de archivos .py en la carpeta
    scripts = [f.name for f in os.scandir(ruta_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\n Scripts en: {ruta_carpeta}")
        # Muestra los scripts encontrados
        for idx, script in enumerate(scripts, start=1):
            print(f"{idx} - {script}")
        print("0 - Regresar al menú principal")

        eleccion = input("Elige un script para ver/ejecutar o '0' para regresar: ")
        if eleccion == '0':
            break
        else:
            try:
                idx = int(eleccion) - 1
                if 0 <= idx < len(scripts):
                    # Construye la ruta completa al script elegido
                    ruta_script = os.path.join(ruta_carpeta, scripts[idx])
                    # Muestra el contenido del script
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        # Pregunta si el usuario quiere ejecutar el script
                        ejecutar = input("¿Deseas ejecutarlo? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        else:
                            print("No se ejecutó el script.")
                        input("Presiona Enter para continuar...")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")


# Punto de entrada principal del programa
if __name__ == "__main__":
    mostrar_menu()
