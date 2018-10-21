import random
from enum import Enum


class DNDApp:

    def __init__(self):
        self.finished_games = []
        self.player_list = []

    def run(self):
        """The actual game that keeps running till the player exits."""
        self.player_list = load_player_list()
        while True:
            player = self.choose_player()

            # FIXME
            game = DNDGame()
            game.play()
            result = game.endingMoney()
            player.record.append(result)

            if not self.keep_playing():
                return

    def choose_player(self):
        """Choose a player from a list or create a new one."""
        #import pdb; pdb.set_trace()
        i = -1
        for i, player in enumerate(self.player_list):
            print(f'{i+1}: {player.name} (${sum(player.record)})')

        CREATE_NEW = i+2
        print(f'{CREATE_NEW}: Create new')

        # TODO: validate the input values below
        player_num = int(input('Choose a number from the above list: '))
        if player_num == CREATE_NEW:
            new_player_name = input('Enter a new player name: ')
            new_player = DNDPlayer(new_player_name)
            self.player_list.append(new_player)

        return self.player_list[player_num-1]

    def keep_playing(self):
        return True


class DNDGame:
    def play(self):

        # Setup the 22 boxes for the current game.
        self.boxes = DNDBox.setup_boxes()

        # Choose a box number to keep at the begining of the game.
        self.choose_player_box()

        # Start of game loop
        end_game = False
        while not end_game:
            self.show_boxes_and_menu()


        return

    def show_boxes_and_menu(self):
        # To show boxes dict and game menu.
        print('\n'.join(f'{k}: {v[1]}' for k, v in self.boxes.items()))

        print('\nMenu:', end=" ")
        for i in Menu:
            print('f({i.value}) {i.name}', end=" | ")


    def endingMoney(self):
        return 100

    def choose_player_box(self):
        player_box_num = int(input('Choose a box number from 1 to 22 to keep: '))
        player_box_state = BoxState(2).name

        DNDBox.update_box_state(player_box_num, player_box_state)


class DNDPlayer:

    def __init__(self, name, email=''):
        self.name = name
        self.record = []
        self.email_address = email

class DNDBox:

    def update_box_state(self, num, state):
        DNDGame.boxes[num][1] = state

    def shuffle_box_values(self):
        # shuffle values between 0.01 and 25000 randomly in a list and returns that list.
        values = [0.01,0.10,0.50,1.00,5.00,10.00,50.00,100.00,250.00,50.000,750.00,1000.00,3000.00,5000.00,10000.00,15000.00,20000.00,35000.00,50000.00,75000.00,100000.00,250000.00]
        box_values = random.shuffle(values)

        return box_values

    def setup_boxes(self):
        # assign 'closed' state and values to each box. Returns a dict with the boxes value and state.
        boxes = {}
        box_state = BoxState(0).name
        values = self.shuffle_box_values()
        for index in range(22):
            box_num = index+1
            box_value = values[index]
            boxes[box_num] = [box_value, box_state]

        return boxes

class BoxState(Enum):
    CLOSED = 0
    OPENED = 1
    PLAYER_BOX = 2


class Menu(Enum):
    EXIT = 0
    PLAY = 1
    NEW = 2
    ANALYSIS = 3


def load_player_list(): # static method working w/ global data, common for all instances
    with open('players_name.txt') as f:
        f.seek(0)
        names = f.readlines()
    player_list = []
    for name in names:
        name = name.strip()
        p = DNDPlayer(name)
        player_list.append(p)
    return player_list


if __name__ == '__main__':
    #DNDPlayer.load_player_list()
    app = DNDApp()
    app.run()
