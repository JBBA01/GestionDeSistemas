import subprocess

def ejecutar(comando):
    subprocess.run(comando, shell=True)

def crear_archivo(nombre):
    subprocess.run(["touch", nombre])

def crear_carpeta(nombre):
    subprocess.run(["mkdir", nombre])

def mover_archivo(origen, destino):
    subprocess.run(["mv", origen, destino])

def listar_carpetas():
    subprocess.run(["ls", "-d", "*/"])

def ejecutar_programa(Calculadora):
    subprocess.run(Calculadora, shell=True)

def menu():
    print("Elija una opción:")
    print("1. Crear archivo promedio.txt")
    print("2. Crear carpeta 'calificaciones'")
    print("3. Crear carpeta 'primer parcial' y mover archivo 'promedio.txt'")
    print("4. Crear archivo comandos.py en carpeta 'calificaciones'")
    print("5. Listar todas las carpetas")
    print("6. Ejecutar programa calculadora")
    print("x. Salida")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        crear_archivo("promedio.txt")
        print("Archivo 'promedio.txt' creado.")
    elif opcion == "2":
        crear_carpeta("calificaciones")
        print("Carpeta 'calificaciones' creada.")
    elif opcion == "3":
        crear_carpeta("primer_parcial")
        mover_archivo("promedio.txt", "primer_parcial")
        print("Archivo 'promedio.txt' movido a la carpeta 'primer parcial'.")
    elif opcion == "4":
        subprocess.run(["touch", "calificaciones/comandos.py"])
        print("Archivo 'comandos.py' creado en la carpeta 'calificaciones'.")
    elif opcion == "5":
        listar_carpetas()
    elif opcion == "6":
        import Menu
    elif opcion == "x":
        print("Adiós")
    else:
        print("Elige una opción válida.")
        menu()

menu()
