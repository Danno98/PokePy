import json
import random
import time
from pathlib import Path

# Diccionario para el arte ASCII de los Pokémon
ARTE_ASCII = {
    "Pikachu": r"""
        @-@          @@@@
          @.@@@@@@@@`-@`
            @        @      @
            @@@   @@@ @    @@@@@
           @@  @    @@@@  @   @@@
           @  @-@     @@ @ @ <  
            @@@@     @@@   > @
           @ @    @ @  @@@@
          @@@    @@@ @@@@<
            @    @     @@
             >   @    @
            @@@@@> @@
                     @@@
        """,
    "Charmander": r"""
                      @@--@@@-@@
                    @@          @@
                  @@          @@  @@
                 @@@          @ @@   @
                @ @@           @ @@   @
                @@@          @@@@@@   @
              @@@             @   @   @
             @              @@@@@@   @
             @@   @                   @
              @@     @           @@  @
          @@  @@-@@-@@@@@@@---@@@    @
          @@@@ @@-@@@@@        @@@@@@@   @
        -@@@     @@ @-@@--@@@@@ @@@@@
          @@         @@@@@@     @@              @@         @   @  @@@@
            @@      @            @            @          @    @@@ @@@
              @@   @              @       @@@-@           @       @@
                @@'               @   @@@                @      @
                   @                @     @                @@@  @
                   @                 @     @                 @@
                   @                 @      @                @ @
                   @                 @       @              @@@
                   @@                @       @             @   @
                    @                @       @           @@@
                  @@@ @               @  @@@@ @@@@@@@@-@@@@    @
                 @     @             @      @!             @@@
                @       @@          @        @           @@@
               @          @@       @         @        @@@
                @@          @@'@@@'          @------'@@@
               @@@@  @@     @@                @@@@@@@@
           @@@@ @    @       @@     @@      @@@
           @@@ @@@         @@      @ @  @  @@@
            @@@@@@--@@@@@@@'        @!@ @! @@@
                                @@ @ @@
    """,
    "Bulbasaur": r"""
                                             @
                        @@@@------@@@@@@@,@ @@@@@.
                     @@@          @@@@@        @
                   @@@         @@@              @
                  @   @     @@@                   @
                 @   @     @                     @@.
                 @  @     @                       @@
       @@@@      @@@@@@@  @       @@@               @@
     @@@@@@  @@@@@@@       @@--@@@@@@  @               @  @
    @  @            @@@               @              @   @
    @@         @@@@@  @               @             @    @
   @@@@    @@@@   @--@                      @@@      @     @
 @ @@ @@   @--       @@@    @  @@@         @  @@@@@      @@
 @@@@@@@           @@@  @  @  @ @ @        @@    @      @@@
 @ @@  @                 @  @@@ @@                @@@@
 @    @@@                  @@@@@@@                    @
 @@@                                 @    @@   @@@@  @
   @@   @    @                @@@@ @    @@ @@@   @@@
    @ @@ @        @@@@@@----@@@@   @   @@@@ @   @@@ @
   @   @@ @ @-@@@--@@         @@@ @@@@@@' @   @@@@@
  @   @  @ @@ @@@@@@@ @         @@@@@@@ @         @
  @ @@@ @@@@@@@@@@ @@@@       @@         @@        @
 @@@@@@ @@@@@   @@@@ @@      @         @@@       @
 @@@@@@ @@@@@@@   @@@ @@   @             @         @
 @@@@@ @@@@@@ @@@  @@ @@@'@@@@@@@@@@@@@@@
 @@@@@@@ @@ @ @@@@@ @@@@@@@
    """,
    "Squirtle": r"""
                       @@@@@@@@
                    @@@            @@@@
                  @@@                   @@@@
                @@@                        @
              @@@                           @
              @@ @               @@@@       @
             @@@@ @             @ @  @       @
             @   @            @@@@@  @@       @
             @   @            @@@@@@@       @ @
             @@@@             @@@@@@@       @ @@@
             @                       @@@@  @@  @   @
             @@@@@'-   @          @ @@@   @-@ @     @
        @@@@@@@ @@@@@@@@---------@@@         @@ @@@@@@@
        @@@@        @@@@@@@      @@@@          @  @     @
        @@ @          @   @@@@@@'    @@           @ @     @
          @@          @              @@          @  @     @
            @@        @@@@@@@@@@@@@@@@        @   @     @
              @@@    @      @          @@     @@   @     @
                 @@@@       @            @@@@@ @  @      @
                    @ @      @            @     @  @      @    @@@@@@@
                     @ @@     @          @      @  @      @  @@@
                      @  @@@@  @        @       @   @    @@@
                       @@    @@@@@@@@'@       @   @  @@@@
                        @        @        @@@ @@@@@@  @@@@@     @
                        @ @@@      @         @@@@@@@@  @     @
                       @     @@     @       @         @ @         @
                      @       @@@   @@@@@@ @          @"          @
                      @          @@@@    @@          @            @     @@@@
                      @@           @ @@@@@@          @-@@@@@@-@@@@
                        @          @      @          @
                       @@@           @     @@         @
                        @@@@@@@,,@@--'      @          @
                                      @@@@@@@@--@@@@.
    """
}

# Clase base para representar un Pokémon
class Pokemon:
    #constructor de la clase
    def __init__(self, nombre, hp, ataques):
        self.nombre = nombre
        self.hp = hp
        self.ataques = ataques

    #Permite que el Pokémon realice un ataque sobre otro Pokémon (enemigo)
    def atacar(self, ataque, enemigo):
        if ataque in self.ataques:
            dano = self.ataques[ataque]
            enemigo.hp -= dano
            print(f"{self.nombre} usa {ataque}! {enemigo.nombre} ahora tiene {max(enemigo.hp, 0)} HP.")
        else:
            print(f"{self.nombre} no conoce el ataque {ataque}.")

    #Aumenta el HP del Pokémon en 20 puntos (hasta un máximo de 100)
    def usar_pocion(self):
        self.hp = min(self.hp + 20, 100)
        print(f"{self.nombre} usa una poción! Ahora tiene {self.hp} HP.")

    #Devuelve True si está derrotado, si no lo está entonces devuelve False.
    def esta_derrotado(self):
        return self.hp <= 0

# Clase para manejar la lógica del juego
class JuegoPokemon:
    def __init__(self):
        self.logo = r"""
            _.----.        ____         ,'  _\   ___    ___     ____
        _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
        \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
        \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
          \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
           \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
            \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
             \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
              \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
               \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                    `'                            '-._|
        """
        # Cargar datos de Pokémon desde el archivo JSON
        ruta_archivo = "pokemon.json"
        self.pokemon_data = self.cargar_json(ruta_archivo)
        self.pociones = 3

    def cargar_json(self, ruta_archivo):
        # Convertimos la ruta a un objeto Path
        ruta = Path(ruta_archivo)

        # Verificamos si el archivo existe
        if not ruta.exists():
            raise FileNotFoundError(f"El archivo {ruta_archivo} no existe.")

        # Cargamos y retornamos los datos del archivo JSON
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo) #Convertimos el contenido del archivo JSON en un diccionario de Python.
            
    #Mostramos el logo del juego en la consola
    def mostrar_logo(self):
        print(self.logo)
        time.sleep(2)

    #Permite al jugador elegir un Pokémon de la lista.
    def elegir_pokemon(self):
        while True:
            print("Elige tu Pokémon:")
            for i, poke in enumerate(self.pokemon_data.keys(), 1):
                print(f"{i}. {poke}")

            try:
                eleccion = int(input("Ingresa el número de tu elección: "))
                if eleccion < 1 or eleccion > len(self.pokemon_data):
                    print("Opción no válida, por favor elige un número entre 1 y 4.")
                    continue
                else:
                    player_pokemon_name = list(self.pokemon_data.keys())[eleccion - 1]
                    player_pokemon = Pokemon(
                        player_pokemon_name,
                        self.pokemon_data[player_pokemon_name]["hp"],
                        self.pokemon_data[player_pokemon_name]["ataques"]
                    )
                    print(f"Has elegido a {player_pokemon_name}!")
                    print(ARTE_ASCII[player_pokemon_name])  # Mostrar arte ASCII
                    return player_pokemon
            except ValueError:
                print("Por favor ingresa un número válido.")

    #Selecciona aleatoriamente un Pokémon enemigo que sea diferente al elegido por el jugador
    def elegir_enemigo(self, player_pokemon):
        enemy_pokemon_name = random.choice(list(self.pokemon_data.keys()))
        while enemy_pokemon_name == player_pokemon.nombre:
            enemy_pokemon_name = random.choice(list(self.pokemon_data.keys()))
        enemy_pokemon = Pokemon(
            enemy_pokemon_name,
            self.pokemon_data[enemy_pokemon_name]["hp"],
            self.pokemon_data[enemy_pokemon_name]["ataques"]
        )
        print(f"Tu oponente será {enemy_pokemon_name}!")
        print(ARTE_ASCII[enemy_pokemon_name])  # Mostrar arte ASCII
        return enemy_pokemon

    def mostrar_barra_vida(nombre, hp_actual, hp_maximo, longitud_barra=20):
    # Calcula el porcentaje de HP restante
        porcentaje_vida = (hp_actual / hp_maximo) * 100
    
        # Calcula cuántos caracteres de la barra deben estar llenos
        caracteres_llenos = int((hp_actual / hp_maximo) * longitud_barra)
        barra = "█" * caracteres_llenos  # Caracteres llenos
        barra += " " * (longitud_barra - caracteres_llenos)  # Caracteres vacíos
    
        # Colorea la barra según el porcentaje de vida
        if porcentaje_vida > 50:
            color = "\033[92m"  # Verde
        elif porcentaje_vida > 20:
            color = "\033[93m"  # Amarillo
        else:
            color = "\033[91m"  # Rojo
    
        # Restablece el color al final
        reset_color = "\033[0m"
    
        # Muestra la barra de vida
        print(f"{nombre}: [{color}{barra}{reset_color}] {hp_actual}/{hp_maximo} HP")

    #Es el método principal que controla el flujo del juego.
    def jugar(self):
        self.mostrar_logo()
        player_pokemon = self.elegir_pokemon()
        enemy_pokemon = self.elegir_enemigo(player_pokemon)

        while player_pokemon.hp > 0 and enemy_pokemon.hp > 0:
            print("\n--- Estado actual ---")
            mostrar_barra_vida(player_pokemon.nombre, player_pokemon.hp, 100)
            mostrar_barra_vida(enemy_pokemon.nombre, enemy_pokemon.hp, 100)
            print("--------------------")

            opcion = 0
            while opcion not in [1, 2, 3]:
                print("\n¿Qué te gustaría hacer?")
                print("1. Atacar")
                print("2. Dar poción")
                print("3. Huir")

                entrada = input("Ingresa el número de tu opción: ")
                if entrada.isdigit():
                    opcion = int(entrada)
                    if opcion not in [1, 2, 3]:
                        print("Opción no válida. Inténtalo de nuevo.")
                else:
                    print("Por favor, ingresa un número válido.")

            if opcion == 1:
                print(f"\nElige un ataque para {player_pokemon.nombre}:")
                ataques = list(player_pokemon.ataques.keys())

                ataque_elegido = -1
                while ataque_elegido not in range(len(ataques)):
                    for i, atk in enumerate(ataques, 1):
                        print(f"{i}. {atk} ({player_pokemon.ataques[atk]} de daño)")

                    entrada = input("Ingresa el número de ataque: ")
                    if entrada.isdigit():
                        ataque_elegido = int(entrada) - 1
                        if ataque_elegido not in range(len(ataques)):
                            print("Opción no válida. Inténtalo de nuevo.")
                    else:
                        print("Por favor, ingresa un número válido.")

                ataque_nombre = ataques[ataque_elegido]
                player_pokemon.atacar(ataque_nombre, enemy_pokemon)

                if enemy_pokemon.esta_derrotado():
                    print(f"{enemy_pokemon.nombre} ha sido derrotado! Ganaste!")
                    break

            elif opcion == 2:
                if self.pociones > 0:
                    if player_pokemon.hp >= 100:
                        print("No puedes usar poción, tienes 100 de HP ")
                        continue
                    else:
                        self.pociones -= 1
                        player_pokemon.usar_pocion()
                        print(f"Te quedan {self.pociones} pociones.")
                else:
                    print("No te quedan pociones!")
                    continue

            elif opcion == 3:
                print(f"{player_pokemon.nombre} ha huido! Fin del juego.")
                break

            if enemy_pokemon.hp > 0:
                ataque_enemy_nombre = random.choice(list(enemy_pokemon.ataques.keys()))
                enemy_pokemon.atacar(ataque_enemy_nombre, player_pokemon)

                if player_pokemon.esta_derrotado():
                    print(f"Tu {player_pokemon.nombre} ha sido derrotado! Perdiste. ):")
                    break

            time.sleep(2)

        print("Game Over.")


# Iniciar el juego
if __name__ == "__main__":
    juego = JuegoPokemon()
    juego.jugar()
