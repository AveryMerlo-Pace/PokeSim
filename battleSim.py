from pokemon import Pokemon
import time
import random

pokemon_list = [
    Pokemon("Bulbasaur", ["Grass", "Poison"], 105, 54, 54, 50, {
        "Vine Whip": {"power": 45, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Razor Leaf": {"power": 55, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Sludge Bomb": {"power": 90, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Ivysaur", ["Grass", "Poison"], 120, 67, 68, 65, {
        "Vine Whip": {"power": 45, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Razor Leaf": {"power": 55, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Sludge Bomb": {"power": 90, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Venusaur", ["Grass", "Poison"], 140, 87, 88, 85, {
        "Vine Whip": {"power": 45, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Crunch": {"power": 80, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Razor Leaf": {"power": 55, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Sludge Bomb": {"power": 90, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Charmander", ["Fire"], 99, 57, 48, 70, {
        "Ember": {"power": 40, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Dragon", "Rock"]},
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Flamethrower": {"power": 90, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Dragon", "Rock"]}
    }),
    Pokemon("Charmeleon", ["Fire"], 118, 69, 63, 85, {
        "Ember": {"power": 40, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Dragon", "Rock"]},
        "Metal Claw": {"power": 50, "type": "Steel", "stab": 1.5, "super_effective": ["Rock", "Ice", "Fairy"], "not_very_effective": ["Fire", "Water", "Electric", "Steel"]},
        "Flamethrower": {"power": 90, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Dragon", "Rock"]},
        "Fire Spin": {"power": 35, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Dragon", "Rock"]}
    }),
    Pokemon("Charizard", ["Fire", "Flying"], 138, 89, 83, 105, {
        "Flamethrower": {"power": 90, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Dragon", "Rock"]},
        "Air Slash": {"power": 75, "type": "Flying", "stab": 1.5, "super_effective": ["Bug", "Fighting", "Grass"], "not_very_effective": ["Dragon", "Steel", "Rock"]},
        "Metal Wing": {"power": 50, "type": "Steel", "stab": 1, "super_effective": ["Rock", "Ice", "Fairy"], "not_very_effective": ["Fire", "Water", "Electric", "Steel"]},
        "Dragon Claw": {"power": 80, "type": "Dragon", "stab": 1.5, "super_effective": ["Dragon"], "not_very_effective": []}
    }),
    Pokemon("Squirtle", ["Water"], 104, 53, 70, 48, {
        "Water Gun": {"power": 40, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Dragon"]},
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Rapid Spin": {"power": 50, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Wartortle", ["Water"], 119, 68, 85, 63, {
        "Surf": {"power": 70, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Dragon"]},
        "Swift": {"power": 50, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Rapid Spin": {"power": 50, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Blastoise", ["Water"], 139, 88, 105, 83, {
        "Hydro Pump": {"power": 110, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Dragon"]},
        "Ice Beam": {"power": 90, "type": "Ice", "stab": 1, "super_effective": ["Dragon", "Flying", "Grass", "Ground"], "not_very_effective": ["Ice", "Water"]},
        "Crunch": {"power": 80, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Rapid Spin": {"power": 50, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Caterpie", ["Bug"], 105, 35, 40, 50, {
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "String Shot": {"power": 10, "type": "Bug", "stab": 1, "super_effective": [], "not_very_effective": []},
    }),
    Pokemon("Metapod", ["Bug"], 110, 25, 60, 35, {
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Harden": {"power": 0, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
    }),
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

# CREATE AND DESCRIBE USER PORKEMON
your_random_pokemon = pokemon_list[random.randint(0, 10)] # random.randint(0, len(pokemon_list)-1)
print(f"Your {your_random_pokemon.describePokemon()[0]}")
#time.sleep(1)
for i in range(1, len(your_random_pokemon.describePokemon())):
    print(f"{your_random_pokemon.describePokemon()[i]}")
    #time.sleep(1)

print("")
time.sleep(3)

# CREATE AND DESCRIBE AI POKEMON
ai_random_pokemon = pokemon_list[random.randint(0, 10)] # random.randint(0, len(pokemon_list)-1)
while your_random_pokemon == ai_random_pokemon:
    ai_random_pokemon = pokemon_list[random.randint(0, 10)] #random.randint(0, len(pokemon_list)-1)]
print(f"The AI's {ai_random_pokemon.describePokemon()[0]}")
#time.sleep(1)
for i in range(1, len(ai_random_pokemon.describePokemon())):
    print(f"{ai_random_pokemon.describePokemon()[i]}")
    #time.sleep(1)

print("")
time.sleep(3)

# DESCRIBE USER MOVESET
print(f"USER {your_random_pokemon.describeMoveset()[0]}")
#time.sleep(1)
for i in range(1, len(your_random_pokemon.describeMoveset())):
    print(your_random_pokemon.describeMoveset()[i])
    #time.sleep(1)

print("")
time.sleep(3)

# DESCRIBE AI MOVESET
print(f"AI {ai_random_pokemon.describeMoveset()[0]}")
#time.sleep(1)
for i in range(1, len(ai_random_pokemon.describeMoveset())):
    print(ai_random_pokemon.describeMoveset()[i])
    #time.sleep(1)

print("")
time.sleep(3)

# WHO ATTACKS FIRST
print(f"{ai_random_pokemon.name.upper()} (AI) ATTACKS FIRST ({ai_random_pokemon.spd} SPD > {your_random_pokemon.spd} SPD)\n" if ai_random_pokemon.spd > your_random_pokemon.spd else f"{your_random_pokemon.name.upper()} (USER) ATTACKS FIRST ({your_random_pokemon.spd} SPD > {ai_random_pokemon.spd} SPD)\n")

# ATTACK UNTIL ONE HP IS <=0
# while ai_random_pokemon.hp > 0 and your_random_pokemon.hp > 0:
#     print(f"AI HP: {ai_random_pokemon.hp}!")
#     print(f"USER HP: {your_random_pokemon.hp}!")
#     ai_random_pokemon.hp -= 1
#     your_random_pokemon.hp -= 1
