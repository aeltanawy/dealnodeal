#import numpy as np
import pandas as pd
#import pathlib
import random

class GameSetup:
    '''Getting player name and assign random values to boxes.'''

    def __init__(self):
        self.player_name = ''
        #self.opened_boxes = 0
        self.player_box = 0
        self.end_game = False
        self.win = False
        self.deal = False
        self.box_df = box_assignment()

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

    def welcome_msg():
        '''
        To print a welcome message at the start of the game.
        '''
        game_name = 'DEAL OR NO DEAL'
        print('\n|' + '-' * 5 + '-' * (len(game_name) + 2) + '-' * 5 + '|')
        print('|' + "-" * 5 + f' {game_name} ' + '-' * 5 + '|')
        print('|' + '-' * 5 + '-' * (len(game_name) + 2) + '-' * 5 + '|\n')

    def player_name(self):
        self.player_name = input('Enter your name: ').capitalize()


class GamePlay:
    def game_main():
        #To choose the player box that is kept till the end at the begining of the game
        if GameSetup.opened_boxes == 0:
            try: # TODO-1: turn to a function with box_func as argument
                player_box = int(input('Choose a box number from 1 to 22: '))
            except ValueError:
                print(error_message(type=True, value='integer'))
                continue
            if player_box in range(1, 23):
                break
            print(error_message(between=True, first=1, last=22))
            GameSetup.player_box = int(player_box)
            box_update(player_box, '--chosen')

        print(f'\n{box_to_print()}')
        menu()

        #Main game loop. After player opens 5 boxes, comes the banker offer. Player decides deal or no deal
        for i in range(5):
            try: # TODO-1
                open_box = int(input('Choose a box number from 1 to 22: '))
            except ValueError:
                print(error_message(type=True, value='integer'))
                continue
            if open_box in range(1, 23):
                break
            print(error_message(between=True, first=1, last=22))
            remainaing_boxes()

            box_update(open_box, '--opened')

        #banker offer aftr openeing 5 boxes and if the player didn't accept the deal yet
        if not GameSetup.deal:
            GameSetup.deal = banker_offer()


    def validate_box(self, num):
        '''Evaluates the box number state'''


    def banker_offer(self):
        try: # TODO-1
            deal = input((f'Banker offers you for your chosen box: {offer}\nDeal (Y) or no Deal (N)? ').lower())
        except ValueError:
            print(error_message(type=True, value='"Y" or "N"'))
            continue
        if deal == 'y' or deal == 'n':
            if deal == 'y'
                return True
            else:
                return False
            break
        print(error_message(type=True, value='"Y" or "N"'))

    def box_to_print(self):
        '''
        Slice the box DataFrame to contain everything but the value column, and
        returns it.
        '''
        self.box_to_print = self.box_df.loc[:, self.box_df.columns != 'value']
        return self.box_to_print

    def box_update(self, num, state):
        '''
        This method changes the state value of the chosen box in the
        DataFrame.
        '''
        self.box_df.loc[num, 'state'] = state

    def error_message(between=False, first=0, last=0, type=False, value=0):
        '''
        This method hosts the error messages of the game and returns the
        correct meddage to display.
        '''
        if between:
            msg = f"\nThe value you typed is not between '{first}' and '{last}'!\nPlease enter the correct value.\n"
        elif type:
            msg = f"\nThe value you typed is not of type '{value}'!\nPlease enter the correct value.\n"

        return msg

    def menu():
        '''To print the game menu.'''
        print('\nMenu: (1) Play | (2) New | (3) Analysis | (9) Exit\n')

class BoxSate:
    def open_box():

    def player_box():



#GamePlay.main()
