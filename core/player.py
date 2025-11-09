from core.utils import dice_roll
import random

PROFESSIONS = ["healer","Fighter"]


class Player:
    def __init__(self,name="fighter",hp=50,speed=random.randint(5,10),power =random.randint(5,10),rating_armor=random.randint(5,15)):
        self.name=name
        self.hp=hp
        self.speed=speed
        self.power=power
        self.rating_armor=rating_armor
        self.profession=random.choice(PROFESSIONS)
      
      
        if self.profession == "healer":
            self.hp+=10 
        else:
            self.power+=2    
            
    def speak(self):
        print(self.name)

    def attack(self,monster):
        if dice_roll(20)+self.speed > monster.rating_armor:
            monster.hp -=self.power
            print(f"{self.name} attacked {monster.name}")
        else:    
            print(f"{self.name} missed {monster.name}")
       
        

 
