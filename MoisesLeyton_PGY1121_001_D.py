from os import system
system("cls")

ubicaciones = [["" for _ in range(10)] for _ in range(10)]
asistentes = {}

def comprar_entradas():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))
    if cantidad < 1 or cantidad > 3:
        print("Cantidad de entradas inválida. Intente nuevamente.")
        return
    
    print("----- Asientos Disponibles -----")
    mostrar_asientos()
    
    for _ in range(cantidad):
        fila = int(input("Ingrese el número de fila: "))
        columna = int(input("Ingrese el número de columna: "))
        
        if fila < 1 or fila > 10 or columna < 1 or columna > 10:
            print("Ubicación inválida. Intente nuevamente.")
            return
        
        if ubicaciones[fila - 1][columna - 1] != "":
            print("Ubicación no disponible. Intente nuevamente.")
            return
        
        ubicaciones[fila - 1][columna - 1] = "X"
    
    run = input("Ingrese el RUN (sin guiones ni dígito verificador) del asistente: ")
    asistentes[run] = cantidad * calcular_precio_entrada(fila - 1, columna - 1)

    print("Operación realizada correctamente.")

def calcular_precio_entrada(fila, columna):
    asiento_num = fila * 10 + columna + 1
    if asiento_num <= 20:
        return 120000
    elif asiento_num <= 50:
        return 80000
    else:
        return 50000

def ubicaciones_disponibles():
    disponibles = 0
    for i in range(10):
        for j in range(10):
            if ubicaciones[i][j] == "":
                disponibles += 1
    
    print(f"Total de ubicaciones disponibles: {disponibles}")

def listado_asistentes():
    print("Listado de asistentes:")
    for run, cantidad in asistentes.items():
        print(f"RUN: {run}, Cantidad de Entradas: {cantidad // 1000}")

def ganancias_totales():
    ganancias = sum(asistentes.values())
    print(f"Ganancias totales: ${ganancias}")

def mostrar_menu():
    print("----- MENÚ -----")
    print("1. Comprar Entradas")
    print("2. Ubicaciones Disponibles")
    print("3. Listado de Asistentes")
    print("4. Ganancias Totales")
    print("5. Salir")

def mostrar_asientos():
    print("----- Asientos -----")
    for i in range(10):
        for j in range(10):
            ubicacion = ubicaciones[i][j]
            if ubicacion == "":
                asiento_num = i * 10 + j + 1
                print(f"{asiento_num:3d}", end=" ")
            else:
                print(" X ", end="")
        print()

opcion = 0

while opcion != 5:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        comprar_entradas()
    elif opcion == 2:
        ubicaciones_disponibles()
    elif opcion == 3:
        listado_asistentes()
    elif opcion == 4:
        ganancias_totales()
    elif opcion == 5:
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Intente nuevamente.")
    
    mostrar_asientos()
