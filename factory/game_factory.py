# Abstract Factory
# The Abstract Factory design pattern is a generalization of Factory Method. Basically,
# an Abstract Factory is a (logical) group of Factory Methods, where each Factory
# Method is responsible for generating a different kind of object


# Frog game

class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}!"
        print(msg)


class Bug:
    def __str__(self):
        return "a bug"

    def action(self):
        return "eats it"


class FrogGame:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t------ Frog World -------"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


# Wizard game

class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Wizard battles against {obstacle} and {act}!"
        print(msg)


class Ork:
    def __str__(self):
        return "an evil ork"

    def action(self):
        return "kills it"


class WizardGame:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t------ Wizard World -------"

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


# Game environment
class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_chosen_game(user_name):
    print(f"Would you like to play {user_name} in Wizard game?")
    print(f"Would you like to play {user_name} in Frog game?")
    game_number = input("Wizard game press: 1, From game press: 2 ")
    try:
        game_number = int(game_number)
        if game_number not in (1, 2):
            raise ValueError
    except ValueError as err:
        print("You have chosen the wrong game number")
        return False, game_number
    return True, game_number


def main():
    user_name = input("Hello. What's your name? ")
    is_valid_input = False
    while not is_valid_input:
        is_valid_input, game_number = validate_chosen_game(user_name)
    games = {
        1: FrogGame,
        2: WizardGame
    }
    chosen_game = games[game_number]
    environment = GameEnvironment(chosen_game(user_name))
    environment.play()


main()
