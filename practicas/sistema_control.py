class UsuarioNoEncontradoError(Exception):
    """Excepción personalizada para usuarios no registrados."""
    pass

class ControlAcceso:
    def __init__(self):
        # Diccionario inicial de usuarios autorizados
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        """Valida si la matrícula existe y devuelve el rol."""
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"> [ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
            return rol
        else:
            raise UsuarioNoEncontradoError("> [ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")

    def agregar_usuario(self, nueva_matricula, nuevo_rol):
        """Permite añadir nuevos registros al diccionario."""
        self.usuarios_autorizados[nueva_matricula] = nuevo_rol
        print(f"--- Usuario {nueva_matricula} registrado exitosamente como {nuevo_rol} ---")

def ejecutar_sistema():
    sistema = ControlAcceso()
    print("--- Sistema de Seguridad Laboratorio IA - UX ---")

    while True:
        try:
            print("\n" + "="*40)
            matricula = input("Ingrese su matrícula (o 'salir' para terminar): ").strip()

            if matricula.lower() == 'salir':
                break
            
            if not matricula:
                raise ValueError("Error: El campo de matrícula no puede estar vacío.")

            # Validación de permisos
            rol_actual = sistema.verificar_permisos(matricula)

            # Funcionalidad Extra: Gestión de Administrador
            if rol_actual == "Administrador":
                opcion = input("¿Desea registrar un nuevo usuario? (s/n): ").lower()
                if opcion == 's':
                    m = input("Nueva matrícula: ").strip()
                    r = input("Rol (Estudiante/Investigador/Administrador): ").strip()
                    if m and r:
                        sistema.agregar_usuario(m, r)
                    else:
                        print("Error: Datos del nuevo usuario incompletos.")

        except UsuarioNoEncontradoError as e:
            print(e)
        except ValueError as e:
            print(f"> [ERROR DE ENTRADA] {e}")
        except Exception as e:
            print(f"> [ERROR INESPERADO] {e}")
        finally:
            print("--- Intento de acceso registrado en el log del servidor ---")

if __name__ == "__main__":
    ejecutar_sistema()