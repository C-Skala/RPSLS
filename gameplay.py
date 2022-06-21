class Gameplay:

    def __init__(self) -> None:
        pass

    def war_of_the_hands(self):
        Gameplay.welcome_and_rules
        Gameplay.player_setup


    def welcome_and_rules(self):
        print('welcome to the hardened world where the fastest hand wins')
        print('the rules are simple, pick a number corelated to one of our weapons and hope it is stronger than your oponent')
        print('the weapons and how they compaire are as follows:')
        print("")
        print("")
        print("")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard Poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("")
        print("")
        print("to ensure this war doesnt wage on for eternity a winner will be declaired after three superior weapon picks")

    def player_setup(self):
        players = input('First lets see who will wage this war!\n1-man vs. computer\n2-man vs.man\n3-computer vs computer\nplease select 1, 2, or 3: ')
