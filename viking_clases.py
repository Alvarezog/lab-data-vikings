# Soldier
import random


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength   

    def attack(self):
        return self.strength
    
    def receive_damage(self, damage):
        self.health = self.health - damage
    
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return(f"{self.name} has received {damage} points of damage")
        elif self.health <= 0:
            return(f"{self.name} has died in act of combat")
      
    def battle_cry(self):
        return("Odin Owns You All!")

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return(f"A Saxon has received {damage} points of damage")
        elif self.health <= 0:
            return("A Saxon has died in combat")
    

# War


class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
            
    def add_viking(self, Viking):
        self.viking_army.append(Viking)
        
    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon)
        
    def viking_attack(self):
        attacked_saxon = random.choice(self.saxon_army)
        result = attacked_saxon.receive_damage(random.choice(self.viking_army).strength)
        if attacked_saxon.health <= 0:
            self.saxon_army.remove(attacked_saxon)
        else:
            pass
        return(result)
    
    def saxon_attack(self):
        attacked_viking = random.choice(self.viking_army)
        result = attacked_viking.receive_damage(random.choice(self.saxon_army).strength)
        if attacked_viking.health <= 0:
            self.viking_army.remove(attacked_viking)
        else:
            pass
        return(result)
    
    def show_status(self):
        if len(self.saxon_army) == 0:
            return("Vikings have won the war of the century!")
        elif len(self.viking_army) == 0:
            return("Saxons have fought for their lives and survive another day...")
        else:
            return("Vikings and Saxons are still in the thick of battle.")
    
