# import random
# import enum


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
        return

    def endingMoney(self):
        return 100


class DNDPlayer:

    def __init__(self, name, email=''):
        self.name = name
        self.record = []
        self.email_address = email



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
