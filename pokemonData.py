from pokemon import Pokemon
import random

# DATA THAT NEEDS TO BE MOVED INTO A FILE

pokemon_list = [
    Pokemon("Bulbasaur", ["Grass", "Poison"], 105, 54, 54, 50, {
        "Vine Whip": {
            "power": 45, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Rock", "Ground"], 
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Razor Leaf": {
            "power": 55, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Rock", "Ground"], 
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 95
        },
        "Poison Gas": {
            "power": 20, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], 
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 90
        }
    }),
    Pokemon("Ivysaur", ["Grass", "Poison"], 120, 67, 68, 65, {
        "Vine Whip": {
            "power": 45, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Rock", "Ground"], 
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Razor Leaf": {
            "power": 55, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Rock", "Ground"], 
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 95
        },
        "Sludge Bomb": {
            "power": 90, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], 
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        }
    }),
    Pokemon("Venusaur", ["Grass", "Poison"], 140, 87, 88, 85, {
        "Vine Whip": {
            "power": 45, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Rock", "Ground"], 
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Crunch": {
            "power": 80, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"], 
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Leaf Blast": {
            "power": 120, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Rock", "Ground"], 
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 70
        },
        "Sludge Bomb": {
            "power": 90, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], 
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        }
    }),
    Pokemon("Charmander", ["Fire"], 99, 57, 48, 70, {
        "Ember": {
            "power": 40, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"], 
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"], 
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        }
    }),
    Pokemon("Charmeleon", ["Fire"], 118, 69, 63, 85, {
        "Ember": {
            "power": 40, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"], 
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Metal Claw": {
            "power": 50, "type": "Steel", "stab": 1,
            "super_effective": ["Rock", "Ice", "Fairy"], 
            "not_very_effective": ["Fire", "Water", "Electric", "Steel"],
            "accuracy": 95
        },
        "Flamethrower": {
            "power": 90, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"], 
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Fire Spin": {
            "power": 35, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"], 
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 85
        }
    }),
    Pokemon("Charizard", ["Fire", "Flying"], 138, 89, 83, 105, {
        "Flamethrower": {
            "power": 90, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"], 
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Air Slash": {
            "power": 75, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"], 
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 95
        },
        "Steel Wing": {
            "power": 70, "type": "Steel", "stab": 1,
            "super_effective": ["Rock", "Ice", "Fairy"], 
            "not_very_effective": ["Fire", "Water", "Electric", "Steel"],
            "accuracy": 90
        },
        "Dragon Claw": {
            "power": 80, "type": "Dragon", "stab": 1,
            "super_effective": ["Dragon"], 
            "not_very_effective": ["Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Squirtle", ["Water"], 104, 53, 70, 48, {
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], 
            "not_very_effective": ["Water", "Dragon", "Grass"],
            "accuracy": 100
        },
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"], 
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Wartortle", ["Water"], 119, 68, 85, 63, {
        "Surf": {
            "power": 90, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], 
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Swift": {
            "power": 60, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"], 
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Rapid Spin": {
            "power": 50, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Blastoise", ["Water"], 139, 88, 105, 83, {
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], 
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        },
        "Ice Beam": {
            "power": 90, "type": "Ice", "stab": 1,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"], 
            "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 100
        },
        "Crunch": {
            "power": 80, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"], 
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Rapid Spin": {
            "power": 50, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Caterpie", ["Bug"], 105, 35, 40, 50, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "String Shot": {
            "power": 0, "type": "Bug", "stab": 1.5,
            "super_effective": [], 
            "not_very_effective": [],
            "accuracy": 95
        }
    }),
    Pokemon("Metapod", ["Bug"], 110, 25, 60, 35, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Harden": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], 
            "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Butterfree", ["Bug", "Flying"], 120, 50, 55, 80, {
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Gust": {
            "power": 40, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Bug Buzz": {
            "power": 90, "type": "Bug", "stab": 1.5,
            "super_effective": ["Grass", "Psychic", "Dark"], 
            "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
            "accuracy": 100
        },
        "Sleep Powder": {
            "power": 0, "type": "Grass", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 75
        }
    }),
    Pokemon("Weedle", ["Bug", "Poison"], 100, 35, 30, 50, {
        "Poison Sting": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "String Shot": {
            "power": 0, "type": "Bug", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 95
        }
    }),
    Pokemon("Kakuna", ["Bug", "Poison"], 105, 25, 50, 35, {
        "Poison Sting": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Harden": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Beedrill", ["Bug", "Poison"], 125, 80, 45, 75, {
        "Poison Jab": {
            "power": 80, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Fury Attack": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        },
        "X-Scissor": {
            "power": 80, "type": "Bug", "stab": 1.5,
            "super_effective": ["Grass", "Psychic", "Dark"],
            "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
            "accuracy": 100
        },
        "Twineedle": {
            "power": 25, "type": "Bug", "stab": 1.5,
            "super_effective": ["Grass", "Psychic", "Dark"],
            "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
            "accuracy": 100
        }
    }),
    Pokemon("Pidgey", ["Normal", "Flying"], 100, 50, 45, 60, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Gust": {
            "power": 40, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        }
    }),
    Pokemon("Pidgeotto", ["Normal", "Flying"], 125, 65, 60, 75, {
        "Wing Attack": {
            "power": 60, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Gust": {
            "power": 40, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Aerial Ace": {
            "power": 60, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        }
    }),
    Pokemon("Pidgeot", ["Normal", "Flying"], 145, 85, 80, 95, {
        "Air Slash": {
            "power": 75, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 95
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Hurricane": {
            "power": 110, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 70
        },
        "Steel Wing": {
            "power": 70, "type": "Steel", "stab": 1,
            "super_effective": ["Rock", "Ice", "Fairy"],
            "not_very_effective": ["Fire", "Water", "Electric", "Steel"],
            "accuracy": 90
        }
    }),
    Pokemon("Rattata", ["Normal"], 95, 60, 40, 80, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        }
    }),
    Pokemon("Raticate", ["Normal"], 120, 85, 65, 105, {
        "Hyper Fang": {
            "power": 80, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 90
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Crunch": {
            "power": 80, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Sucker Punch": {
            "power": 70, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        }
    }),
    Pokemon("Spearow", ["Normal", "Flying"], 100, 65, 35, 75, {
        "Peck": {
            "power": 35, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Fury Attack": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        }
    }),
    Pokemon("Fearow", ["Normal", "Flying"], 125, 95, 70, 105, {
        "Drill Peck": {
            "power": 80, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Fury Attack": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        },
        "Leer": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Ekans", ["Poison"], 95, 65, 50, 60, {
        "Poison Sting": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Wrap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 90
        }
    }),
    Pokemon("Arbok", ["Poison"], 120, 90, 75, 85, {
        "Poison Fang": {
            "power": 50, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Crunch": {
            "power": 80, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Gunk Shot": {
            "power": 120, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 80
        },
        "Glare": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Pikachu", ["Electric"], 95, 60, 35, 95, {
        "Thunder Shock": {
            "power": 40, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Thunderbolt": {
            "power": 90, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Iron Tail": {
            "power": 100, "type": "Steel", "stab": 1,
            "super_effective": ["Rock", "Ice", "Fairy"],
            "not_very_effective": ["Fire", "Water", "Electric", "Steel"],
            "accuracy": 75
        }
    }),
    Pokemon("Raichu", ["Electric"], 120, 95, 60, 110, {
        "Thunderbolt": {
            "power": 90, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Thunder": {
            "power": 110, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 70
        },
        "Iron Tail": {
            "power": 100, "type": "Steel", "stab": 1,
            "super_effective": ["Rock", "Ice", "Fairy"],
            "not_very_effective": ["Fire", "Water", "Electric", "Steel"],
            "accuracy": 75
        }
    }),
    Pokemon("Sandshrew", ["Ground"], 110, 80, 90, 45, {
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Sand Attack": {
            "power": 0, "type": "Ground", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Flying"],
            "accuracy": 100
        },
        "Dig": {
            "power": 80, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 100
        },
        "Poison Sting": {
            "power": 15, "type": "Poison", "stab": 1,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        }
    }),
    Pokemon("Sandslash", ["Ground"], 135, 105, 115, 70, {
        "Earthquake": {
            "power": 100, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 100
        },
        "Slash": {
            "power": 75, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Dig": {
            "power": 80, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 100
        },
        "Poison Jab": {
            "power": 80, "type": "Poison", "stab": 1,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        }
    }),
    Pokemon("Nidoran♀", ["Poison"], 115, 52, 57, 46, {
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Poison Sting": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Growl": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Nidorina", ["Poison"], 130, 67, 72, 61, {
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Poison Fang": {
            "power": 50, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Body Slam": {
            "power": 85, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        }
    }),
    Pokemon("Nidoqueen", ["Poison", "Ground"], 150, 87, 92, 81, {
        "Earthquake": {
            "power": 100, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 100
        },
        "Poison Fang": {
            "power": 50, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Body Slam": {
            "power": 85, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Crunch": {
            "power": 80, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        }
    }),
    Pokemon("Nidoran♂", ["Poison"], 106, 62, 45, 55, {
        "Peck": {
            "power": 35, "type": "Flying", "stab": 1,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Poison Sting": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Leer": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Nidorino", ["Poison"], 121, 77, 62, 70, {
        "Horn Attack": {
            "power": 65, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Poison Jab": {
            "power": 80, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Fury Attack": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        },
        "Leer": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Nidoking", ["Poison", "Ground"], 141, 97, 82, 90, {
        "Earthquake": {
            "power": 100, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 100
        },
        "Poison Jab": {
            "power": 80, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Megahorn": {
            "power": 120, "type": "Bug", "stab": 1,
            "super_effective": ["Grass", "Psychic", "Dark"],
            "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
            "accuracy": 85
        },
        "Thunderbolt": {
            "power": 90, "type": "Electric", "stab": 1,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Clefairy", ["Fairy"], 130, 50, 53, 40, {
        "Pound": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Disarming Voice": {
            "power": 40, "type": "Fairy", "stab": 1.5,
            "super_effective": ["Fighting", "Dark", "Dragon"],
            "not_very_effective": ["Fire", "Poison", "Steel"],
            "accuracy": 100
        },
        "Sing": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 55
        }
    }),
    Pokemon("Clefable", ["Fairy"], 155, 75, 78, 65, {
        "Moonblast": {
            "power": 95, "type": "Fairy", "stab": 1.5,
            "super_effective": ["Fighting", "Dark", "Dragon"],
            "not_very_effective": ["Fire", "Poison", "Steel"],
            "accuracy": 100
        },
        "Body Slam": {
            "power": 85, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Psychic": {
            "power": 90, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Metronome": {
            "power": 20, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Vulpix", ["Fire"], 98, 46, 45, 70, {
        "Ember": {
            "power": 40, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Will-O-Wisp": {
            "power": 20, "type": "Fire", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Ninetales", ["Fire"], 133, 81, 80, 105, {
        "Flamethrower": {
            "power": 90, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Will-O-Wisp": {
            "power": 20, "type": "Fire", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 100
        },
        "Extrasensory": {
            "power": 80, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Jigglypuff", ["Normal", "Fairy"], 180, 50, 28, 25, {
        "Pound": {
            "power": 40, "type": "Normal", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"]
        },
        "Disarming Voice": {
            "power": 40, "type": "Fairy", "stab": 1.5,
            "super_effective": ["Fighting", "Dark", "Dragon"],
            "not_very_effective": ["Fire", "Poison", "Steel"]
        },
        "Sing": {
            "power": 15, "type": "Normal", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": []
        },
        "Defense Curl": {
            "power": 10, "type": "Normal", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": []
        }
    }),
    Pokemon("Wigglytuff", ["Normal", "Fairy"], 205, 75, 53, 50, {
        "Double-Edge": {
            "power": 120, "type": "Normal", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"]
        },
        "Play Rough": {
            "power": 90, "type": "Fairy", "stab": 1.5,
            "super_effective": ["Fighting", "Dark", "Dragon"],
            "not_very_effective": ["Fire", "Poison", "Steel"]
        },
        "Hyper Voice": {
            "power": 90, "type": "Normal", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"]
        },
        "Disable": {
            "power": 20, "type": "Normal", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": []
        }
    }),
    Pokemon("Zubat", ["Poison", "Flying"], 95, 50, 40, 75, {
        "Absorb": {
            "power": 20, "type": "Grass", "stab": 1,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]
        },
        "Wing Attack": {
            "power": 60, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"]
        },
        "Poison Fang": {
            "power": 50, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]
        }
    }),
    Pokemon("Golbat", ["Poison", "Flying"], 120, 75, 65, 95, {
        "Wing Attack": {
            "power": 60, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"]
        },
        "Poison Fang": {
            "power": 50, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"]
        },
        "Air Cutter": {
            "power": 60, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"]
        },
        "Confuse Ray": {
            "power": 10, "type": "Ghost", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Dark"]
        }
    }),
    Pokemon("Oddish", ["Grass", "Poison"], 110, 55, 60, 40, {
        "Absorb": {
            "power": 20, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Poison Powder": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 75
        },
        "Acid": {
            "power": 40, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        }
    }),
    Pokemon("Gloom", ["Grass", "Poison"], 125, 70, 75, 55, {
        "Mega Drain": {
            "power": 40, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Poison Powder": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 75
        },
        "Acid": {
            "power": 40, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Lucky Chant": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Vileplume", ["Grass", "Poison"], 145, 90, 95, 75, {
        "Petal Blizzard": {
            "power": 90, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Sludge Bomb": {
            "power": 90, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Moonblast": {
            "power": 95, "type": "Fairy", "stab": 1,
            "super_effective": ["Fighting", "Dark", "Dragon"],
            "not_very_effective": ["Fire", "Poison", "Steel"],
            "accuracy": 100
        },
        "Sleep Powder": {
            "power": 15, "type": "Grass", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 75
        }
    }),
    Pokemon("Paras", ["Bug", "Grass"], 100, 60, 55, 30, {
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Absorb": {
            "power": 20, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Poison Powder": {
            "power": 15, "type": "Poison", "stab": 1,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 75
        },
        "Stun Spore": {
            "power": 15, "type": "Grass", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 75
        }
    }),
    Pokemon("Parasect", ["Bug", "Grass"], 125, 85, 80, 55, {
        "X-Scissor": {
            "power": 80, "type": "Bug", "stab": 1.5,
            "super_effective": ["Grass", "Psychic", "Dark"],
            "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
            "accuracy": 100
        },
        "Giga Drain": {
            "power": 75, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Poison Jab": {
            "power": 80, "type": "Poison", "stab": 1,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Spore": {
            "power": 15, "type": "Grass", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Venonat", ["Bug", "Poison"], 115, 55, 55, 50, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Poison Powder": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 75
        },
        "Psybeam": {
            "power": 65, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Venomoth", ["Bug", "Poison"], 130, 70, 65, 95, {
        "Bug Buzz": {
            "power": 90, "type": "Bug", "stab": 1.5,
            "super_effective": ["Grass", "Psychic", "Dark"],
            "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
            "accuracy": 100
        },
        "Psychic": {
            "power": 90, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Sludge Bomb": {
            "power": 90, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Sleep Powder": {
            "power": 15, "type": "Grass", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 75
        }
    }),
    Pokemon("Diglett", ["Ground"], 80, 55, 25, 95, {
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Dig": {
            "power": 80, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 100
        },
        "Mud-Slap": {
            "power": 20, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 100
        }
    }),
    Pokemon("Dugtrio", ["Ground"], 105, 80, 50, 120, {
        "Earthquake": {
            "power": 100, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 100
        },
        "Slash": {
            "power": 70, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Dig": {
            "power": 80, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 100
        },
        "Sand Tomb": {
            "power": 35, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "accuracy": 85
        }
    }),
    Pokemon("Meowth", ["Normal"], 90, 45, 35, 90, {
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1.5,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Pay Day": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Persian", ["Normal"], 115, 70, 60, 115, {
        "Slash": {
            "power": 70, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Play Rough": {
            "power": 90, "type": "Fairy", "stab": 1,
            "super_effective": ["Fighting", "Dark", "Dragon"],
            "not_very_effective": ["Fire", "Poison", "Steel"],
            "accuracy": 90
        },
        "Fake Out": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Ghost", "Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Psyduck", ["Water"], 100, 52, 48, 55, {
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Disable": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Golduck", ["Water"], 130, 82, 78, 85, {
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        },
        "Psychic": {
            "power": 90, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Zen Headbutt": {
            "power": 80, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 90
        },
        "Fury Swipes": {
            "power": 18, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 80
        }
    }),
    Pokemon("Mankey", ["Fighting"], 100, 80, 35, 70, {
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Low Kick": {
            "power": 60, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 100
        },
        "Fury Swipes": {
            "power": 18, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 80
        }
    }),
    Pokemon("Primeape", ["Fighting"], 120, 105, 60, 95, {
        "Close Combat": {
            "power": 120, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        },
        "Cross Chop": {
            "power": 100, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 80
        },
        "Fury Swipes": {
            "power": 18, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 80
        },
        "Screech": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 85
        }
    }),
    Pokemon("Growlithe", ["Fire"], 120, 70, 45, 60, {
        "Ember": {
            "power": 40, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 100
        },
        "Take Down": {
            "power": 90, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        }
    }),
    Pokemon("Arcanine", ["Fire"], 155, 110, 80, 95, {
        "Flare Blitz": {
            "power": 120, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Crunch": {
            "power": 80, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Extreme Speed": {
            "power": 80, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Agility": {
            "power": 15, "type": "Psychic", "stab": 1,
            "super_effective": [],
            "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Poliwag", ["Water"], 100, 50, 40, 90, {
        "Bubble": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Pound": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60
        }
    }),
    Pokemon("Poliwhirl", ["Water"], 130, 65, 65, 70, {
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Double Slap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60
        },
        "Bubble Beam": {
            "power": 65, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Poliwrath", ["Water", "Fighting"], 160, 85, 95, 70, {
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        },
        "Close Combat": {
            "power": 120, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        },
        "Dynamic Punch": {
            "power": 100, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 50
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60
        }
    }),
    Pokemon("Abra", ["Psychic"], 90, 20, 15, 90, {
        "Teleport": {
            "power": 10, "type": "Psychic", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Kadabra", ["Psychic"], 100, 35, 30, 105, {
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Psybeam": {
            "power": 65, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Disable": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Alakazam", ["Psychic"], 120, 50, 45, 120, {
        "Psychic": {
            "power": 90, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Psybeam": {
            "power": 65, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Recover": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Future Sight": {
            "power": 120, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Machop", ["Fighting"], 140, 80, 50, 35, {
        "Low Kick": {
            "power": 60, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Focus Energy": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Karate Chop": {
            "power": 50, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        }
    }),
    Pokemon("Machoke", ["Fighting"], 160, 100, 70, 45, {
        "Low Sweep": {
            "power": 65, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Focus Energy": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Seismic Toss": {
            "power": 100, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        }
    }),
    Pokemon("Machamp", ["Fighting"], 180, 130, 80, 55, {
        "Close Combat": {
            "power": 120, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Focus Energy": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Dynamic Punch": {
            "power": 100, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 50
        }
    }),
    Pokemon("Bellsprout", ["Grass", "Poison"], 105, 75, 50, 40, {
        "Vine Whip": {
            "power": 45, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Rock", "Ground"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Growth": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Wrap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 90
        },
        "Poison Powder": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 75
        }
    }),
    Pokemon("Weepinbell", ["Grass", "Poison"], 130, 90, 65, 55, {
        "Vine Whip": {
            "power": 45, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Rock", "Ground"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Growth": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Wrap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 90
        },
        "Acid": {
            "power": 40, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        }
    }),
    Pokemon("Victreebel", ["Grass", "Poison"], 155, 105, 80, 70, {
        "Leaf Blade": {
            "power": 90, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Growth": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Slam": {
            "power": 80, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 75
        },
        "Sludge Bomb": {
            "power": 90, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        }
    }),
    Pokemon("Tentacool", ["Water", "Poison"], 100, 40, 35, 70, {
        "Bubble": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Poison Sting": {
            "power": 15, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Wrap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 90
        },
        "Supersonic": {
            "power": 20, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 55
        }
    }),
    Pokemon("Tentacruel", ["Water", "Poison"], 150, 70, 65, 100, {
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        },
        "Poison Jab": {
            "power": 80, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Wrap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 90
        },
        "Acid Armor": {
            "power": 20, "type": "Poison", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Geodude", ["Rock", "Ground"], 100, 80, 100, 20, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Rock Throw": {
            "power": 50, "type": "Rock", "stab": 1.5,
            "super_effective": ["Fire", "Ice", "Flying", "Bug"],
            "not_very_effective": ["Normal", "Fighting", "Ground", "Steel"],
            "accuracy": 90
        },
        "Defense Curl": {
            "power": 20, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Magnitude": {
            "power": 70, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        }
    }),
    Pokemon("Graveler", ["Rock", "Ground"], 130, 95, 115, 35, {
        "Rock Slide": {
            "power": 75, "type": "Rock", "stab": 1.5,
            "super_effective": ["Fire", "Ice", "Flying", "Bug"],
            "not_very_effective": ["Normal", "Fighting", "Ground", "Steel"],
            "accuracy": 90
        },
        "Magnitude": {
            "power": 70, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        },
        "Rollout": {
            "power": 30, "type": "Rock", "stab": 1.5,
            "super_effective": ["Fire", "Ice", "Flying", "Bug"],
            "not_very_effective": ["Normal", "Fighting", "Ground", "Steel"],
            "accuracy": 90
        },
        "Self-Destruct": {
            "power": 200, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost", "Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Golem", ["Rock", "Ground"], 160, 110, 130, 45, {
        "Earthquake": {
            "power": 100, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        },
        "Stone Edge": {
            "power": 100, "type": "Rock", "stab": 1.5,
            "super_effective": ["Fire", "Ice", "Flying", "Bug"],
            "not_very_effective": ["Normal", "Fighting", "Ground", "Steel"],
            "accuracy": 80
        },
        "Rollout": {
            "power": 30, "type": "Rock", "stab": 1.5,
            "super_effective": ["Fire", "Ice", "Flying", "Bug"],
            "not_very_effective": ["Normal", "Fighting", "Ground", "Steel"],
            "accuracy": 90
        },
        "Explosion": {
            "power": 250, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost", "Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Ponyta", ["Fire"], 105, 85, 55, 90, {
        "Ember": {
            "power": 40, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Tail Whip": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Stomp": {
            "power": 65, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Flame Wheel": {
            "power": 60, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Rapidash", ["Fire"], 130, 100, 70, 105, {
        "Flare Blitz": {
            "power": 120, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100, "recoil": True
        },
        "Tail Whip": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Stomp": {
            "power": 65, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Megahorn": {
            "power": 120, "type": "Bug", "stab": 1,
            "super_effective": ["Grass", "Psychic", "Dark"],
            "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
            "accuracy": 85
        }
    }),
    Pokemon("Slowpoke", ["Water", "Psychic"], 150, 65, 65, 15, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Yawn": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Slowbro", ["Water", "Psychic"], 170, 75, 110, 30, {
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        },
        "Psychic": {
            "power": 90, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Withdraw": {
            "power": 15, "type": "Water", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Slack Off": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Magnemite", ["Electric", "Steel"], 95, 35, 70, 45, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Thunder Shock": {
            "power": 40, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"], "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Metal Sound": {
            "power": 10, "type": "Steel", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 85
        },
        "Sonic Boom": {
            "power": 20, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost"],
            "accuracy": 90
        }
    }),
    Pokemon("Magneton", ["Electric", "Steel"], 125, 60, 95, 70, {
        "Thunderbolt": {
            "power": 90, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"], "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Metal Claw": {
            "power": 50, "type": "Steel", "stab": 1.5,
            "super_effective": ["Rock", "Ice", "Fairy"], "not_very_effective": ["Fire", "Water", "Electric", "Steel"],
            "accuracy": 95
        },
        "Tri Attack": {
            "power": 80, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Magnet Bomb": {
            "power": 60, "type": "Steel", "stab": 1.5,
            "super_effective": ["Rock", "Ice", "Fairy"], "not_very_effective": ["Fire", "Water", "Electric", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Farfetch'd", ["Normal", "Flying"], 115, 90, 55, 60, {
        "Peck": {
            "power": 35, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Fury Attack": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        },
        "Cut": {
            "power": 50, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 95
        }
    }),
    Pokemon("Doduo", ["Normal", "Flying"], 110, 85, 45, 75, {
        "Peck": {
            "power": 35, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Growl": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Fury Attack": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        },
        "Tri Attack": {
            "power": 80, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Dodrio", ["Normal", "Flying"], 135, 110, 70, 100, {
        "Drill Peck": {
            "power": 80, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"], "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Growl": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Fury Attack": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        },
        "Tri Attack": {
            "power": 80, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Seel", ["Water"], 130, 45, 55, 45, {
        "Headbutt": {
            "power": 70, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Growl": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Icy Wind": {
            "power": 55, "type": "Ice", "stab": 1,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"], "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 95
        },
        "Bubble Beam": {
            "power": 65, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Dewgong", ["Water", "Ice"], 160, 70, 80, 70, {
        "Ice Beam": {
            "power": 90, "type": "Ice", "stab": 1,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"], "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 100
        },
        "Headbutt": {
            "power": 70, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Aqua Jet": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Aurora Beam": {
            "power": 65, "type": "Ice", "stab": 1.5,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"], "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Grimer", ["Poison"], 160, 80, 50, 25, {
        "Pound": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Poison Gas": {
            "power": 20, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 90
        },
        "Disable": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Sludge": {
            "power": 65, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        }
    }),
    Pokemon("Muk", ["Poison"], 190, 105, 75, 50, {
        "Pound": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Sludge Bomb": {
            "power": 90, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        },
        "Disable": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Gunk Shot": {
            "power": 120, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 80
        }
    }),
    Pokemon("Shellder", ["Water"], 100, 65, 100, 40, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Withdraw": {
            "power": 15, "type": "Water", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Ice Shard": {
            "power": 40, "type": "Ice", "stab": 1,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"], "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 100
        },
        "Bubble Beam": {
            "power": 65, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Cloyster", ["Water", "Ice"], 130, 95, 180, 70, {
        "Icicle Spear": {
            "power": 25, "type": "Ice", "stab": 1.5,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"], "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 100
        },
        "Withdraw": {
            "power": 15, "type": "Water", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Spike Cannon": {
            "power": 20, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost"],
            "accuracy": 100
        },
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        }
    }),
    Pokemon("Gastly", ["Ghost", "Poison"], 100, 35, 30, 80, {
        "Lick": {
            "power": 30, "type": "Ghost", "stab": 1.5,
            "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60
        },
        "Confuse Ray": {
            "power": 10, "type": "Ghost", "stab": 1.5,
            "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100
        },
        "Night Shade": {
            "power": 100, "type": "Ghost", "stab": 1.5,
            "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100
        }
    }),
    Pokemon("Haunter", ["Ghost", "Poison"], 110, 50, 45, 95, {
        "Lick": {
            "power": 30, "type": "Ghost", "stab": 1.5,
            "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60
        },
        "Confuse Ray": {
            "power": 10, "type": "Ghost", "stab": 1.5,
            "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100
        },
        "Shadow Ball": {
            "power": 80, "type": "Ghost", "stab": 1.5,
            "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100
        }
    }),
    Pokemon("Gengar", ["Ghost", "Poison"], 130, 65, 60, 110, {
        "Shadow Ball": {
            "power": 80, "type": "Ghost", "stab": 1.5,
            "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60
        },
        "Confuse Ray": {
            "power": 10, "type": "Ghost", "stab": 1.5,
            "super_effective": ["Ghost", "Psychic"], "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100
        },
        "Sludge Bomb": {
            "power": 90, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"], "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100
        }
    }),
    Pokemon("Onix", ["Rock", "Ground"], 90, 45, 160, 70, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Rock Throw": {
            "power": 50, "type": "Rock", "stab": 1.5,
            "super_effective": ["Fire", "Ice", "Flying", "Bug"], "not_very_effective": ["Normal", "Fighting", "Ground", "Steel"],
            "accuracy": 90
        },
        "Harden": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Dig": {
            "power": 80, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"], "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        }
    }),
    Pokemon("Drowzee", ["Psychic"], 130, 48, 45, 42, {
        "Pound": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60
        },
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Disable": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Hypno", ["Psychic"], 170, 73, 70, 67, {
        "Psychic": {
            "power": 90, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60
        },
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Dream Eater": {
            "power": 100, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Krabby", ["Water"], 90, 105, 90, 50, {
        "Bubble": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Vice Grip": {
            "power": 55, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Harden": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Kingler", ["Water"], 110, 130, 115, 75, {
        "Crabhammer": {
            "power": 100, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"], "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 90
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Vice Grip": {
            "power": 55, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Guillotine": {
            "power": 230, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost", "Rock", "Steel"],
            "accuracy": 30  # Guillotine is a one-hit KO move with 30% accuracy
        }
    }),
    Pokemon("Voltorb", ["Electric"], 100, 30, 50, 100, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Sonic Boom": {
            "power": 20, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost"],
            "accuracy": 90  # Fixed accuracy for Sonic Boom
        },
        "Screech": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 85  # Fixed accuracy for Screech
        },
        "Spark": {
            "power": 65, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"], "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Electrode", ["Electric"], 120, 50, 70, 140, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Sonic Boom": {
            "power": 20, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost"],
            "accuracy": 90
        },
        "Screech": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 85
        },
        "Thunderbolt": {
            "power": 90, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"], "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Exeggcute", ["Grass", "Psychic"], 120, 40, 80, 40, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60  # Fixed accuracy for Hypnosis
        },
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Barrage": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost", "Rock", "Steel"],
            "accuracy": 85  # Fixed accuracy for Barrage
        }
    }),
    Pokemon("Exeggutor", ["Grass", "Psychic"], 190, 95, 85, 55, {
        "Psychic": {
            "power": 90, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Hypnosis": {
            "power": 15, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 60
        },
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"], "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Solar Beam": {
            "power": 120, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Rock"], "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Cubone", ["Ground"], 120, 50, 95, 35, {
        "Bone Club": {
            "power": 65, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 85  # Fixed accuracy for Bone Club
        },
        "Growl": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Headbutt": {
            "power": 70, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Marowak", ["Ground"], 140, 80, 110, 45, {
        "Earthquake": {
            "power": 100, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        },
        "Growl": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Bonemerang": {
            "power": 50, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 90  # Fixed accuracy for Bonemerang
        }
    }),
    Pokemon("Hitmonlee", ["Fighting"], 110, 120, 53, 87, {
        "High Jump Kick": {
            "power": 130, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 90  # Fixed accuracy for High Jump Kick
        },
        "Double Kick": {
            "power": 30, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100  # Fixed accuracy for Double Kick
        },
        "Rolling Kick": {
            "power": 60, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 85  # Fixed accuracy for Rolling Kick
        },
        "Mega Kick": {
            "power": 120, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 75  # Fixed accuracy for Mega Kick
        }
    }),
    Pokemon("Hitmonchan", ["Fighting"], 110, 105, 79, 76, {
        "Close Combat": {
            "power": 120, "type": "Fighting", "stab": 1.5,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100  # Fixed accuracy for Close Combat
        },
        "Ice Punch": {
            "power": 75, "type": "Ice", "stab": 1,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"],
            "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 100  # Fixed accuracy for Ice Punch
        },
        "Thunder Punch": {
            "power": 75, "type": "Electric", "stab": 1,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100  # Fixed accuracy for Thunder Punch
        },
        "Fire Punch": {
            "power": 75, "type": "Fire", "stab": 1,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100  # Fixed accuracy for Fire Punch
        }
    }),
    Pokemon("Lickitung", ["Normal"], 160, 55, 75, 30, {
        "Lick": {
            "power": 30, "type": "Ghost", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100  # Fixed accuracy for Lick
        },
        "Wrap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 90  # Fixed accuracy for Wrap
        },
        "Defense Curl": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Fixed accuracy for Defense Curl
        },
        "Slam": {
            "power": 80, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 75  # Fixed accuracy for Slam
        }
    }),
    Pokemon("Koffing", ["Poison"], 120, 65, 95, 35, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Smog": {
            "power": 30, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 70  # Fixed accuracy for Smog
        },
        "Self-Destruct": {
            "power": 200, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost", "Rock", "Steel"],
            "accuracy": 100  # Fixed accuracy for Self-Destruct
        },
        "Sludge": {
            "power": 65, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100  # Fixed accuracy for Sludge
        }
    }),
    Pokemon("Weezing", ["Poison"], 150, 90, 120, 60, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Sludge Bomb": {
            "power": 90, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 100  # Fixed accuracy for Sludge Bomb
        },
        "Explosion": {
            "power": 250, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost", "Rock", "Steel"],
            "accuracy": 100  # Fixed accuracy for Explosion
        },
        "Gunk Shot": {
            "power": 120, "type": "Poison", "stab": 1.5,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 80  # Fixed accuracy for Gunk Shot
        }
    }),
    Pokemon("Rhyhorn", ["Ground", "Rock"], 160, 85, 95, 25, {
        "Horn Attack": {
            "power": 65, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100  # Fixed accuracy for Horn Attack
        },
        "Stomp": {
            "power": 65, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100  # Fixed accuracy for Stomp
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Fixed accuracy for Leer
        },
        "Rock Throw": {
            "power": 50, "type": "Rock", "stab": 1.5,
            "super_effective": ["Fire", "Ice", "Flying", "Bug"],
            "not_very_effective": ["Normal", "Fighting", "Ground", "Steel"],
            "accuracy": 90  # Fixed accuracy for Rock Throw
        }
    }),
    Pokemon("Rhydon", ["Ground", "Rock"], 190, 130, 120, 40, {
        "Earthquake": {
            "power": 100, "type": "Ground", "stab": 1.5,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100  # Fixed accuracy for Earthquake
        },
        "Stomp": {
            "power": 65, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100  # Fixed accuracy for Stomp
        },
        "Leer": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Fixed accuracy for Leer
        },
        "Rock Slide": {
            "power": 75, "type": "Rock", "stab": 1.5,
            "super_effective": ["Fire", "Ice", "Flying", "Bug"],
            "not_very_effective": ["Normal", "Fighting", "Ground", "Steel"],
            "accuracy": 90  # Fixed accuracy for Rock Slide
        }
    }),
    Pokemon("Chansey", ["Normal"], 250, 50, 150, 50, {
        "Pound": {
            "power": 40, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100  # Fixed accuracy for Pound
        },
        "Growl": {
            "power": 10, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Fixed accuracy for Growl
        },
        "Double Slap": {
            "power": 15, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85  # Fixed accuracy for Double Slap
        },
        "Soft-Boiled": {
            "power": 0, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Healing move, accuracy is 100%
        }
    }),
    Pokemon("Tangela", ["Grass"], 130, 55, 115, 60, {
        "Constrict": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100  # Fixed accuracy for Constrict
        },
        "Absorb": {
            "power": 20, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100  # Fixed accuracy for Absorb
        },
        "Poison Powder": {
            "power": 0, "type": "Poison", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 75  # Fixed accuracy for Poison Powder
        },
        "Vine Whip": {
            "power": 45, "type": "Grass", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100  # Fixed accuracy for Vine Whip
        }
    }),
    Pokemon("Kangaskhan", ["Normal"], 165, 95, 80, 90, {
        "Comet Punch": {
            "power": 18, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85  # Fixed accuracy for Comet Punch
        },
        "Leer": {
            "power": 0, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Leer is a status move
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark", "Fighting"],  # Added Fighting as it resists Dark
            "accuracy": 100
        },
        "Mega Punch": {
            "power": 80, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85  # Fixed accuracy for Mega Punch
        }
    }),
    Pokemon("Horsea", ["Water"], 100, 40, 70, 60, {
        "Bubble": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Leer": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Leer is a status move
        },
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Twister": {
            "power": 40, "type": "Dragon", "stab": 1,
            "super_effective": ["Dragon"],
            "not_very_effective": ["Steel"],  # Steel resists Dragon
            "accuracy": 100
        }
    }),
    Pokemon("Seadra", ["Water"], 120, 65, 95, 85, {
        "Bubble Beam": {
            "power": 65, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Leer": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Leer is a status move
        },
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Twister": {
            "power": 40, "type": "Dragon", "stab": 1,
            "super_effective": ["Dragon"],
            "not_very_effective": ["Steel"],  # Steel resists Dragon
            "accuracy": 100
        }
    }),
    Pokemon("Goldeen", ["Water"], 100, 67, 60, 63, {
        "Peck": {
            "power": 35, "type": "Flying", "stab": 1,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Tail Whip": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Tail Whip is a status move
        },
        "Horn Attack": {
            "power": 65, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Seaking", ["Water"], 130, 92, 75, 68, {
        "Peck": {
            "power": 35, "type": "Flying", "stab": 1,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Tail Whip": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Tail Whip is a status move
        },
        "Horn Drill": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Ghost", "Rock", "Steel"],
            "accuracy": 30  # Horn Drill is a one-hit KO move with low accuracy
        },
        "Waterfall": {
            "power": 80, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Staryu", ["Water"], 90, 45, 55, 85, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Harden": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Harden is a status move
        },
        "Swift": {
            "power": 60, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100  # Swift never misses
        }
    }),
    Pokemon("Starmie", ["Water", "Psychic"], 120, 75, 85, 115, {
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        },
        "Psychic": {
            "power": 90, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Recover": {
            "power": 0, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100  # Recover is a healing move
        },
        "Thunderbolt": {
            "power": 90, "type": "Electric", "stab": 1,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Mr. Mime", ["Psychic", "Fairy"], 115, 67, 87, 110, {
        "Confusion": {
            "power": 50, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Double Slap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        },
        "Light Screen": {
            "power": 15, "type": "Psychic", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Dazzling Gleam": {
            "power": 80, "type": "Fairy", "stab": 1.5,
            "super_effective": ["Fighting", "Dark", "Dragon"],
            "not_very_effective": ["Fire", "Poison", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Scyther", ["Bug", "Flying"], 145, 130, 100, 125, {
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Leer": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Focus Energy": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Wing Attack": {
            "power": 60, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        }
    }),
    Pokemon("Jynx", ["Ice", "Psychic"], 140, 72, 57, 115, {
        "Pound": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Lovely Kiss": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 75
        },
        "Double Slap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 85
        },
        "Ice Punch": {
            "power": 75, "type": "Ice", "stab": 1.5,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"],
            "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Electabuzz", ["Electric"], 140, 103, 79, 125, {
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Leer": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Thunder Shock": {
            "power": 40, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Thunder Punch": {
            "power": 75, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Magmar", ["Fire"], 140, 115, 79, 113, {
        "Ember": {
            "power": 40, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Leer": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Smog": {
            "power": 30, "type": "Poison", "stab": 1,
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "accuracy": 70
        },
        "Fire Punch": {
            "power": 75, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Pinsir", ["Bug"], 140, 145, 120, 105, {
        "Vice Grip": {
            "power": 55, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Leer": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Focus Energy": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Seismic Toss": {
            "power": 100, "type": "Fighting", "stab": 1,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        }
    }),
    Pokemon("Tauros", ["Normal"], 150, 120, 115, 130, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Leer": {
            "power": 15, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Horn Attack": {
            "power": 65, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Rage": {
            "power": 20, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Ghost", "Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Magikarp", ["Water"], 95, 32, 77, 100, {
        "Splash": {
            "power": 15, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Gyarados", ["Water", "Flying"], 170, 145, 99, 101, {
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        },
        "Leer": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Dragon Rage": {
            "power": 40, "type": "Dragon", "stab": 1,
            "super_effective": ["Dragon"],
            "not_very_effective": ["Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Lapras", ["Water", "Ice"], 205, 105, 100, 80, {
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Growl": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Sing": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Ice Beam": {
            "power": 90, "type": "Ice", "stab": 1.5,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"],
            "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Ditto", ["Normal"], 123, 70, 70, 70, {
        "Transform": {
            "power": 15, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Eevee", ["Normal"], 130, 77, 72, 77, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Tail Whip": {
            "power": 15, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Sand Attack": {
            "power": 15, "type": "Ground", "stab": 1,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        },
        "Quick Attack": {
            "power": 40, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Vaporeon", ["Water"], 205, 87, 82, 87, {
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Tail Whip": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Sand Attack": {
            "power": 10, "type": "Ground", "stab": 1,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        },
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        }
    }),
    Pokemon("Jolteon", ["Electric"], 140, 87, 82, 150, {
        "Thunder Shock": {
            "power": 40, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Tail Whip": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Sand Attack": {
            "power": 10, "type": "Ground", "stab": 1,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        },
        "Thunderbolt": {
            "power": 90, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Flareon", ["Fire"], 140, 150, 82, 87, {
        "Ember": {
            "power": 40, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Tail Whip": {
            "power": 10, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Sand Attack": {
            "power": 10, "type": "Ground", "stab": 1,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        },
        "Fire Blast": {
            "power": 110, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 85
        }
    }),
    Pokemon("Porygon", ["Normal"], 140, 82, 92, 60, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Sharpen": {
            "power": 10, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Conversion": {
            "power": 10, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Tri Attack": {
            "power": 80, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Omanyte", ["Rock", "Water"], 110, 62, 120, 57, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Withdraw": {
            "power": 15, "type": "Water", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Water Gun": {
            "power": 40, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        }
    }),
    Pokemon("Omastar", ["Rock", "Water"], 145, 82, 145, 77, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Withdraw": {
            "power": 15, "type": "Water", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        }
    }),
    Pokemon("Kabuto", ["Rock", "Water"], 105, 100, 110, 77, {
        "Scratch": {
            "power": 40, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Harden": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Absorb": {
            "power": 20, "type": "Grass", "stab": 1,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Leer": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        }
    }),
    Pokemon("Kabutops", ["Rock", "Water"], 135, 135, 125, 100, {
        "Slash": {
            "power": 70, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Harden": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Absorb": {
            "power": 20, "type": "Grass", "stab": 1,
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "accuracy": 100
        },
        "Hydro Pump": {
            "power": 110, "type": "Water", "stab": 1.5,
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "accuracy": 80
        }
    }),
    Pokemon("Aerodactyl", ["Rock", "Flying"], 155, 125, 87, 150, {
        "Wing Attack": {
            "power": 60, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Agility": {
            "power": 15, "type": "Psychic", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Bite": {
            "power": 60, "type": "Dark", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Fairy", "Dark"],
            "accuracy": 100
        },
        "Ancient Power": {
            "power": 60, "type": "Rock", "stab": 1.5,
            "super_effective": ["Fire", "Ice", "Flying", "Bug"],
            "not_very_effective": ["Normal", "Fighting", "Ground", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Snorlax", ["Normal"], 235, 130, 87, 50, {
        "Tackle": {
            "power": 40, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        },
        "Defense Curl": {
            "power": 15, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Amnesia": {
            "power": 15, "type": "Psychic", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Body Slam": {
            "power": 85, "type": "Normal", "stab": 1.5,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Articuno", ["Ice", "Flying"], 165, 105, 120, 105, {
        "Blizzard": {
            "power": 110, "type": "Ice", "stab": 1.5,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"],
            "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 70
        },
        "Hurricane": {
            "power": 110, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 70
        },
        "Sheer Cold": {
            "power": 130, "type": "Ice", "stab": 1.5,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"],
            "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 30
        },
        "Freeze-Dry": {
            "power": 70, "type": "Ice", "stab": 1.5,
            "super_effective": ["Water", "Ground", "Flying", "Dragon"],
            "not_very_effective": ["Fire", "Ice", "Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Zapdos", ["Electric", "Flying"], 165, 110, 105, 120, {
        "Thunder": {
            "power": 110, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 70
        },
        "Sky Attack": {
            "power": 140, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 90
        },
        "Drill Peck": {
            "power": 80, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100
        },
        "Discharge": {
            "power": 80, "type": "Electric", "stab": 1.5,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Moltres", ["Fire", "Flying"], 165, 120, 110, 110, {
        "Fire Blast": {
            "power": 110, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 85
        },
        "Brave Bird": {
            "power": 120, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 100, "recoil": True
        },
        "Sky Attack": {
            "power": 140, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 90, "charge": True
        },
        "Heat Wave": {
            "power": 95, "type": "Fire", "stab": 1.5,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 90
        }
    }),
    Pokemon("Dratini", ["Dragon"], 116, 86, 67, 72, {
        "Wrap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 90
        },
        "Leer": {
            "power": 20, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Thunder Wave": {
            "power": 20, "type": "Electric", "stab": 1,
            "super_effective": [], "not_very_effective": ["Electric", "Ground"],
            "accuracy": 90
        },
        "Twister": {
            "power": 40, "type": "Dragon", "stab": 1.5,
            "super_effective": ["Dragon"], "not_very_effective": ["Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Dragonair", ["Dragon"], 136, 106, 87, 92, {
        "Wrap": {
            "power": 15, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": ["Rock", "Steel"],
            "accuracy": 90
        },
        "Leer": {
            "power": 20, "type": "Normal", "stab": 1,
            "super_effective": [], "not_very_effective": [],
            "accuracy": 100
        },
        "Thunder Wave": {
            "power": 20, "type": "Electric", "stab": 1,
            "super_effective": [], "not_very_effective": ["Electric", "Ground"],
            "accuracy": 90
        },
        "Dragon Rage": {
            "power": 40, "type": "Dragon", "stab": 1.5,
            "super_effective": ["Dragon"], "not_very_effective": ["Steel"],
            "accuracy": 100
        }
    }),
    Pokemon("Dragonite", ["Dragon", "Flying"], 166, 155, 115, 100, {
        "Dragon Claw": {
            "power": 80, "type": "Dragon", "stab": 1.5,
            "super_effective": ["Dragon"], "not_very_effective": ["Steel"],
            "accuracy": 100
        },
        "Thunder Wave": {
            "power": 20, "type": "Electric", "stab": 1,
            "super_effective": [], "not_very_effective": ["Electric", "Ground"],
            "accuracy": 90
        },
        "Fire Punch": {
            "power": 75, "type": "Fire", "stab": 1,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Hurricane": {
            "power": 110, "type": "Flying", "stab": 1.5,
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Steel", "Rock"],
            "accuracy": 70
        }
    }),
    Pokemon("Mewtwo", ["Psychic"], 181, 130, 110, 150, {
        "Psystrike": {
            "power": 100, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Aura Sphere": {
            "power": 80, "type": "Fighting", "stab": 1,
            "super_effective": ["Normal", "Rock", "Steel", "Ice", "Dark"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "accuracy": 100
        },
        "Ice Beam": {
            "power": 90, "type": "Ice", "stab": 1,
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"],
            "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "accuracy": 100
        },
        "Thunderbolt": {
            "power": 90, "type": "Electric", "stab": 1,
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "accuracy": 100
        }
    }),
    Pokemon("Mew", ["Psychic"], 175, 120, 120, 120, {
        "Psychic": {
            "power": 90, "type": "Psychic", "stab": 1.5,
            "super_effective": ["Poison", "Fighting"],
            "not_very_effective": ["Psychic", "Steel"],
            "accuracy": 100
        },
        "Flamethrower": {
            "power": 90, "type": "Fire", "stab": 1,
            "super_effective": ["Bug", "Steel", "Grass", "Ice"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "accuracy": 100
        },
        "Earthquake": {
            "power": 100, "type": "Ground", "stab": 1,
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug", "Flying"],
            "accuracy": 100
        },
        "Shadow Ball": {
            "power": 80, "type": "Ghost", "stab": 1,
            "super_effective": ["Ghost", "Psychic"],
            "not_very_effective": ["Dark", "Normal"],
            "accuracy": 100
        }
    })
]
