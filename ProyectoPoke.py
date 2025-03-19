import random
import time
# Clase base para representar un Pokémon
class Pokemon:
    #constructor de la clase.
    def __init__(self, nombre, hp, ataques, ascii_art):
        self.nombre = nombre
        self.hp = hp
        self.ataques = ataques
        self.ascii_art = ascii_art  # Nuevo atributo para el arte ASCII

    #Permite que el Pokémon realice un ataque sobre otro Pokémon (enemigo).
    def atacar(self, ataque, enemigo):
        if ataque in self.ataques:
            dano = self.ataques[ataque]
            enemigo.hp -= dano
            print(f"{self.nombre} usa {ataque}! {enemigo.nombre} ahora tiene {max(enemigo.hp, 0)} HP.")
        else:
            print(f"{self.nombre} no conoce el ataque {ataque}.")

     #Aumenta el HP del Pokémon en 20 puntos (hasta un máximo de 100).
    def usar_pocion(self):
        self.hp = min(self.hp + 20, 100)
        print(f"{self.nombre} usa una poción! Ahora tiene {self.hp} HP.")

    #Devuelve True si está derrotado, si no lo está entonces devuelve False.
    def esta_derrotado(self):
        return self.hp <= 0
    #Imprime el contenido del atributo ascii_art
    def mostrar_ascii(self):
        print(self.ascii_art)  # Método para mostrar el arte ASCII


# Clases específicas para cada Pokémon, heredan de la clase Pokemon
class Pikachu(Pokemon):
    def __init__(self):
        ascii_art = r"""
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
        """
        super().__init__("Pikachu", 100, {"Impactrueno": 20, "Rayo": 30}, ascii_art)


class Charmander(Pokemon):
    def __init__(self):
        ascii_art = r"""
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
        """
        super().__init__("Charmander", 100, {"Ascuas": 15, "Lanzallamas": 35}, ascii_art)


class Bulbasaur(Pokemon):
    def __init__(self):
        ascii_art = r"""
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
        """
        super().__init__("Bulbasaur", 100, {"Hoja Afilada": 25, "Latigazo": 20}, ascii_art)


class Squirtle(Pokemon):
    def __init__(self):
        ascii_art = r"""
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
        super().__init__("Squirtle", 100, {"Pistola Agua": 20, "Hidrobomba": 40}, ascii_art)


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
        #Diccionario que mapea nombres de Pokémon a sus clases correspondientes
        self.pokemon_classes = {
            "Pikachu": Pikachu,
            "Charmander": Charmander,
            "Bulbasaur": Bulbasaur,
            "Squirtle": Squirtle
        }
        self.pociones = 3

    #Mostramos el logo del juego en la consola
    def mostrar_logo(self):
        print(self.logo)
        time.sleep(2)

    #Permite al jugador elegir un Pokémon de la lista.
    def elegir_pokemon(self):
        while True:
            print("Elige tu Pokémon:")
            for i, poke in enumerate(self.pokemon_classes.keys(), 1):
                print(f"{i}. {poke}")

            try:
                eleccion = int(input("Ingresa el número de tu elección: "))
                if eleccion < 1 or eleccion > len(self.pokemon_classes):
                    print("Opción no válida, por favor elige un número entre 1 y 4.")
                    continue
                else:
                    player_pokemon_name = list(self.pokemon_classes.keys())[eleccion - 1]
                    player_pokemon = self.pokemon_classes[player_pokemon_name]()
                    print(f"Has elegido a {player_pokemon_name}!")
                    player_pokemon.mostrar_ascii()  # Mostramos arte ASCII desde el objeto
                    return player_pokemon
            except ValueError:
                print("Por favor ingresa un número válido.")

     #Selecciona aleatoriamente un Pokémon enemigo que sea diferente al elegido por el jugador
    def elegir_enemigo(self, player_pokemon):
        enemy_pokemon_name = random.choice(list(self.pokemon_classes.keys()))
        while enemy_pokemon_name == player_pokemon.nombre:
            enemy_pokemon_name = random.choice(list(self.pokemon_classes.keys()))
        enemy_pokemon = self.pokemon_classes[enemy_pokemon_name]()
        print(f"Tu oponente será {enemy_pokemon_name}!")
        enemy_pokemon.mostrar_ascii()  # Mostrar arte ASCII desde el objeto
        return enemy_pokemon

    #Es el método principal que controla el flujo del juego.
    def jugar(self):
        self.mostrar_logo()
        player_pokemon = self.elegir_pokemon()
        enemy_pokemon = self.elegir_enemigo(player_pokemon)

        while player_pokemon.hp > 0 and enemy_pokemon.hp > 0:
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

            # Turno del enemigo
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
