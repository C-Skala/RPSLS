from random import randint


class Player:
    def __init__(self) -> None:
        self.chosen_gesture = ""
        self.gestures = ["Rock", "Paper", "Scissors", "Lizzard", "Spock"]
        self.wins = 0
        # self.pick_a_weapon()

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
