from random import randint


class Player:
    def __init__(self) -> None:
        self.pick_a_weapon()

    def pick_a_weapon(self):
        weapon_choice = randint(0,4)
        if weapon_choice == 0:
            print('player picked Rock')
        elif weapon_choice == 1:
            print('player picked Paper')
        elif weapon_choice == 2:
            print('player picked Scissors')
        elif weapon_choice == 3:
            print('player picked Lizzard')
        elif weapon_choice == 4:
            print('player picked Spock')
