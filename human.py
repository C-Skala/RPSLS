from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.set_name()

    def pick_a_weapon(self):
        weapon_picked = False
        while weapon_picked == False:
            self.chosen_gesture = input('please select a number. \n1-Rock\n2-Paper\n3-Scissors\n4-Lizzard\n5-Spock\n1,2,3,4,5: ')
            if self.chosen_gesture == '1':
                self.chosen_gesture = 'Rock'
                print(f'{self.name} picked Rock')
                weapon_picked = True
            elif self.chosen_gesture == '2':
                self.chosen_gesture = 'Paper'
                print(f'{self.name} picked Paper')
                weapon_picked = True
            elif self.chosen_gesture == '3':
                self.chosen_gesture = 'Scissors'
                print(f'{self.name} picked Scissors')
                weapon_picked = True
            elif self.chosen_gesture == '4':
                self.chosen_gesture = 'Lizzard'
                print(f'{self.name} picked Lizzard')
                weapon_picked = True
            elif self.chosen_gesture == '5':
                self.chosen_gesture = 'Spock'
                print(f'{self.name} picked Spock')
                weapon_picked = True
            else:
                print('please select a number from the list')

    def set_name(self):
        self.name = input("Please enter your name?: ")
        