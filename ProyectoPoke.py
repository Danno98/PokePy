import random
import time

# Variable que guarda en formato de texto el logo del juego
logo = r"""
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

time.sleep(2) #pausa la ejecución del programa para hacerlo mas inmersivo

# Lista de Pokemon que podemos elegir 
pokemon_list = {
    "Pikachu": {"HP": 100, "Attacks": {"Impactrueno": 20, "Rayo": 30}},
    "Charmander": {"HP": 100, "Attacks": {"Ascuas": 15, "Lanzallamas": 35}},
    "Bulbasaur": {"HP": 100, "Attacks": {"Hoja Afilada": 25, "Latigazo": 20}},
    "Squirtle": {"HP": 100, "Attacks": {"Pistola Agua": 20, "Hidrobomba": 40}}
}

#Lista de pokemon hechos en tipo codigo ascii
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

# bucle while que da a elegir el pokemon al jugador, si el jugador no elige un numeor valido le da a elegir de nuevo
# Hasta que elige uno correcto
while True:
    print("Elige tu Pokémon:")
    for i, poke in enumerate(pokemon_list.keys(), 1):
        print(f"{i}. {poke}")

    try:
        eleccion = int(input("Ingresa el número de tu elección: ")) #Variable elccion que guarda lo que teclea el usuario
        if eleccion < 1 or eleccion > len(pokemon_list): #comparamos eleccion menor a uno o eleccion mayor a la longitud de pokemon_list (4)
            print("Opción no válida, por favor elige un número entre 1 y 4.") #si ingresa un numero que no esé en el rango imprime esto
            continue
        else: #si el usuario tecleó un número válido...
            player_pokemon_name = list(pokemon_list.keys())[eleccion - 1]
            player_pokemon = pokemon_list[player_pokemon_name]
            print(f"Has elegido a {player_pokemon_name}!")
            print(pokemon_ascii[player_pokemon_name])
            break  # Si la elección es válida, salimos del bucle
    except ValueError: #si no es valida le manda al usuario el avido de que debe ingresar una opcion correcta
        print("Por favor ingresa un numero valido.")


time.sleep(2) #Pausamos la ejecución del programa

# Se elige el pokémon enemigo
enemy_pokemon_name = random.choice(list(pokemon_list.keys())) #Usamos uso de random para que se elija al pokemon enemigo 
while enemy_pokemon_name == player_pokemon_name: #Nuestro bucle while se ejecuta mientras enemy_pokemon_name sea igual al pokemon que eligió el usuario
    enemy_pokemon_name = random.choice(list(pokemon_list.keys())) # vuelve a entrar a random para elegir otro pokemon
enemy_pokemon = pokemon_list[enemy_pokemon_name] #asignamos los datalles de ese pokemon al que fue elegido para el enemigo
print(f"Tu oponente será {enemy_pokemon_name}!") #imprimimos el nombre del pokemon que se eligió
print(pokemon_ascii[enemy_pokemon_name]) #imprimimos el grafico del pokemon

time.sleep(2) 

# Hacemos un condador para las pociones que vamos a ocupar
pociones = 3

# 
while player_pokemon["HP"] > 0 and enemy_pokemon["HP"] > 0: # mientras el HP de nuestro pokemon y el del enemigo sean diferentes de cero se ejecuta
    opcion = 0
    while opcion not in [1, 2, 3]:
        print("\n¿Qué te gustaría hacer?")
        print("1. Atacar")
        print("2. Dar poción")
        print("3. Huir")
        
        entrada = input("Ingresa el número de tu opción: ") 
        if entrada.isdigit():  # Verificamos que sea un número con la funcion isdigit
            opcion = int(entrada)
            if opcion not in [1, 2, 3]: # si la opcion no esta dentro de la lista entonces...
                print("Opción no válida. Inténtalo de nuevo.") # si no es un numero dentro de la lista entonces imprime que no es valido
        else:
            print("Por favor, ingresa un número válido.") # si no es numero devuelve que tiene que teclear un numero entero

    if opcion == 1: #si el usuario teclea 1
        # Atacar
        print(f"\nElige un ataque para {player_pokemon_name}:") #imprime #Elige un ataque#
        ataques = list(player_pokemon["Attacks"].keys()) # imprime la lista de ataques de ese pokemon

        ataque_elegido = -1 
        while ataque_elegido not in range(len(ataques)): # 
            for i, atk in enumerate(ataques, 1):
                print(f"{i}. {atk} ({player_pokemon['Attacks'][atk]} de daño)")

            entrada = input("Ingresa el número de ataque: ") #Se guarda el valor tecleado por el usuario
            if entrada.isdigit(): #si es un digito 
                ataque_elegido = int(entrada) - 1  
                if ataque_elegido not in range(len(ataques)): #si no está en el rango de los ataques
                    print("Opción no válida. Inténtalo de nuevo.") #imprime que no es valido
            else: #si no es un digito
                print("Por favor, ingresa un número válido.") #pide el usuario un digito

        ataque_nombre = ataques[ataque_elegido]
        ataque_dano = player_pokemon["Attacks"][ataque_nombre]
        enemy_pokemon["HP"] -= ataque_dano
        if enemy_pokemon["HP"] <= 0: #Si el HP del pokemon enemigo es menor o igual a cero
            print(f"{player_pokemon_name} usa {ataque_nombre}! {enemy_pokemon_name} ahora tiene 0 HP.") #se imprimen
            print(f"{enemy_pokemon_name} ha sido derrotado! Ganaste!") 
            break

        else: #si no es menor o igual a cero
            print(f"{player_pokemon_name} usa {ataque_nombre}! {enemy_pokemon_name} ahora tiene {enemy_pokemon['HP']} HP.")#el juego continua

    #pociones
    elif opcion == 2: # si el usuario teclea 2
        if pociones > 0: # si pociones es mayor a cero
            pociones -= 1 # se le resta uno a pociones cuando se elige
            player_pokemon["HP"] = min(player_pokemon["HP"] + 20, 100)  # la vida no pasa de 100
            if player_pokemon["HP"] < 100: # si la vida es menor a 100 entonces
                print(f"Has usado una poción! {player_pokemon_name} ahora tiene {player_pokemon['HP']} HP.") # se imprime 
                print(f"Te quedan {pociones} pociones.")
            else: # si la vida es mayor a 100
                print(f"Tienes {player_pokemon['HP']} de HP, no puedes usar pocion" ) #imprime
                continue #volvemos al menu
        else: #si pociones es menor a cero entonces 
            print("No te quedan pociones!")
            continue #volvemos al menu

    elif opcion == 3:
        # Huir
        print(f"{player_pokemon_name} ha huido! Fin del juego.")
        break

    
    # Turno del enemigo
    if enemy_pokemon["HP"] > 0: #si la vida del enemigo es mayor a cero 
        ataque_enemy_nombre, ataque_enemy_dano = random.choice(list(enemy_pokemon["Attacks"].items()))
        player_pokemon["HP"] -= ataque_enemy_dano
        print(f"{enemy_pokemon_name} usa {ataque_enemy_nombre}! {player_pokemon_name} ahora tiene {player_pokemon['HP']} HP.")
        
    else: # si la vida del enemigo es cero o menor 
            print(f"{enemy_pokemon_name} usa {ataque_enemy_nombre}! {player_pokemon_name} ahora tiene 0 HP.")
            print(f"Tu {player_pokemon_name} ha sido derrotado! Perdiste. ):")
            break
            
    
    time.sleep(2)

print("Game Over.")
