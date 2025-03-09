from pokemon import Pokemon
import time
import random
import os

pokemon_list = [
    Pokemon("Bulbasaur", ["Grass", "Poison"], 105, 54, 54, 50, {
        "Vine Whip": {"power": 45, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Razor Leaf": {"power": 55, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Poison Gas": {"power": 40, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
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
        "Leaf Blast": {"power": 90, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Sludge Bomb": {"power": 90, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Charmander", ["Fire"], 99, 57, 48, 70, {
        "Ember": {"power": 40, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Dragon", "Rock"]},
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]}
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
        "Steel Wing": {"power": 70, "type": "Steel", "stab": 1, "super_effective": ["Rock", "Ice", "Fairy"], "not_very_effective": ["Fire", "Water", "Electric", "Steel"]},
        "Dragon Claw": {"power": 80, "type": "Dragon", "stab": 1.5, "super_effective": ["Dragon"], "not_very_effective": []}
    }),
    Pokemon("Squirtle", ["Water"], 104, 53, 70, 48, {
        "Water Gun": {"power": 40, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Dragon"]},
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]}
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
    Pokemon("Butterfree", ["Bug", "Flying"], 120, 50, 55, 80, {
        "Confusion": {"power": 50, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Gust": {"power": 40, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Bug Buzz": {"power": 90, "type": "Bug", "stab": 1.5, "super_effective": ["Grass", "Psychic", "Dark"], "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"]},
        "Sleep Powder": {"power": 0, "type": "Grass", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Weedle", ["Bug", "Poison"], 100, 35, 30, 50, {
        "Poison Sting": {"power": 15, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "String Shot": {"power": 10, "type": "Bug", "stab": 1.5, "super_effective": [], "not_very_effective": []},
    }),
    Pokemon("Kakuna", ["Bug", "Poison"], 105, 25, 50, 35, {
        "Poison Sting": {"power": 15, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Harden": {"power": 0, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
    }),
    Pokemon("Beedrill", ["Bug", "Poison"], 125, 80, 45, 75, {
        "Poison Jab": {"power": 80, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Fury Attack": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "X-Scissor": {"power": 80, "type": "Bug", "stab": 1.5, "super_effective": ["Grass", "Psychic", "Dark"], "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"]},
        "Twineedle": {"power": 25, "type": "Bug", "stab": 1.5, "super_effective": ["Grass", "Psychic", "Dark"], "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"]}
    }),
    Pokemon("Pidgey", ["Normal", "Flying"], 100, 50, 45, 60, {
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Gust": {"power": 40, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
    }),
    Pokemon("Pidgeotto", ["Normal", "Flying"], 125, 65, 60, 75, {
        "Wing Attack": {"power": 60, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Quick Attack": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Gust": {"power": 40, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Aerial Ace": {"power": 60, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]}
    }),
    Pokemon("Pidgeot", ["Normal", "Flying"], 145, 85, 80, 95, {
        "Air Slash": {"power": 75, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Quick Attack": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Hurricane": {"power": 110, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Steel Wing": {"power": 70, "type": "Steel", "stab": 1, "super_effective": ["Rock", "Ice", "Fairy"], "not_very_effective": ["Fire", "Water", "Electric", "Steel"]}
    }),
    Pokemon("Rattata", ["Normal"], 95, 60, 40, 80, {
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Quick Attack": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]}
    }),
    Pokemon("Raticate", ["Normal"], 120, 85, 65, 105, {
        "Hyper Fang": {"power": 80, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Quick Attack": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Crunch": {"power": 80, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Sucker Punch": {"power": 70, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]}
    }),
    Pokemon("Spearow", ["Normal", "Flying"], 100, 65, 35, 75, {
        "Peck": {"power": 35, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Leer": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Fury Attack": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]}
    }),
    Pokemon("Fearow", ["Normal", "Flying"], 125, 95, 70, 105, {
        "Drill Peck": {"power": 80, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Quick Attack": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Fury Attack": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Leer": {"power": 0, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Ekans", ["Poison"], 95, 65, 50, 60, {
        "Poison Sting": {"power": 15, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Wrap": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]}
    }),
    Pokemon("Arbok", ["Poison"], 120, 90, 75, 85, {
        "Poison Fang": {"power": 50, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Crunch": {"power": 80, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Gunk Shot": {"power": 120, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Glare": {"power": 0, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Pikachu", ["Electric"], 95, 60, 35, 95, {
        "Thunder Shock": {"power": 40, "type": "Electric", "stab": 1.5, "super_effective": ["Water", "Flying"], "not_very_effective": ["Electric", "Grass", "Dragon"]},
        "Quick Attack": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Thunderbolt": {"power": 90, "type": "Electric", "stab": 1.5, "super_effective": ["Water", "Flying"], "not_very_effective": ["Electric", "Grass", "Dragon"]},
        "Iron Tail": {"power": 100, "type": "Steel", "stab": 1, "super_effective": ["Rock", "Ice", "Fairy"], "not_very_effective": ["Fire", "Water", "Electric", "Steel"]}
    }),
    Pokemon("Raichu", ["Electric"], 120, 95, 60, 110, {
        "Thunderbolt": {"power": 90, "type": "Electric", "stab": 1.5, "super_effective": ["Water", "Flying"], "not_very_effective": ["Electric", "Grass", "Dragon"]},
        "Quick Attack": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Thunder": {"power": 110, "type": "Electric", "stab": 1.5, "super_effective": ["Water", "Flying"], "not_very_effective": ["Electric", "Grass", "Dragon"]},
        "Iron Tail": {"power": 100, "type": "Steel", "stab": 1, "super_effective": ["Rock", "Ice", "Fairy"], "not_very_effective": ["Fire", "Water", "Electric", "Steel"]}
    }),
    Pokemon("Sandshrew", ["Ground"], 110, 80, 90, 45, {
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Sand Attack": {"power": 0, "type": "Ground", "stab": 1, "super_effective": [], "not_very_effective": ["Flying"]},
        "Dig": {"power": 80, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]},
        "Poison Sting": {"power": 15, "type": "Poison", "stab": 1, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Sandslash", ["Ground"], 135, 105, 115, 70, {
        "Earthquake": {"power": 100, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]},
        "Slash": {"power": 75, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Dig": {"power": 80, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]},
        "Poison Jab": {"power": 80, "type": "Poison", "stab": 1, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Nidoran♀", ["Poison"], 115, 52, 57, 46, {
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Poison Sting": {"power": 15, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Growl": {"power": 0, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Nidorina", ["Poison"], 130, 67, 72, 61, {
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Poison Fang": {"power": 50, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Body Slam": {"power": 85, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]}
    }),
    Pokemon("Nidoqueen", ["Poison", "Ground"], 150, 87, 92, 81, {
        "Earthquake": {"power": 100, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]},
        "Poison Fang": {"power": 50, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Body Slam": {"power": 85, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Crunch": {"power": 80, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]}
    }),
    Pokemon("Nidoran♂", ["Poison"], 106, 62, 45, 55, {
        "Peck": {"power": 35, "type": "Flying", "stab": 1, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Poison Sting": {"power": 15, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Leer": {"power": 0, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Nidorino", ["Poison"], 121, 77, 62, 70, {
        "Horn Attack": {"power": 65, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Poison Jab": {"power": 80, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Fury Attack": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Leer": {"power": 0, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Nidoking", ["Poison", "Ground"], 141, 97, 82, 90, {
        "Earthquake": {"power": 100, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]},
        "Poison Jab": {"power": 80, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Megahorn": {"power": 120, "type": "Bug", "stab": 1, "super_effective": ["Grass", "Psychic", "Dark"], "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"]},
        "Thunderbolt": {"power": 90, "type": "Electric", "stab": 1, "super_effective": ["Water", "Flying"], "not_very_effective": ["Electric", "Grass", "Dragon"]}
    }),
    Pokemon("Clefairy", ["Fairy"], 130, 50, 53, 40, {
        "Pound": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Disarming Voice": {"power": 40, "type": "Fairy", "stab": 1.5, "super_effective": ["Fighting", "Dark", "Dragon"], "not_very_effective": ["Fire", "Poison", "Steel"]},
        "Sing": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Clefable", ["Fairy"], 155, 75, 78, 65, {
        "Moonblast": {"power": 95, "type": "Fairy", "stab": 1.5, "super_effective": ["Fighting", "Dark", "Dragon"], "not_very_effective": ["Fire", "Poison", "Steel"]},
        "Body Slam": {"power": 85, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Psychic": {"power": 90, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Metronome": {"power": 20, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Vulpix", ["Fire"], 98, 46, 45, 70, {
        "Ember": {"power": 40, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Dragon", "Rock"]},
        "Quick Attack": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Will-O-Wisp": {"power": 20, "type": "Fire", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Ninetales", ["Fire"], 133, 81, 80, 105, {
        "Flamethrower": {"power": 90, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Dragon", "Rock"]},
        "Quick Attack": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Will-O-Wisp": {"power": 20, "type": "Fire", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Extrasensory": {"power": 80, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]}
    }),
    Pokemon("Jigglypuff", ["Normal", "Fairy"], 180, 50, 28, 25, {
        "Pound": {"power": 40, "type": "Normal", "stab": 1.5, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Disarming Voice": {"power": 40, "type": "Fairy", "stab": 1.5, "super_effective": ["Fighting", "Dark", "Dragon"], "not_very_effective": ["Fire", "Poison", "Steel"]},
        "Sing": {"power": 15, "type": "Normal", "stab": 1.5, "super_effective": [], "not_very_effective": []},
        "Defense Curl": {"power": 10, "type": "Normal", "stab": 1.5, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Wigglytuff", ["Normal", "Fairy"], 205, 75, 53, 50, {
        "Double-Edge": {"power": 120, "type": "Normal", "stab": 1.5, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Play Rough": {"power": 90, "type": "Fairy", "stab": 1.5, "super_effective": ["Fighting", "Dark", "Dragon"], "not_very_effective": ["Fire", "Poison", "Steel"]},
        "Hyper Voice": {"power": 90, "type": "Normal", "stab": 1.5, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Disable": {"power": 10, "type": "Normal", "stab": 1.5, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Zubat", ["Poison", "Flying"], 95, 50, 40, 75, {
        "Absorb": {"power": 20, "type": "Grass", "stab": 1, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Gust": {"power": 40, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Poison Fang": {"power": 50, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Golbat", ["Poison", "Flying"], 120, 75, 65, 95, {
        "Wing Attack": {"power": 60, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Poison Fang": {"power": 50, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Air Cutter": {"power": 60, "type": "Flying", "stab": 1.5, "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"]},
        "Confuse Ray": {"power": 10, "type": "Ghost", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Dark"]}
    }),
    Pokemon("Oddish", ["Grass", "Poison"], 110, 55, 60, 40, {
        "Absorb": {"power": 20, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Poison Powder": {"power": 15, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Acid": {"power": 40, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Gloom", ["Grass", "Poison"], 125, 70, 75, 55, {
        "Mega Drain": {"power": 40, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Poison Powder": {"power": 15, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Acid": {"power": 40, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Lucky Chant": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Vileplume", ["Grass", "Poison"], 145, 90, 95, 75, {
        "Petal Blizzard": {"power": 90, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Sludge Bomb": {"power": 90, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Moonblast": {"power": 95, "type": "Fairy", "stab": 1, "super_effective": ["Fighting", "Dark", "Dragon"], "not_very_effective": ["Fire", "Poison", "Steel"]},
        "Sleep Powder": {"power": 15, "type": "Grass", "stab": 1.5, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Paras", ["Bug", "Grass"], 100, 60, 55, 30, {
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Absorb": {"power": 20, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Poison Powder": {"power": 15, "type": "Poison", "stab": 1, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Stun Spore": {"power": 15, "type": "Grass", "stab": 1.5, "super_effective": [], "not_very_effective": []}
    }),
   Pokemon("Parasect", ["Bug", "Grass"], 125, 85, 80, 55, {
        "X-Scissor": {"power": 80, "type": "Bug", "stab": 1.5, "super_effective": ["Grass", "Psychic", "Dark"], "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"]},
        "Giga Drain": {"power": 75, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Poison Jab": {"power": 80, "type": "Poison", "stab": 1, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Spore": {"power": 15, "type": "Grass", "stab": 1.5, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Venonat", ["Bug", "Poison"], 115, 55, 55, 50, {
        "Tackle": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Confusion": {"power": 50, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Poison Powder": {"power": 15, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Psybeam": {"power": 65, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]}
    }),
    Pokemon("Venomoth", ["Bug", "Poison"], 130, 70, 65, 95, {
        "Bug Buzz": {"power": 90, "type": "Bug", "stab": 1.5, "super_effective": ["Grass", "Psychic", "Dark"], "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"]},
        "Psychic": {"power": 90, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Sludge Bomb": {"power": 90, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]},
        "Sleep Powder": {"power": 15, "type": "Grass", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Diglett", ["Ground"], 80, 55, 25, 95, {
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Dig": {"power": 80, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]},
        "Mud-Slap": {"power": 20, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]}
    }),
    Pokemon("Dugtrio", ["Ground"], 105, 80, 50, 120, {
        "Earthquake": {"power": 100, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]},
        "Slash": {"power": 70, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Dig": {"power": 80, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]},
        "Sand Tomb": {"power": 35, "type": "Ground", "stab": 1.5, "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug"]}
    }),
    Pokemon("Meowth", ["Normal"], 90, 45, 35, 90, {
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Pay Day": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]}
    }),
    Pokemon("Persian", ["Normal"], 115, 70, 60, 115, {
        "Slash": {"power": 70, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Play Rough": {"power": 90, "type": "Fairy", "stab": 1, "super_effective": ["Fighting", "Dark", "Dragon"], "not_very_effective": ["Fire", "Poison", "Steel"]},
        "Fake Out": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Ghost", "Rock", "Steel"]}
    }),
    Pokemon("Psyduck", ["Water"], 100, 52, 48, 55, {
        "Water Gun": {"power": 40, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Dragon", "Grass"]},
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Confusion": {"power": 50, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Disable": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Golduck", ["Water"], 130, 82, 78, 85, {
        "Hydro Pump": {"power": 110, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Dragon", "Grass"]},
        "Psychic": {"power": 90, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Zen Headbutt": {"power": 80, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Fury Swipes": {"power": 18, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]}
    }),
    Pokemon("Mankey", ["Fighting"], 100, 80, 35, 70, {
        "Scratch": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Low Kick": {"power": 60, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]},
        "Leer": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Fury Swipes": {"power": 18, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]}
    }),
    Pokemon("Primeape", ["Fighting"], 120, 105, 60, 95, {
        "Close Combat": {"power": 120, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]},
        "Cross Chop": {"power": 100, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]},
        "Fury Swipes": {"power": 18, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Screech": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Growlithe", ["Fire"], 120, 70, 45, 60, {
        "Ember": {"power": 40, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Water", "Rock", "Dragon"]},
        "Bite": {"power": 60, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Leer": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Take Down": {"power": 90, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]}
    }),
    Pokemon("Arcanine", ["Fire"], 155, 110, 80, 95, {
        "Flare Blitz": {"power": 120, "type": "Fire", "stab": 1.5, "super_effective": ["Bug", "Steel", "Grass", "Ice"], "not_very_effective": ["Fire", "Water", "Rock", "Dragon"]},
        "Crunch": {"power": 80, "type": "Dark", "stab": 1, "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Fairy", "Dark"]},
        "Extreme Speed": {"power": 80, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Agility": {"power": 15, "type": "Psychic", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Poliwag", ["Water"], 100, 50, 40, 90, {
        "Bubble": {"power": 40, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"]},
        "Pound": {"power": 40, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Hypnosis": {"power": 15, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]}
    }),
    Pokemon("Poliwhirl", ["Water"], 130, 65, 65, 70, {
        "Water Gun": {"power": 40, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"]},
        "Double Slap": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Hypnosis": {"power": 15, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Bubble Beam": {"power": 65, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"]}
    }),
    Pokemon("Poliwrath", ["Water", "Fighting"], 160, 85, 95, 70, {
        "Hydro Pump": {"power": 110, "type": "Water", "stab": 1.5, "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"]},
        "Close Combat": {"power": 120, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]},
        "Dynamic Punch": {"power": 100, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]},
        "Hypnosis": {"power": 15, "type": "Psychic", "stab": 1, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]}
    }),
    Pokemon("Abra", ["Psychic"], 90, 20, 15, 90, {
        "Teleport": {"power": 10, "type": "Psychic", "stab": 1.5, "super_effective": [], "not_very_effective": []},
        "Confusion": {"power": 50, "type": "Psychic", "stab": 1.5, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]}
    }),
    Pokemon("Kadabra", ["Psychic"], 100, 35, 30, 105, {
        "Confusion": {"power": 50, "type": "Psychic", "stab": 1.5, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Psybeam": {"power": 65, "type": "Psychic", "stab": 1.5, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Disable": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []}
    }),
    Pokemon("Alakazam", ["Psychic"], 120, 50, 45, 120, {
        "Psychic": {"power": 90, "type": "Psychic", "stab": 1.5, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Psybeam": {"power": 65, "type": "Psychic", "stab": 1.5, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]},
        "Recover": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Future Sight": {"power": 120, "type": "Psychic", "stab": 1.5, "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"]}
    }),
    Pokemon("Machop", ["Fighting"], 140, 80, 50, 35, {
        "Low Kick": {"power": 60, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]},
        "Leer": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Focus Energy": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Karate Chop": {"power": 50, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]}
    }),
    Pokemon("Machoke", ["Fighting"], 160, 100, 70, 45, {
        "Low Sweep": {"power": 65, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]},
        "Leer": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Focus Energy": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Seismic Toss": {"power": 100, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]}
    }),
    Pokemon("Machamp", ["Fighting"], 180, 130, 80, 55, {
        "Close Combat": {"power": 120, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]},
        "Leer": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Focus Energy": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Dynamic Punch": {"power": 100, "type": "Fighting", "stab": 1.5, "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"], "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"]}
    }),
    Pokemon("Bellsprout", ["Grass", "Poison"], 105, 75, 50, 40, {
        "Vine Whip": {"power": 45, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Growth": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Wrap": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Poison Powder": {"power": 15, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Weepinbell", ["Grass", "Poison"], 130, 90, 65, 55, {
        "Vine Whip": {"power": 45, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Growth": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Wrap": {"power": 15, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Acid": {"power": 40, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Victreebel", ["Grass", "Poison"], 155, 105, 80, 70, {
        "Leaf Blade": {"power": 90, "type": "Grass", "stab": 1.5, "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]},
        "Growth": {"power": 10, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": []},
        "Slam": {"power": 80, "type": "Normal", "stab": 1, "super_effective": [], "not_very_effective": ["Rock", "Steel"]},
        "Sludge Bomb": {"power": 90, "type": "Poison", "stab": 1.5, "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]}
    }),
    Pokemon("Tentacool", ["Water", "Poison"], 100, 40, 35, 70),
    Pokemon("Tentacruel", ["Water", "Poison"], 150, 70, 65, 100),
    Pokemon("Geodude", ["Rock", "Ground"], 100, 80, 100, 20),
    Pokemon("Graveler", ["Rock", "Ground"], 130, 95, 115, 35),
    Pokemon("Golem", ["Rock", "Ground"], 160, 110, 130, 45),
    Pokemon("Ponyta", ["Fire"], 105, 85, 55, 90),
    Pokemon("Rapidash", ["Fire"], 130, 100, 70, 105),
    Pokemon("Slowpoke", ["Water", "Psychic"], 150, 65, 65, 15),
    Pokemon("Slowbro", ["Water", "Psychic"], 170, 75, 110, 30),
    Pokemon("Magnemite", ["Electric", "Steel"], 95, 35, 70, 45),
    Pokemon("Magneton", ["Electric", "Steel"], 125, 60, 95, 70),
    Pokemon("Farfetch'd", ["Normal", "Flying"], 115, 90, 55, 60),
    Pokemon("Doduo", ["Normal", "Flying"], 110, 85, 45, 75),
    Pokemon("Dodrio", ["Normal", "Flying"], 135, 110, 70, 100),
    Pokemon("Seel", ["Water"], 130, 45, 55, 45),
    Pokemon("Dewgong", ["Water", "Ice"], 160, 70, 80, 70),
    Pokemon("Grimer", ["Poison"], 160, 80, 50, 25),
    Pokemon("Muk", ["Poison"], 190, 105, 75, 50),
    Pokemon("Shellder", ["Water"], 100, 65, 100, 40),
    Pokemon("Cloyster", ["Water", "Ice"], 130, 95, 180, 70),
    Pokemon("Gastly", ["Ghost", "Poison"], 100, 35, 30, 80),
    Pokemon("Haunter", ["Ghost", "Poison"], 110, 50, 45, 95),
    Pokemon("Gengar", ["Ghost", "Poison"], 130, 65, 60, 110),
    Pokemon("Onix", ["Rock", "Ground"], 90, 45, 160, 70),
    Pokemon("Drowzee", ["Psychic"], 130, 48, 45, 42),
    Pokemon("Hypno", ["Psychic"], 170, 73, 70, 67),
    Pokemon("Krabby", ["Water"], 90, 105, 90, 50),
    Pokemon("Kingler", ["Water"], 110, 130, 115, 75),
    Pokemon("Voltorb", ["Electric"], 100, 30, 50, 100),
    Pokemon("Electrode", ["Electric"], 120, 50, 70, 140),
    Pokemon("Exeggcute", ["Grass", "Psychic"], 120, 40, 80, 40),
    Pokemon("Exeggutor", ["Grass", "Psychic"], 190, 95, 85, 55),
    Pokemon("Cubone", ["Ground"], 120, 50, 95, 35),
    Pokemon("Marowak", ["Ground"], 140, 80, 110, 45),
    Pokemon("Hitmonlee", ["Fighting"], 110, 120, 53, 87),
    Pokemon("Hitmonchan", ["Fighting"], 110, 105, 79, 76),
    Pokemon("Lickitung", ["Normal"], 160, 55, 75, 30),
    Pokemon("Koffing", ["Poison"], 120, 65, 95, 35),
    Pokemon("Weezing", ["Poison"], 150, 90, 120, 60),
    Pokemon("Rhyhorn", ["Ground", "Rock"], 160, 85, 95, 25),
    Pokemon("Rhydon", ["Ground", "Rock"], 190, 130, 120, 40),
    Pokemon("Chansey", ["Normal"], 250, 5, 5, 50),
    Pokemon("Tangela", ["Grass"], 130, 55, 115, 60),
    Pokemon("Kangaskhan", ["Normal"], 165, 95, 80, 90),
    Pokemon("Horsea", ["Water"], 100, 40, 70, 60),
    Pokemon("Seadra", ["Water"], 120, 65, 95, 85),
    Pokemon("Goldeen", ["Water"], 100, 67, 60, 63),
    Pokemon("Seaking", ["Water"], 130, 92, 75, 68),
    Pokemon("Staryu", ["Water"], 90, 45, 55, 85),
    Pokemon("Starmie", ["Water", "Psychic"], 120, 75, 85, 115),
    Pokemon("Mr. Mime", ["Psychic", "Fairy"], 115, 67, 87, 110),
    Pokemon("Scyther", ["Bug", "Flying"], 145, 130, 100, 125),
    Pokemon("Jynx", ["Ice", "Psychic"], 140, 72, 57, 115),
    Pokemon("Electabuzz", ["Electric"], 140, 103, 79, 125),
    Pokemon("Magmar", ["Fire"], 140, 115, 79, 113),
    Pokemon("Pinsir", ["Bug"], 140, 145, 120, 105),
    Pokemon("Tauros", ["Normal"], 150, 120, 115, 130),
    Pokemon("Magikarp", ["Water"], 95, 32, 77, 100),
    Pokemon("Gyarados", ["Water", "Flying"], 170, 145, 99, 101),
    Pokemon("Lapras", ["Water", "Ice"], 205, 105, 100, 80),
    Pokemon("Ditto", ["Normal"], 123, 70, 70, 70),
    Pokemon("Eevee", ["Normal"], 130, 77, 72, 77),
    Pokemon("Vaporeon", ["Water"], 205, 87, 82, 87),
    Pokemon("Jolteon", ["Electric"], 140, 87, 82, 150),
    Pokemon("Flareon", ["Fire"], 140, 150, 82, 87),
    Pokemon("Porygon", ["Normal"], 140, 82, 92, 60),
    Pokemon("Omanyte", ["Rock", "Water"], 110, 62, 120, 57),
    Pokemon("Omastar", ["Rock", "Water"], 145, 82, 145, 77),
    Pokemon("Kabuto", ["Rock", "Water"], 105, 100, 110, 77),
    Pokemon("Kabutops", ["Rock", "Water"], 135, 135, 125, 100),
    Pokemon("Aerodactyl", ["Rock", "Flying"], 155, 125, 87, 150),
    Pokemon("Snorlax", ["Normal"], 235, 130, 87, 50),
    Pokemon("Articuno", ["Ice", "Flying"], 165, 105, 120, 105),
    Pokemon("Zapdos", ["Electric", "Flying"], 165, 110, 105, 120),
    Pokemon("Moltres", ["Fire", "Flying"], 165, 120, 110, 110),
    Pokemon("Dratini", ["Dragon"], 116, 86, 67, 72),
    Pokemon("Dragonair", ["Dragon"], 136, 106, 87, 92),
    Pokemon("Dragonite", ["Dragon", "Flying"], 166, 155, 115, 100),
    Pokemon("Mewtwo", ["Psychic"], 181, 130, 110, 150),
    Pokemon("Mew", ["Psychic"], 175, 120, 120, 120)
]

os.system('clear')

# CREATE AND DESCRIBE USER PORKEMON
your_random_pokemon = pokemon_list[random.randint(0, len(pokemon_list)-1)]
print(f"Your {your_random_pokemon.describePokemon()[0]}")
#time.sleep(1)
for i in range(1, len(your_random_pokemon.describePokemon())):
    print(f"{your_random_pokemon.describePokemon()[i]}")
    #time.sleep(1)

print("")
time.sleep(3)

# CREATE AND DESCRIBE AI POKEMON
ai_random_pokemon = pokemon_list[random.randint(0, len(pokemon_list)-1)]
while your_random_pokemon == ai_random_pokemon:
    ai_random_pokemon = pokemon_list[random.randint(0, len(pokemon_list)-1)]
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
time.sleep(5)

os.system('clear')

# WHO ATTACKS FIRST
print(f"{ai_random_pokemon.name.upper()} (AI) ATTACKS FIRST ({ai_random_pokemon.spd} SPD > {your_random_pokemon.spd} SPD)\n" if ai_random_pokemon.spd > your_random_pokemon.spd else f"{your_random_pokemon.name.upper()} (USER) ATTACKS FIRST ({your_random_pokemon.spd} SPD > {ai_random_pokemon.spd} SPD)\n")

# ATTACK UNTIL ONE HP IS <=0
# while ai_random_pokemon.hp > 0 and your_random_pokemon.hp > 0:
#     print(f"AI HP: {ai_random_pokemon.hp}!")
#     print(f"USER HP: {your_random_pokemon.hp}!")
#     ai_random_pokemon.hp -= 1
#     your_random_pokemon.hp -= 1
