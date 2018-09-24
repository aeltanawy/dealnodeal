# import random
# import enum


class DNDApp:

    def __init__(self):
        self.finished_games = []
        self.player_list = []

    def run(self):
        """The actual game that keeps running till the player exits."""
        self.player_list = DNDPlayer.load_player_list()
        while True:
            player = self.choose_player()

            # FIXME
            game = DNDGame()
            game.play()
            result = game.did_win()
            player.record.append(result)
            if not keep_playing():
                return

    def choose_player(self):
        """Choose a player from a list or create a new one."""
        #import pdb; pdb.set_trace()
        i = -1
        for i, value in enumerate(self.player_list): # this will start i = 0
            print(f'{i+1}: {value.strip()}')

        #create a constant of i+2 then you don't have to repeat yourself typing numbers
        print(f'{i+2}: Create new')

        # TODO: validate the input values below
        player_num = int(input('Choose a number from the above list: '))
        if player_num == i+2:
            new_player_name = input('Enter a new player name: ')
            players.append(new_player_name)

        return self.player_list[player_num-1].strip()


class DNDPlayer:

    def load_player_list(): # static method working w/ global data, common for all instances
        with open('players_name.txt') as f:
            f.seek(0)
            names = f.readlines() #create a new list with stripped names, using list comprehension

        return names


if __name__ == '__main__':
    DNDPlayer.load_player_list()
    app = DNDApp()
    app.run()
