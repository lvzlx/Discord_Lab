def procesar_sensores():
    print("--- MÓDULO DE SENSORES (VECTORES) ---")
    sensores_distancia = []
    
    for i in range(5):
        distancia = float(input(f"Ingrese distancia sensor {i + 1}: "))
        sensores_distancia.append(distancia)
    
    # Cálculo del promedio de proximidad
    promedio = sum(sensores_distancia) / len(sensores_distancia)
    
    estado = "Seguro"
    if promedio < 2.0:
        estado = "Peligro"
        print(f"Promedio de proximidad: {promedio:.2f}m. Aviso: Reduciendo velocidad global.")
    else:
        print(f"Promedio de proximidad: {promedio:.2f}m. Estado: {estado}.")
    
    return promedio

def procesar_vision():
    
    print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")
    print("Llenando matriz de cámara 3x3:")
    
    camara_ia = []
    
    # Lectura y validación (Saturación)
    for fila in range(3):
        nueva_fila = []
        for col in range(3):
            brillo = int(input(f"Fila {fila}, Col {col} (Brillo 0-255): "))
            
            # Lógica de saturación: si supera 255, se asigna 255
            if brillo > 255:
                brillo = 255
            elif brillo < 0:
                brillo = 0
                
            nueva_fila.append(brillo)
        camara_ia.append(nueva_fila)

    # Escritura (Visualización en formato tabla)
    print("\nVisualización de la imagen capturada:")
    for fila in camara_ia:
        print(f"[ {'  '.join(map(str, fila))} ]")

    # Análisis de puntos de luz alta
    puntos_brillantes = 0
    for fila in camara_ia:
        for pixel in fila:
            if pixel > 200:
                puntos_brillantes += 1
                
    print(f"\nResultado de Análisis IA:")
    print(f"Se detectaron {puntos_brillantes} píxeles de alta intensidad.")

def main():
    procesar_sensores()
    procesar_vision()

if __name__ == "__main__":
    main()