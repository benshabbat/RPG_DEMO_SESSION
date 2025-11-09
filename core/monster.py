import random
from core.utils import dice_roll

WEAPONS=["axe","sword","knife"]



class Monster:
    def __init__(self,name,hp,speed,power,rating_armor,type):
        self.name=name
        self.hp=hp
        self.speed=speed
        self.power=power
        self.rating_armor=rating_armor
        self.type=type
        self.weapon=random.choice(WEAPONS)
        
    def speak(self):
        print(f"{self.name} {self.type}")
    
    def attack(self,player):
        
        if self.weapon == "axe":
            self.power *=1.5
        elif self.weapon == "knife":
            self.speed *=0.5  
              
        if dice_roll(20)+self.speed > player.rating_armor:
            
            player.hp -=(self.power +dice_roll(6))
            
            print(f"{self.name} attacked {player.name}")
        else:    
            print(f"{self.name} missed {player.name}")
       

 
