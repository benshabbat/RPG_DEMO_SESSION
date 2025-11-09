from core.player import Player
from core.orc import Orc
from core.goblin import Goblin
from core.monster import Monster
from core.utils import dice_roll
import random



class Game:
    
    def start(self):
        self.show_menu()
        
        
    def show_menu(self):
        menu = "1.start Game\n2.Exit\n"
        res = "0"
        while res != "1" and res != "2":
            res = input(menu)
        if res == "1":
            self.battle(self.create_player(),self.monster_random_choose())
        else:
            exit()
        return res 
    
      
    @staticmethod
    def create_player():
        return Player()
    
    @staticmethod
    def monster_random_choose():
        return random.choice([Orc(),Goblin()])
        
    
    def battle(self,player:Player,monster:Monster):

        
        dice_player = dice_roll(6)+player.speed
        dice_monster = dice_roll(6)+monster.speed
        
        if dice_player>= dice_monster:
            player.attack(monster)
            player.turn = False
            monster.turn = True
           
        else:
            monster.attack(player)    
            monster.turn = False
            player.turn = True
        
        while player.hp >0 and monster.hp >0:
            if player.turn:
                player.attack(monster)
                player.turn = False
                monster.turn = True
            else:
                monster.attack(player)    
                monster.turn = False
                player.turn = True
        
        
        
    
    @staticmethod   
    def dice_roll(sides):
        return dice_roll(sides)
    
