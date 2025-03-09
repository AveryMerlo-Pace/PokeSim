import random
import time
print("")

POKE_LEVEL = 50

class Pokemon:
    def __init__(self, name, poketype, hp, atk, defn, spd, moves=None):
        self.name = name
        self.poketype = poketype
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.spd = spd
        self.moves = moves if moves else {}
    
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
    
    def describeMoveset(self):
        moveSet = [f"{self.name.upper()}'s moves are:"]
        count = 1
        for i in self.moves.keys():
            moveSet.append(f"{count}. {i} (POWER: {self.moves[i]["power"]}, TYPE: {self.moves[i]["type"]})")
            count = count + 1
        return moveSet
    
    def pokemonAttack(self, opp_pokemon):
        return ""
    