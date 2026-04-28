def obtener_saludo(nombre_bot):
    """
    Retorna un saludo formateado
    """
    return f"Hola, soy {nombre_bot} y estoy listo para ayudarte."

def procesar_comando_recordar(argumento):
    """
    Valida y procesa la accion de recordar un dato
    """
    if not comando:
        return "Error: falta el nombre. Uso de !recordar [nombre]"
    retorn f"¡Entendido! Recordaré el nombre: {comando}"

def calcular_uptime(hora_inicio):
    """
    Calcula la diferencias de tiempo entre el inicio 
    y el actual (mostrar actividad del bot)
    """
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    return f"Tiempo de actividad: {segundos] segundos"
    

def mostrar_ayuda():
    
    
def iniciar_agente():



import datetime

def main():
    nombre_bot = "AgenteBot"
    hora_inicio = datetime.datetime.now()
    
    print(obtener_saludo(nombre_bot))
    
    while True:
        comando = input("Ingrese un comando: ")
        
        if comando.startswith("recordar "):
            argumento = comando[len("recordar "):]
            print(procesar_comando_recordar(argumento))
        elif comando == "uptime":
            print(calcular_uptime(hora_inicio))
        elif comando == "ayuda":
            mostrar_ayuda()
        elif comando == "salir":
            print("¡Hasta luego!")
            break
        else:
            print("Comando no reconocido. Escriba 'ayuda' para ver los comandos disponibles.")

if __name__ == "__main__":
    main()