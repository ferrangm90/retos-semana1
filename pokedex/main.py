import requests as consulta


def buscar_pokemon(nombre):

    respuesta = consulta.get(
        f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    )

    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None


while True:

    print("\n==============================")
    print("        POKÉDEX")
    print("==============================")
    print("1 - Buscar Pokémon")
    print("2 - Salir")
    print("==============================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Introduce el nombre o número del Pokémon: ")

        pokemon = buscar_pokemon(nombre)

        if pokemon is None:

            print("\nPokémon no encontrado.")
            print("Comprueba el nombre o número introducido.")

        else:

            print("\n==============================")
            print("     INFORMACIÓN DEL POKÉMON")
            print("==============================")

            print(f"Nombre: {pokemon['name'].capitalize()}")
            print(f"ID: {pokemon['id']}")
            print(f"Altura: {pokemon['height'] / 10} m")
            print(f"Peso: {pokemon['weight'] / 10} kg")

            # Tipos
            print("\nTipos:")

            for tipo in pokemon["types"]:
                print(f"- {tipo['type']['name'].capitalize()}")

            # Habilidades
            print("\nHabilidades:")

            for habilidad in pokemon["abilities"]:
                print(f"- {habilidad['ability']['name'].capitalize()}")

            # Estadísticas
            print("\nEstadísticas:")

            for estadistica in pokemon["stats"]:

                nombre_estadistica = estadistica["stat"]["name"]
                valor = estadistica["base_stat"]

                print(f"- {nombre_estadistica.capitalize()}: {valor}")

            # Movimientos
            print("\nPrimeros 10 movimientos:")

            movimientos = pokemon["moves"]

            for movimiento in movimientos[:10]:
                print(f"- {movimiento['move']['name'].capitalize()}")

            print("\n==============================")

    elif opcion == "2":

        print("\nGracias por utilizar la Pokédex.")
        break

    else:

        print("\nOpción incorrecta.")
        print("Seleccione 1 o 2.")