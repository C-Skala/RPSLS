from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.set_name()

    def pick_a_weapon(self):
        self.chosen_gesture = input('please select a number. \n1-Rock\n2-Paper\n3-Scissors\n4-Lizzard\n5-Spock')
        if self.chosen_gesture == 1:
            self.chosen_gesture == 'Rock'
            print('player picked Rock')
        elif self.chosen_gesture == 2:
            self.chosen_gesture == 'Paper'
            print('player picked Paper')
        elif self.chosen_gesture == 3:
            self.chosen_gesture == 'Scissors'
            print('player picked Scissors')
        elif self.chosen_gesture == 4:
            self.chosen_gesture == 'Lizzard'
            print('player picked Lizzard')
        elif self.chosen_gesture == 5:
            self.chosen_gesture == 'Spock'
            print('player picked Spock')

    def set_name(self):
        self.name = input("Please enter your name?: ")
        