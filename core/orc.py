from core.monster import Monster
import random



class Orc(Monster):
    def __init__(self):
        super().__init__(
            name="Orc",
            hp=50,
            type="orc",
            speed=random.randint(0,5),
            power =random.randint(10,15),
            rating_armor=random.randint(0,5),
            )
        