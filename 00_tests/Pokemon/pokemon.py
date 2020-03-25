### CLASS DECLARATION

class Trainer:
    def __init__(self, name, nb_potions):
        self.name = name
        self.nb_potions = nb_potions
        self.pokelist = []
        self.active = 0

    def __repr__(self):
        return ("{} {}".format(self.name, self.show_pokelist()))

    def set_active_pokemon(self):
        list_index = [ i for i in range(len(self.pokelist))]
        print("Setting active Pokemon for Trainer {}.\n".format(self.name))
        for index in list_index:
            print("Press {} for {} ({})".format(index, self.pokelist[index].name, self.pokelist[index].knocked_out))
        user_choice = int(input("\nActive Pokemon choice: "))
        if user_choice in list_index:
            if self.pokelist[user_choice].knocked_out == "Alive":
                self.active = self.pokelist[user_choice]
                print("")
                return
            else:
                print("Please choose an alive Pokemon!")
                self.set_active_pokemon()
        else:
            print("Choice not in the list, please try again.")
            self.set_active_pokemon()

    def add_pokelist(self, new_pokemon):
        if len(self.pokelist) <= 6:
            self.pokelist.append(new_pokemon)
            new_pokemon.owner = self
            print("Add {} to {} Pokedex.\n".format(new_pokemon.name, self.name))
        else:
            print("Pokedex Already Full")
            return

    def remove_pokelist(self, remove_pokemon):
        self.pokelist.remove(remove_pokemon)
        remove_pokemon.owner = None
        print("Remove {} from {} Pokedex.\n".format(remove_pokemon.name, self.name))

    def transfer_pokemon(self, pokemon, target_trainer):
        if pokemon.owner == self:
           if self.active != pokemon:
                print("{} transfers {} to {}.\n".format(self.name, pokemon.name, target_trainer.name))
                self.remove_pokelist(pokemon)
                target_trainer.add_pokelist(pokemon)
                pokemon.owner = target_trainer
           else:
               user_choice = input ("Can't transfer! {} is your active Pokemon. Do you want to set another active Pokemon? y/n: ".format(pokemon.name))
               if user_choice.lower() == "y":
                   self.set_active_pokemon()
                   self.transfer_pokemon(pokemon, target_trainer)
               else:
                   return
        else:
            print("Can't transfer! You don't owned this pokemon, {} is owned by {}.\n".format(pokemon.name, pokemon.owner.name))
            return
        
    def show_pokelist(self):
        if len(self.pokelist) > 0:
            print("{} Pokedex has:".format(self.name))
            for pokemon in self.pokelist:
                print("{} (Level {}) - {} - {}/10 XP".format(pokemon.name, pokemon.level, pokemon.knocked_out, pokemon.experience))
        else:
            return "has no Pokemon yet!\n"

    def use_potion(self):
        if self.nb_potions > 0:
            self.nb_potions -= 1
            self.active.restore_health(50)

    def attack_trainer(self, target_trainer):
        if (self.active != 0) and (target_trainer.active != 0):
            if self.active.knocked_out == "Alive":
                print("{} use {} to attack {} defends with {}!\n".format(self.name, self.active.name, target_trainer.name, target_trainer.active.name))
                self.active.attack(target_trainer.active)
            else:
                self.set_active_pokemon()
                self.active.attack(target_trainer.active)
        else:
            print("Please set active Pokemon for trainers")
            self.set_active_pokemon()

class Pokemon:

    unique_id = 0

    evolution = {"Squirtle": ["Squirtle", "Wartortle", "Blastoise"], 
             "Charmander": ["Charmander", "Charmeleon", "Charizard"],
             "Bulbasaur": ["Bulbasaur", "Ivysaur", "Venusaur"], 
             "Pidgey": ["Pidgey", "Pidgeotto", "Pidgeot"]}

    def set_name(self):
        if self.family in self.evolution.keys():
            if self.level < 5:
                self.name = self.evolution[self.family][0]
            elif self.level < 10:
                self.name = self.evolution[self.family][1]
            elif self.level >= 10:
                self.name = self.evolution[self.family][2]
        else:
            return

    def __init__(self, name, level, type, health, knocked_out, owner=None):
        self.id = name + str(self.unique_id)
        self.family = name
        self.level = level
        self.experience = 0
        self.set_name()
        self.type = type
        self.health = health
        self.maximum_health = self.level * self.health
        self.owner = owner
        if knocked_out == True:
            self.knocked_out = "Dead"
        else:
            self.knocked_out = "Alive"
        Pokemon.unique_id += 1

    def __repr__(self):
        return ("Pokemon {} - Level {} - Type {} - HP: {}, MaxHP: {}, {}\n".format(self.name, self.level, self.type, self.health, self.maximum_health, self.knocked_out))

    def is_alive(self):
        return self.knocked_out == "Alive"

    def is_target_alive(self, target):
        return target.knocked_out == "Alive"

    def level_up(self):
        if self.is_alive():
            self.level += 1
            self.maximum_health = self.level * self.health
            check_name = self.name
            self.set_name()
            if check_name != self.name:
                print("Hurray! {} has now evolve into a {} and is now on level {}!\n".format(check_name, self.name, self.level))
            else:
                print("Level Up ! {} is now on level {}.\n".format(self.name, self.level))
        else:
            print("Can't level up, {} is dead".format(self.name))

    def get_level(self):
        print("{} is level: {}.\n".format(self.name, self.level))
        return self.level

    def get_id(self):
        print("{} (ID: {}.)\n".format(self.name, self.id))
        return self.id

    def get_status(self):
        print("{} is {}.\n".format(self.name, self.knocked_out))
        return self.knocked_out

    def knock_out(self):
        if self.is_alive():
            print("Oh no! {} is Dead.".format(self.name))
            self.knocked_out = "Dead"
            self.health = 0
        else:
            print("{} is already dead.\n".format(self.name))

    def revive(self):
        if not self.is_alive():
            self.knocked_out = "Alive"
            self.health = self.maximum_health // 2
            print("Reviving {} with {} HPs!\n".format(self.name, self.health))
        else:
            print("Can't revive {}. Already alive!".format(self.name))

    def lose_health(self, lost_hp):
        if self.is_alive():
            self.health -= lost_hp
            if self.health > 0:
                print("{} losts {} HPs.\n{} now has {}/{} HPs.\n".format(self.name, lost_hp, self.name, self.health, self.maximum_health))
            elif self.health <= 0:
                self.knock_out()
        else:
            print("Can't lose HPs, {} is already dead.".format(self.name))
        
    def restore_health(self, restore_hp):
        if self.is_alive():
            self.health += restore_hp
            if self.health > self.maximum_health:
                self.health = self.maximum_health
            print("{} heals {} HPs.\n{} now has {}/{} HPs.\n".format(self.name, restore_hp, self.name, self.health, self.maximum_health))
        else:
            print("Can't heal, {} is dead".format(self.name))

    def damage_boost(self, target):
        if self.type == "Fire" and target.type == "Grass":
            boost = 2 * self.level
            return boost
        elif self.type == "Fire" and target.type == "Water":
            boost = 0.5 * self.level
            return boost
        elif self.type == "Water" and target.type == "Fire":
            boost = 2 * self.level
            return boost
        elif self.type == "Water" and target.type == "Grass":
            boost = 0.5 * self.level
            return boost
        elif self.type == "Grass" and target.type == "Fire":
            boost = 0.5 * self.level
            return boost
        elif self.type == "Grass" and target.type == "Water":
            boost = 2 * self.level
            return boost
        else:
            return self.level

    def attack(self, target, sustain=False):
        if self.is_alive():
            if self.is_target_alive(target):
                damage = self.damage_boost(target) * self.level * 5
                print("{} attacks {} and deal {} damage (boost x{})".format(self.name, target.name, damage, self.damage_boost(target)))
                target.lose_health(damage)
                if sustain:
                    print("Sustain!")
                    self.restore_health(damage * 0.25)
                if not self.is_target_alive(target):
                    self.check_xp(target)
            else:
                print("Can't attack target {} is already dead.\n".format(target.name))
        else:
            print("Can't attack your active Pokemon is dead...\n".format(self.name))
            return 

    def check_xp(self, target):
        if self.level == target.level:
            xp = self.add_experience(8)
        elif self.level >= target.level:
            xp = self.add_experience(5)
        else:
            xp = self.add_experience(10)
        if xp :
            print("{} earned {}XP from his fight with {}.\n".format(self.name, xp, target.name))
            return xp
        else:
            return
        
    def add_experience(self, xp):
        if self.is_alive():
            self.experience += xp
            if self.experience >= 10:
                self.level_up()
                rest = self.experience - 10
                self.experience = 0 + rest
            return xp
        else:
            print("Can't XP, {} is dead".format(self.name))
            return


### CLASS INSTANTIATION & CALLS

## TRAINERS
antoine = Trainer("Antoine", 3)
bastien = Trainer("Bastien", 3)

## POKEMONS
squirtle = Pokemon("Squirtle", 2, "Water", 50, False)
charmander = Pokemon("Charmander", 2, "Fire", 50, False)
bulbasaur = Pokemon("Bulbasaur", 3, "Fire", 50, False)
pidgey = Pokemon("Pidgey", 2, "Fire", 50, False)

#squirtle.level_up()
#squirtle.level_up()

## ADD POKEDEX
antoine.add_pokelist(squirtle)
antoine.add_pokelist(charmander)
bastien.add_pokelist(bulbasaur)
bastien.add_pokelist(pidgey)

### SET ACTIVE POKEMON
antoine.set_active_pokemon()
bastien.set_active_pokemon()

### TRAINER ATTACK
antoine.attack_trainer(bastien)
antoine.attack_trainer(bastien)
antoine.attack_trainer(bastien)
#bastien.attack_trainer(antoine)

### SHOW POKEMON
antoine.show_pokelist()

### TRAINER HEAL
#antoine.use_potion()
#bastien.use_potion()

### TRANSFER POKEMON
#antoine.transfer_pokemon(bulbasaur, bastien)
#antoine.transfer_pokemon(charmander, bastien)
#antoine.transfer_pokemon(squirtle, bastien)

#### LEVEL UP 
#print(pidgey)

#pidgey.level_up()
#pidgey.level_up()
#pidgey.level_up()
#pidgey.level_up()
#pidgey.level_up()
#pidgey.level_up()
#pidgey.level_up()
#pidgey.level_up()
#pidgey.level_up()
#pidgey.level_up()
#print(pidgey)
