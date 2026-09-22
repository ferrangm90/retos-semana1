class Usuario:
    def __init__(self, username, password, rol):
        self.username = username
        self.password = password
        self.rol = rol

    def menu(self):
        pass


class Admin(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def menu(self, sistema):
        while True:
            print("\n--- Menú Administrador ---")
            print("1. Ver usuarios")
            print("2. Eliminar usuario")
            print("3. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                sistema.mostrar_usuarios()

            elif opcion == "2":
                username = input("Ingrese el usuario a eliminar: ")
                sistema.eliminar_usuario(username)

            elif opcion == "3":
                print("Sesión cerrada.")
                break
            else:
                print("Opción inválida.")


class Cliente(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password, "cliente")

    def menu(self, sistema=None):
        while True:
            print("\n--- Menú Cliente ---")
            print("1. Ver productos (simulado)")
            print("2. Realizar compra (simulado)")
            print("3. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("Mostrando productos...")

            elif opcion == "2":
                print("Procesando compra...")

            elif opcion == "3":
                print("Sesión cerrada.")
                break
            else:
                print("Opción inválida.")


# Sistema de Autenticación
class SistemaAutenticacion:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self):
        username = input("Nombre de usuario: ")

        if username in self.usuarios:
            print("Error: el usuario ya existe.")
            return

        password = input("Contraseña: ")
        rol = input("Rol (admin/cliente): ").lower()

        if rol == "admin":
            self.usuarios[username] = Admin(username, password)
        elif rol == "cliente":
            self.usuarios[username] = Cliente(username, password)
        else:
            print("Rol inválido.")
            return

        print("Usuario registrado correctamente.")

    def iniciar_sesion(self):
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        usuario = self.usuarios.get(username)

        if not usuario:
            print("Error: el usuario no existe.")
            return

        if usuario.password != password:
            print("Error: contraseña incorrecta.")
            return

        print(f"Bienvenido, {usuario.username} ({usuario.rol})")
        usuario.menu(self)

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return

        print("\nUsuarios registrados:")
        for username, usuario in self.usuarios.items():
            print(f"- {username} ({usuario.rol})")

    def eliminar_usuario(self, username):
        if username in self.usuarios:
            del self.usuarios[username]
            print("Usuario eliminado.")
        else:
            print("El usuario no existe.")

    def menu_principal(self):
        while True:
            print("\n---- Sistema de Autenticación ----")
            print("1. Registrar nuevo usuario")
            print("2. Iniciar sesión")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.iniciar_sesion()
            elif opcion == "3":
                print("Saliendo del sistema.")
                break
            else:
                print("Opción inválida.")


sistema = SistemaAutenticacion()
sistema.menu_principal()