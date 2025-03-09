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
    
    def pokemonAttack(self, move, opp_defense, opp_type1, opp_type2):
        level = 50
        critical = 2 if random.randint(1, 10) == 5 else 1
        power = self.moves[move]["power"]
        a_d = self.atk / opp_defense
        stab = self.moves[move]["stab"]
        if opp_type1 in self.moves[move]["not_very_effective"]:
            type1 = 0.5
            print(f"{move} is not very effective against {opp_type1}...")
        elif opp_type1 in self.moves[move]["super_effective"]:
            type1 = 2
            print(f"{move} is super effective against {opp_type1}!")
        else:
            type1 = 1
        type2 = 1
        if opp_type2 != None:
            if opp_type2 in self.moves[move]["not_very_effective"]:
                type2 = 0.5
                print(f"{move} is not very effective against {opp_type2}...")
            elif opp_type2 in self.moves[move]["super_effective"]:
                type2 = 2
                print(f"{move} is super effective against {opp_type2}!")
            else:
                type2 = 1
        
        rando = float(random.randint(217, 255) / 255)
        
        damage = round((((2 * level * critical / + 2) * power * a_d) / 50 + 2) * stab * type1 * type2 * rando)
        return damage
    