
from datetime import datetime


tareas = []


def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_limite = input("Ingrese la fecha límite (formato YYYY-MM-DD): ")
    tarea = {
        "descripcion": descripcion,
        "fecha_limite": datetime.strptime(fecha_limite, "%Y-%m-%d"),
        "estado": "pendiente",
    }
    tareas.append(tarea)

def listar_tareas():
    for tarea in tareas:
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha límite: {tarea['fecha_limite'].strftime('%Y-%m-%d')}")
        print(f"Estado: {tarea['estado']}")
        print("---")


def completar_tarea():
    if tareas:
        listar_tareas()
        id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
        if id_tarea >= 0 and id_tarea < len(tareas):
            tareas[id_tarea]["estado"] = "completada"
        else:
            print("ID de tarea inválido.")
    else:
        print("No hay tareas pendientes.")

def eliminar_tarea():
    if tareas:
        listar_tareas()
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        if id_tarea >= 0 and id_tarea < len(tareas):
            del tareas[id_tarea]
        else:
            print("ID de tarea inválido.")
    else:
        print("No hay tareas pendientes.")


while True:
    print("**Sistema de gestión de tareas**")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        if tareas:
            listar_tareas()
        else:
            print("No hay tareas pendientes.")
    elif opcion == 3:
        completar_tarea()
    elif opcion == 4:
        eliminar_tarea()
    elif opcion == 5:
        break
    else:
        print("Opción no válida.")

print("¡Hasta luego!")

