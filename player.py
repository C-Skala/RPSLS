from random import randint


class Player:
    def __init__(self) -> None:
        self.chosen_gesture = ""
        self.gestures = ["Rock", "Paper", "Scissors", "Lizzard", "Spock"]
        self.wins = 0
        

    def pick_a_weapon(self):
        number_picked   = randint(0,4)
        if number_picked == 0:
            self.chosen_gesture = 'Rock'
            print('player picked Rock')
        elif number_picked== 1:
            self.chosen_gesture = 'Paper'
            print('player picked Paper')
        elif number_picked == 2:
            self.chosen_gesture = 'Scissors'
            print('player picked Scissors')
        elif number_picked == 3:
            self.chosen_gesture = 'Lizzard'
            print('player picked Lizzard')
        elif number_picked == 4:
            self.chosen_gesture = 'Spock'
            print('player picked Spock')
