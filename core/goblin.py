from core.monster import Monster
import random


class Goblin(Monster):
    def __init__(self):
        super().__init__(
            name="Goblin",
            hp=20,
            type="goblin",
            speed=random.randint(5,10),
            power =random.randint(5,10),
            rating_armor=1
            )
        
        
    def attack(self, player):
       super().attack(player)
       if player.hp < player.hp / 2:
          arr_run_away = [True for _ in range(3)] + [False for _ in range(7)]
          res = random.choice(arr_run_away)
          if res:
               self.run_away()
           
           
    def run_away(self):
         print(f"{self.name} is running away!")      