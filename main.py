import random
import time

# Logo de Pokemon
logo = """
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
print(logo)
time.sleep(1)

# Lista de Pokémon disponibles
pokemon_list = {
    "Pikachu": {"HP": 100, "Attacks": {"Impactrueno": 20, "Rayo": 30}},
    "Charmander": {"HP": 100, "Attacks": {"Ascuas": 15, "Lanzallamas": 35}},
    "Bulbasaur": {"HP": 100, "Attacks": {"Hoja Afilada": 25, "Latigazo": 20}},
    "Squirtle": {"HP": 100, "Attacks": {"Pistola Agua": 20, "Hidrobomba": 40}}
}

pokemon_ascii = {
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
     @   @            @@@@@@@@       @ @
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

# Selección del Pokémon por el jugador
while True:
    print("Elige tu Pokémon:")
    for i, poke in enumerate(pokemon_list.keys(), 1):
        print(f"{i}. {poke}")

    try:
        eleccion = int(input("Ingresa el número de tu elección: "))
        if eleccion < 1 or eleccion > len(pokemon_list):
            print("Opción no válida, por favor elige un número entre 1 y 4.")
            continue
        else:
            player_pokemon_name = list(pokemon_list.keys())[eleccion - 1]
            player_pokemon = pokemon_list[player_pokemon_name]
            print(f"Has elegido a {player_pokemon_name}!")
            print(pokemon_ascii[player_pokemon_name])
            break  # Si la elección es válida, salimos del bucle
    except ValueError:
        print("Por favor ingresa un número válido.")


time.sleep(1)

# Elección del Pokémon enemigo
enemy_pokemon_name = random.choice(list(pokemon_list.keys()))
while enemy_pokemon_name == player_pokemon_name:
    enemy_pokemon_name = random.choice(list(pokemon_list.keys()))
enemy_pokemon = pokemon_list[enemy_pokemon_name]
print(f"Tu oponente será {enemy_pokemon_name}!")
print(pokemon_ascii[enemy_pokemon_name])

time.sleep(1)

# Contador de pociones
pociones = 5

# Batalla
while player_pokemon["HP"] > 0 and enemy_pokemon["HP"] > 0:
    # Menú de opciones
    print("\n¿Qué te gustaría hacer?")
    print("1. Atacar")
    print("2. Dar poción")
    print("3. Huir")
    
    opcion = int(input("Ingresa el número de tu opción: "))
    
    if opcion == 1:
        # Atacar
        print(f"\nEs tu turno. Elige un ataque para {player_pokemon_name}:")
        ataques = list(player_pokemon["Attacks"].keys())
        for i, atk in enumerate(ataques, 1):
            print(f"{i}. {atk} ({player_pokemon['Attacks'][atk]} de daño)")
        ataque_elegido = int(input("Ingresa el número de ataque: ")) - 1
        ataque_nombre = ataques[ataque_elegido]
        ataque_dano = player_pokemon["Attacks"][ataque_nombre]
        enemy_pokemon["HP"] -= ataque_dano
        print(f"{player_pokemon_name} usa {ataque_nombre}! {enemy_pokemon_name} ahora tiene {enemy_pokemon['HP']} HP.")
        
        if enemy_pokemon["HP"] <= 0:
            print(f"{enemy_pokemon_name} ha sido derrotado! Ganaste! 🏆")
            break

    elif opcion == 2:
        # Dar poción
        if pociones > 0:
            pociones -= 1
            player_pokemon["HP"] += 20
            print(f"Has usado una poción! {player_pokemon_name} ahora tiene {player_pokemon['HP']} HP.")
            print(f"Te quedan {pociones} pociones.")
        else:
            print("No te quedan pociones!")

    elif opcion == 3:
        # Huir
        print(f"{player_pokemon_name} ha huido! Fin del juego.")
        break
    
    # Turno del enemigo
    if enemy_pokemon["HP"] > 0:
        ataque_enemy_nombre, ataque_enemy_dano = random.choice(list(enemy_pokemon["Attacks"].items()))
        player_pokemon["HP"] -= ataque_enemy_dano
        print(f"{enemy_pokemon_name} usa {ataque_enemy_nombre}! {player_pokemon_name} ahora tiene {player_pokemon['HP']} HP.")
        
        if player_pokemon["HP"] <= 0:
            print(f"{player_pokemon_name} ha sido derrotado! Perdiste... 😢")
            break
    
    time.sleep(1)

print("Juego terminado.")
