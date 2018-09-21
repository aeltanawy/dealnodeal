# import numpy as np
import pandas as pd
# import pathlib
import random


class DondGame:

    def __init__(self, name, chosen_box):
        '''
        To iniitalize NewGame class instance.
        '''
        self.name = name
        self.played = ''
        self.player_box = int(chosen_box)
        #self.open_box = 0, no need to keep track of this
        #self.turns_left_into_offer = 5, compute this from the box df info
        self.win = False
        self.deal = False
        self.box_df = self.box_assignment()


    def box_assignment(self):
        '''
        Creates a DataFrame hosting the boxes informaion. Assigns values randomly to each box and returns the boxes DataFrame.
        '''
        box_value= [0.01,0.10,0.50,1.00,5.00,10.00,50.00,100.00,250.00,500.00,750.00,1000.00,3000.00,5000.00,10000.00,15000.00,20000.00,35000.00,50000.00,75000.00,100000.00,250000.00]
        random.shuffle(box_value)
        df = pd.DataFrame({'state': 'closed', 'value': box_value},
            index=range(1,23))
        box_df = df.rename_axis("box", axis="columns")
        return box_df

    def box_update(self, num, state):
        '''
        This method changes the state value of the chosen box in the DataFrame.
        '''
        self.box_df.loc[num, 'state'] = state

    def box_to_print(self):
        '''
        Slice the box DataFrame to contain everything but the value column, and returns it.
        '''
        self.box_to_print = self.box_df.loc[:, self.box_df.columns != 'value']
        return self.box_to_print


def main():
    #end_game = False
    #while not end_game:
    welcome_msg(
    name = input('Enter your name: ').capitalize()
    while True:
        try:
            chosen_box = int(input('Choose a box number from 1 to 22: '))
        except ValueError:
            print(error_message(type=True, value='integer'))
            continue
        if chosen_box in range(1, 23):
            break
        print(error_message(between=True, first=1, last=22))

    g = NewGame(name, chosen_box)
    g.box_update(chosen_box, '--chosen')
    print(f'\n{g.box_to_print()}')
    menu()

def error_message(between=False, first=0, last=0, type=False, value=0):
    '''
    This method hosts the error messages of the game and returns the correct meddage to display.
    '''
    if between:
        msg = f"\nThe value you typed is not between '{first}' and '{last}'!\nPlease enter the correct value.\n"
    elif type:
        msg = f"\nThe value you typed is not of type '{value}'!\nPlease enter the correct value.\n"

    return msg

def welcome_msg():
    '''
    To print a welcome message at the start of the game.
    '''
    game_name = 'DEAL OR NO DEAL'
    print('\n|' + '-' * 5 + '-' * (len(game_name) + 2) + '-' * 5 + '|')
    print('|' + "-" * 5 + f' {game_name} ' + '-' * 5 + '|')
    print('|' + '-' * 5 + '-' * (len(game_name) + 2) + '-' * 5 + '|\n')

def menu():
    '''
    To print the game menu.
    '''
    print('\nMenu: (1) Play | (2) New | (3) Analysis | (9) Exit\n')

main()
