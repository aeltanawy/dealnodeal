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
    #PLAYER_BOX = None
    #boxes = {}

    def play(self):
        #import pdb; pdb.set_trace()
        # Setup the 22 boxes for the current game.
        self.game_boxes = DNDBoxCollection()

        # Choose a box number to keep at the begining of the game. Update the box state to 'PLAYER_BOX'.
        player_box_num = self.choose_player_box()
        self.game_boxes.setPlayerBox(player_box_num)

        # Start of game loop
        for i in range(4):
            self.playOneRound()
        return

    def playOneRound(self):
        for i in range(5):
            self.show_boxes_and_menu()
            while True:
                box_num = int(input('Choose a box to open'))
                if self.can_open_box(box_num):
                    break

        self.playBankersOffer()

    def playBankersOffer(self):
        pass

    def show_boxes_and_menu(self):
        # To show boxes dict and game menu.
        info = self.game_boxes.getBoxesInfo()
        for line in info:
            print(line)

        print('\nMenu:', end=" ")
        for i in Menu:
            print(f'({i.value}) {i.name}', end=" | ")
        print('\n')


    def endingMoney(self):
        return 100

    def choose_player_box(self):
        player_box_num = int(input('Choose a box number from 1 to 22 to keep: '))

        return player_box_num


class DNDPlayer:

    def __init__(self, name, email=''):
        self.name = name
        self.record = []
        self.email_address = email


class DNDBox:
    def __init__(self, number, value):
        self.number = number
        self.value = value
        self.state = BoxState.CLOSED


class DNDBoxCollection:

    def __init__(self):
        self._boxes = self.setup_boxes()

    def update_box_state(self, boxes, num, state):
        updated_boxes = boxes
        updated_boxes[num][1] = state
        return updated_boxes

    def get_shuffled_box_values(self):
        # shuffle values between 0.01 and 25000 randomly in a list and returns that list.
        #import pdb; pdb.set_trace()
        box_values = [0.01,0.10,0.50,1.00,5.00,10.00,50.00,100.00,250.00,50.000,750.00,1000.00,3000.00,5000.00,10000.00,15000.00,20000.00,35000.00,50000.00,75000.00,100000.00,250000.00]
        random.shuffle(box_values)

        return box_values

    def setup_boxes(self):
        # assign 'closed' state and values to each box. Returns a dict with the boxes value and state.
        boxes = []
        values = self.get_shuffled_box_values()
        for index, value in enumerate(values):
            box_num = index+1
            box = DNDBox(box_num, value)
            boxes.append(box)

        return boxes

    def getBoxByNumber(self, box_num):
        return self._boxes[box_num - 1]


    def setPlayerBox(self, box_num):
        box = self.getBoxByNumber(box_num)
        box.state = BoxState.PLAYER_BOX

    def getBoxesInfo(self):
        boxes_info=[]
        for box in self._boxes:
            boxes_info.append(f'{box.number}: {box.state.name}')
        return boxes_info



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
