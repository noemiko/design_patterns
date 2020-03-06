# We use the Builder pattern when we know that an object must be created in multiple
# steps, and different representations of the same construction are required. These
# requirements exist in many applications such as page generators

class GameWorld():
    def __init__(self, game_name):
        self.game_name = game_name
        self.hero_name = None

    def __str__(self):
        return self.game_name

    def load_hero(self, hero_name):
        print(f"Loading {hero_name}")


class WizardGameWorldBuilder():
    def __init__(self):
        self.game_world = GameWorld("Wizard 2000")
        self.game_time = 700  # sec
        self.number_of_enemies = 8

    def prepare_background(self):
        print("Setup dark background")

    def prepare_enemies(self):
        print(f"Adding {self.number_of_enemies} bad witchers")

    def setup_sound(self):
        print("Trurumpupum")

    def load_hero(self):
        hero_name = "Henryk The Wizard"
        self.game_world.load_hero(hero_name)


class FrogGameWorldBuilder():
    def __init__(self):
        self.game_world = GameWorld("Frog 2000")
        self.game_time = 500  # sec
        self.number_of_enemies = 8

    def prepare_background(self):
        print("Setup green background")

    def prepare_enemies(self):
        print(f"Adding {self.number_of_enemies} bad stork")

    def setup_sound(self):
        print("Cwir cwir")

    def load_hero(self):
        hero_name = "Henryk The Frog"
        self.game_world.load_hero(hero_name)


class GameMaster():
    def __init__(self):
        self.builder = None

    def construct_game(self, builder):
        self.builder = builder
        steps = (builder.prepare_background,
                 builder.prepare_enemies,
                 builder.setup_sound,
                 builder.load_hero)
        [step() for step in steps]

    def game(self):
        return self.builder.game_world


def validate_game(builders):
    try:
        input_msg = 'What game would you like, [w]izard or [f]rog ? '
        chosen_game = input(input_msg)
        builder = builders[chosen_game]()
    except KeyError:
        error_msg = 'Sorry, only wizard (key w) and frog (key f) are available'
        print(error_msg)
        return (False, None)
    return (True, builder)


def main():
    builders = dict(w=WizardGameWorldBuilder, f=FrogGameWorldBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_game(builders)
    print()
    waiter = GameMaster()
    waiter.construct_game(builder)
    game = waiter.game()
    print()
    print(f'Enjoy your {game}!')


if __name__ == '__main__':
    main()
