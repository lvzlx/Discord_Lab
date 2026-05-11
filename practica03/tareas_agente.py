#definicion de tareas v1
import datetime

def agregar_tareas(lista_tareas,descripcion):
    """
    Agregar una tarea a la lista si cumple con los requisitos 
    """

    if len(descripcion) < 3:
        return"Error: Longitud no valida"
    
    # Crear formato para tarea 

    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion} - {fecha}"
    lista_tareas.append(nueva_tarea)
    return f"Tarea agregada con exito"
        
