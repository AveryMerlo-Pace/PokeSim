# IMPORT STATEMENTS
from pokemon import Pokemon
from pokemonData import pokemon_list
import time
import random
import os

# WORKING DAMAGE LINE USING USER MOVE ON AI POKEMON
def userMove(pokemon, opp):
    print(f"It is your turn! What move would you like {pokemon.name.upper()} to make?")
    moveList = ""
    for move in pokemon.moves.keys():
        moveList = moveList + f"{move}    "
    print(moveList)
    print("")
    time.sleep(1.5)
    move = input("").title()
    print("")
    while move not in pokemon.moves.keys():
        print(f"{pokemon.name.upper()} does not know {move}...")
        time.sleep(0.5)
        move = input("Enter another move! ")
    print(f"{pokemon.name.upper()} uses {move}!")
    damage = pokemon.pokemonAttack(move, opp.defn, opp.poketype[0], opp.poketype[1] if len(opp.poketype) > 1 else None)
    time.sleep(1.5)
    print(f"{pokemon.name.upper()} did {damage} damage to {opp.name.upper()} with '{move}'!\n")
    time.sleep(0.5)
    return damage

# AI MOVE ON USER POKEMON
def aiMove(pokemon, opp):
    print("It is the AI's turn!")
    time.sleep(1.5)
    print("")
    ai_smart = 0 if random.randint(1,10) > 3 else 1
    if ai_smart:
        strongest = 0
        for a_move in pokemon.moves.keys():
            if pokemon.moves[a_move]["power"] > strongest:
                strongest = pokemon.moves[a_move]["power"]
                move = a_move
        print(f"{pokemon.name.upper()} (AI) uses {move.upper()}!")
        damage = pokemon.pokemonAttack(move, opp.defn, opp.poketype[0], opp.poketype[1] if len(opp.poketype) > 1 else None)
        time.sleep(1.5)
    else:
        move_number = random.randint(0, 3)
        for i, a_move in enumerate(pokemon.moves.keys()):
            if i == move_number:
                move = a_move
        print(f"{pokemon.name.upper()} (AI) uses {move.upper()}!")
        damage = pokemon.pokemonAttack(move, opp.defn, opp.poketype[0], opp.poketype[1] if len(opp.poketype) > 1 else None)
        time.sleep(1.5)
    print(f"{pokemon.name.upper()} did {damage} damage to {opp.name.upper()} with '{move}'!\n")
    time.sleep(0.5)
    return damage

def intro(your_random_pokemon, ai_random_pokemon):
    # DESCRIBE USER POKEMON
    print(f"Your {your_random_pokemon.describePokemon()[0]}")
    time.sleep(0.5)
    for i in range(1, len(your_random_pokemon.describePokemon())):
        print(f"{your_random_pokemon.describePokemon()[i]}")
        time.sleep(0.5)
    print("")
    time.sleep(1.5)
    
    # DESCRIBE AI POKEMON
    print(f"The AI's {ai_random_pokemon.describePokemon()[0]}")
    time.sleep(0.5)
    for i in range(1, len(ai_random_pokemon.describePokemon())):
        print(f"{ai_random_pokemon.describePokemon()[i]}")
        time.sleep(0.5)
    print("")
    time.sleep(1.5)
    
    # # DESCRIBE USER MOVESET
    print(f"USER {your_random_pokemon.describeMoveset()[0]}")
    time.sleep(0.5)
    for i in range(1, len(your_random_pokemon.describeMoveset())):
        print(your_random_pokemon.describeMoveset()[i])
        time.sleep(0.5)

    print("")
    time.sleep(1.5)
    
    # DESCRIBE AI MOVESET
    print(f"AI {ai_random_pokemon.describeMoveset()[0]}")
    time.sleep(0.5)
    for i in range(1, len(ai_random_pokemon.describeMoveset())):
        print(ai_random_pokemon.describeMoveset()[i])
        time.sleep(0.5)

    print("")
    time.sleep(1.5)
    
def main():

    os.system('clear')
    your_random_pokemon = pokemon_list[random.randint(0, len(pokemon_list)-1)]
    ai_random_pokemon = pokemon_list[random.randint(0, len(pokemon_list)-1)]
    while your_random_pokemon == ai_random_pokemon:
        ai_random_pokemon = pokemon_list[random.randint(0, len(pokemon_list)-1)]
    intro(your_random_pokemon, ai_random_pokemon)
    os.system('clear')
    
    # ATTACK UNTIL ONE HP IS <=0
    your_health = your_random_pokemon.hp
    ai_health = ai_random_pokemon.hp
    move = 0
    while your_health > 0 and ai_health > 0:

        print(f"TURN {move + 1}A:")
        if move == 0:
            print(f"{ai_random_pokemon.name.upper()} (AI) attacks {your_random_pokemon.name.upper()} (USER) first ({ai_random_pokemon.spd} speed > {your_random_pokemon.spd} speed)\n" if ai_random_pokemon.spd > your_random_pokemon.spd else f"{your_random_pokemon.name.upper()} (USER) ATTACKS {ai_random_pokemon.name.upper()} (AI) FIRST ({your_random_pokemon.spd} SPD > {ai_random_pokemon.spd} SPD)\n")
            attackFirst = "USER" if your_random_pokemon.spd > ai_random_pokemon.spd else "AI"
        else:
            print("")
        
        if attackFirst == "USER":
            print(f"{your_random_pokemon.name.upper()}: {your_health} / {your_random_pokemon.hp} HP")
            print("")
            damage = userMove(your_random_pokemon, ai_random_pokemon)
            ai_health = ai_random_pokemon.takeDamage(ai_health, damage) if ai_random_pokemon.takeDamage(ai_health, damage) > 0 else 0
            print(f"{ai_random_pokemon.name.upper()} has {ai_health} / {ai_random_pokemon.hp} HP left.\n")
            time.sleep(1.5)
            
            if ai_health == 0:
                print(f"{ai_random_pokemon.name.upper()} has fainted!")
                time.sleep(1.5)
                print("You win!\n")
                time.sleep(1.5)
                break
            
            time.sleep(1.5)

            print(f"TURN {move + 1}B:")
            print("")
            print(f"{ai_random_pokemon.name.upper()}: {ai_health} / {ai_random_pokemon.hp} HP")
            print("")
            damage = aiMove(ai_random_pokemon, your_random_pokemon) 
            your_health = your_random_pokemon.takeDamage(your_health, damage) if your_random_pokemon.takeDamage(your_health, damage) > 0 else 0
            print(f"{your_random_pokemon.name.upper()} has {your_health} / {your_random_pokemon.hp} HP left.\n")
            time.sleep(1.5)
            
            if your_health == 0:
                print(f"{your_random_pokemon.name.upper()} has fainted!")
                time.sleep(1.5)
                print("You lose!\n")
                time.sleep(1.5)
                break
        else:
            print(f"{ai_random_pokemon.name.upper()}: {ai_health} / {ai_random_pokemon.hp} HP")
            print("")
            damage = aiMove(ai_random_pokemon, your_random_pokemon)
            your_health = your_random_pokemon.takeDamage(your_health, damage) if your_random_pokemon.takeDamage(your_health, damage) > 0 else 0
            print(f"{your_random_pokemon.name.upper()} has {your_health} / {your_random_pokemon.hp} HP left.\n")
            time.sleep(1.5)
            
            if your_health == 0:
                print(f"{your_random_pokemon.name.upper()} has fainted!")
                time.sleep(1.5)
                print("You lose!\n")
                time.sleep(1.5)
                break
            
            time.sleep(1.5)
            
            print(f"TURN {move + 1}B:")
            print("")
            print(f"{your_random_pokemon.name.upper()}: {your_health} / {your_random_pokemon.hp} HP")
            print("")
            damage = userMove(your_random_pokemon, ai_random_pokemon)
            ai_health = ai_random_pokemon.takeDamage(ai_health, damage) if ai_random_pokemon.takeDamage(ai_health, damage) > 0 else 0
            print(f"{ai_random_pokemon.name.upper()} has {ai_health} / {ai_random_pokemon.hp} HP left.\n")
            time.sleep(1.5)
            
            if ai_health == 0:
                print(f"{ai_random_pokemon.name.upper()} has fainted!")
                time.sleep(1.5)
                print("You win!\n")
                time.sleep(1.5)
                break
            
        move = move + 1
        os.system('clear')
        
        

main()
