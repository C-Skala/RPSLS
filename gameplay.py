from time import sleep, time
from human import Human
from ai import Ai


class Gameplay:

    def __init__(self) -> None:
        self.player_one = None
        self.player_two = None

    def war_of_the_hands(self):
        self.welcome_and_rules()
        self.player_setup()
        self.gameplay()
        self.winner()


    def welcome_and_rules(self):
        print('welcome to the hardened world where the fastest hand wins')
        print('the rules are simple, pick a number corelated to one of our weapons and hope it is stronger than your oponent')
        print('the weapons and how they compaire are as follows:')
        print("")
        print("")
        print("")
        sleep(1)
        print("Rock crushes Scissors")
        sleep(1)
        print("Scissors cuts Paper")
        sleep(1)
        print("Paper covers Rock")
        sleep(1)
        print("Rock crushes Lizard")
        sleep(1)
        print("Lizard Poisons Spock")
        sleep(1)
        print("Spock smashes Scissors")
        sleep(1)
        print("Scissors decapitates Lizard")
        sleep(1)
        print("Lizard eats Paper")
        sleep(1)
        print("Paper disproves Spock")
        sleep(1)
        print("Spock vaporizes Rock")
        sleep(1)
        print("")
        print("")
        print("to ensure this war doesnt wage on for eternity a winner will be declaired after two superior weapon picks")

    def player_setup(self):
        player_picked = False
        while player_picked == False:
            players = input('First lets see who will wage this war!\n1-man vs. computer\n2-man vs.man\n3-computer vs computer\nplease select 1, 2, or 3: ')
            if players == "1":
                self.player_one = Human()
                self.player_two = Ai('Ultron')
                sleep(1)
                print("")
                print('man vs computer, a tale as old as 1943')
                print("")
                player_picked = True
            elif players == '2':
                self.player_one = Human()
                self.player_two = Human()
                sleep(1)
                print("")
                print('man vs man huh? going old school this time I see')
                print("")
                player_picked = True
            elif players == "3":
                self.player_one = Ai('Ultron')
                self.player_two = Ai('Skynet')
                sleep(1)
                print("")
                print('computer vs. computer..... BATTLE BOTS!!')
                print("")
                player_picked = True
            else:
                print("")
                print('please select either 1, 2, or 3')
                print("")
                player_picked = False


    def gameplay(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one.pick_a_weapon()
            self.player_two.pick_a_weapon()
            if self.player_one.chosen_gesture == 'Rock':
                if self.player_two.chosen_gesture == 'Rock':
                    print("")
                    print('When the hands match no battle is won or lost, a stalemate occurs no points awarded')
                    print("")
                elif self.player_two.chosen_gesture == 'Scissors':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} crushed {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Lizzard':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} crushed {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Paper':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is incapacitated by {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Spock':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is vaporized by {self.player_two.name}')
                    print("")
            if self.player_one.chosen_gesture == 'Scissors':
                if self.player_two.chosen_gesture == 'Scissors':
                    print("")
                    print('When the hands match no battle is won or lost, a stalemate occurs no points awarded')
                    print("")
                elif self.player_two.chosen_gesture == 'Paper':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} cut {self.player_two.name} to pieces')
                    print("")
                elif self.player_two.chosen_gesture == 'Lizzard':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} decapitated {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Rock':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is smashed by {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Spock':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is smashed by {self.player_two.name}')
                    print("")
            if self.player_one.chosen_gesture == 'Paper':
                if self.player_two.chosen_gesture == 'Paper':
                    print("")
                    print('When the hands match no battle is won or lost, a stalemate occurs no points awarded')
                    print("")
                elif self.player_two.chosen_gesture == 'Rock':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} incapacitated {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Spock':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} Proved {self.player_two.name} wrong')
                    print("")
                elif self.player_two.chosen_gesture == 'Scissors':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is cut into millions of pieces by {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Lizzard':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is eaten by {self.player_two.name}')
                    print("")
            if self.player_one.chosen_gesture == 'Lizzard':
                if self.player_two.chosen_gesture == 'Lizzard':
                    print("")
                    print('When the hands match no battle is won or lost, a stalemate occurs no points awarded')
                    print("")
                elif self.player_two.chosen_gesture == 'Spock':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} Poisened {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Paper':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} eats {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Rock':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is Crushed by {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Scissors':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is decapitated by {self.player_two.name}')
                    print("")
            if self.player_one.chosen_gesture == 'Spock':
                if self.player_two.chosen_gesture == 'Spock':
                    print("")
                    print('When the hands match no battle is won or lost, a stalemate occurs no points awarded')
                    print("")
                elif self.player_two.chosen_gesture == 'Rock':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} Vaporizes {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Scissors':
                    self.player_one.wins += 1
                    print("")
                    print(f'{self.player_one.name} crushes {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Paper':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is disproved by {self.player_two.name}')
                    print("")
                elif self.player_two.chosen_gesture == 'Lizzard':
                    self.player_two.wins += 1
                    print("")
                    print(f'{self.player_one.name} is Poisoned by {self.player_two.name}')
                    print("")

    def winner(self):
        if self.player_one.wins ==2:
            print(f'congrats {self.player_one.name} you are the tactical winner!')
        if self.player_two.wins ==2:
            print(f'congrats {self.player_two.name} you are the tactical winner!')