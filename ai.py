from random import random
from player import Player

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.name = random.choice['Ultron', 'Skynet', 'Hal 2000']
        