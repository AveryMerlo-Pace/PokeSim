import random
import time
#print("\n")

POKE_LEVEL = 50

class Pokemon:
    def __init__(self, name, poketype, hp, atk, defn, spd):
        self.name = name
        self.poketype = poketype
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.spd = spd
    
    def describePokemon(self):
        pokeChar = [f"POKEMON is {self.name.upper()}!"]
        if len(self.poketype) > 1:
            pokeChar.append(f"{self.name.upper()} is {self.poketype[0].upper()} and {self.poketype[1].upper()} type.")
        else:
            pokeChar.append(f"{self.name.upper()} is {self.poketype[0].upper()} type.")
        pokeChar.append(f"HP: {self.hp}")
        pokeChar.append(f"Attack: {self.atk}")
        pokeChar.append(f"Defense: {self.defn}")
        pokeChar.append(f"Speed: {self.spd}")
        return pokeChar
    
    def pokemonAttack(self):
        return ""

pokemon_list = [
    Pokemon("Bulbasaur", ["Grass", "Poison"], 105, 54, 54, 50),
    Pokemon("Ivysaur", ["Grass", "Poison"], 120, 67, 68, 65),
    Pokemon("Venusaur", ["Grass", "Poison"], 140, 87, 88, 85),
    Pokemon("Charmander", ["Fire"], 99, 57, 48, 70),
    Pokemon("Charmeleon", ["Fire"], 118, 69, 63, 85),
    Pokemon("Charizard", ["Fire", "Flying"], 138, 89, 83, 105),
    Pokemon("Squirtle", ["Water"], 104, 53, 70, 48),
    Pokemon("Wartortle", ["Water"], 119, 68, 85, 63),
    Pokemon("Blastoise", ["Water"], 139, 88, 105, 83),
    Pokemon("Caterpie", ["Bug"], 105, 35, 40, 50),
    Pokemon("Metapod", ["Bug"], 110, 25, 60, 35),
    Pokemon("Butterfree", ["Bug", "Flying"], 120, 50, 55, 80),
    Pokemon("Weedle", ["Bug", "Poison"], 100, 35, 30, 50),
    Pokemon("Kakuna", ["Bug", "Poison"], 105, 25, 50, 35),
    Pokemon("Beedrill", ["Bug", "Poison"], 125, 80, 45, 75),
    Pokemon("Pidgey", ["Normal", "Flying"], 100, 50, 45, 60),
    Pokemon("Pidgeotto", ["Normal", "Flying"], 125, 65, 60, 75),
    Pokemon("Pidgeot", ["Normal", "Flying"], 145, 85, 80, 95),
    Pokemon("Rattata", ["Normal"], 95, 60, 40, 80),
    Pokemon("Raticate", ["Normal"], 120, 85, 65, 105),
    Pokemon("Spearow", ["Normal", "Flying"], 100, 65, 35, 75),
    Pokemon("Fearow", ["Normal", "Flying"], 125, 95, 70, 105),
    Pokemon("Ekans", ["Poison"], 95, 65, 50, 60),
    Pokemon("Arbok", ["Poison"], 120, 90, 75, 85),
    Pokemon("Pikachu", ["Electric"], 95, 60, 35, 95),
    Pokemon("Raichu", ["Electric"], 120, 95, 60, 110),
    Pokemon("Sandshrew", ["Ground"], 110, 80, 90, 45),
    Pokemon("Sandslash", ["Ground"], 135, 105, 115, 70),
    Pokemon("Nidoran♀", ["Poison"], 115, 52, 57, 46),
    Pokemon("Nidorina", ["Poison"], 130, 67, 72, 61),
    Pokemon("Nidoqueen", ["Poison", "Ground"], 150, 87, 92, 81),
    Pokemon("Nidoran♂", ["Poison"], 106, 62, 45, 55),
    Pokemon("Nidorino", ["Poison"], 121, 77, 62, 70),
    Pokemon("Nidoking", ["Poison", "Ground"], 141, 97, 82, 90),
    Pokemon("Clefairy", ["Fairy"], 130, 50, 53, 40),
    Pokemon("Clefable", ["Fairy"], 155, 75, 78, 65),
    Pokemon("Vulpix", ["Fire"], 98, 46, 45, 70),
    Pokemon("Ninetales", ["Fire"], 133, 81, 80, 105),
    Pokemon("Jigglypuff", ["Normal", "Fairy"], 180, 50, 28, 25),
    Pokemon("Wigglytuff", ["Normal", "Fairy"], 205, 75, 53, 50),
    Pokemon("Zubat", ["Poison", "Flying"], 95, 50, 40, 75),
    Pokemon("Golbat", ["Poison", "Flying"], 120, 75, 65, 95),
    Pokemon("Oddish", ["Grass", "Poison"], 110, 55, 60, 40),
    Pokemon("Gloom", ["Grass", "Poison"], 125, 70, 75, 55),
    Pokemon("Vileplume", ["Grass", "Poison"], 145, 90, 95, 75),
    Pokemon("Paras", ["Bug", "Grass"], 100, 60, 55, 30),
    Pokemon("Parasect", ["Bug", "Grass"], 125, 85, 80, 55),
    Pokemon("Venonat", ["Bug", "Poison"], 115, 55, 55, 50),
    Pokemon("Venomoth", ["Bug", "Poison"], 130, 70, 65, 95)
]

your_random_pokemon = pokemon_list[random.randint(0, len(pokemon_list)-1)]
print(f"\nYour {your_random_pokemon.describePokemon()[0]}")
#time.sleep(1)
for i in range(1, len(your_random_pokemon.describePokemon())):
    print(f"{your_random_pokemon.describePokemon()[i]}")
    #time.sleep(1)
print("")
#time.sleep(3)
ai_random_pokemon = pokemon_list[random.randint(0, len(pokemon_list)-1)]
while your_random_pokemon == ai_random_pokemon:
    ai_random_pokemon = pokemon_list[random.randint(0, len(pokemon_list)-1)]
print(f"The AI's {ai_random_pokemon.describePokemon()[0]}")
#time.sleep(1)
for i in range(1, len(ai_random_pokemon.describePokemon())):
    print(f"{ai_random_pokemon.describePokemon()[i]}")
    #time.sleep(1)
print("")
print(f"{ai_random_pokemon.name.upper()} (AI) ATTACKS FIRST ({ai_random_pokemon.spd} SPD > {your_random_pokemon.spd} SPD)" if ai_random_pokemon.spd > your_random_pokemon.spd else f"{your_random_pokemon.name.upper()} (USER) ATTACKS FIRST ({your_random_pokemon.spd} SPD > {ai_random_pokemon.spd} SPD)")


    