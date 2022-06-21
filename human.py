from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.set_name()

    def pick_a_weapon(self):
        self.chosen_gesture = randint(0,4)
        if self.chosen_gesture == 0:
            print('player picked Rock')
        elif self.chosen_gesture == 1:
            print('player picked Paper')
        elif self.chosen_gesture == 2:
            print('player picked Scissors')
        elif self.chosen_gesture == 3:
            print('player picked Lizzard')
        elif self.chosen_gesture == 4:
            print('player picked Spock')

    def set_name(self):
        self.name = input("Please enter your name?: ")
        