import numpy as np
import pandas as pd
import pathlib
import random


class NewGame:

    def __init__(self, name):
        self.name = name
        self.played = ""
        self.chosen_box = ""
        self.open_box = ""
        self.turns_left = 23
        self.win = False
        self.deal = False
        self.box_assignment()


    def box_assignment(self):
        box_values= [0.01,0.10,0.50,1.00,5.00,10.00,50.00,100.00,250.00,500.00,750.00,1000.00,3000.00,5000.00,10000.00,15000.00,20000.00,35000.00,50000.00,75000.00,100000.00,250000.00]
        random.shuffle(box_values)
        boxes_df = pd.DataFrame(index=range(1,24), columns=['state', 'value'])
        #boxes_df.assign(state=lambda x: "closed")

def main():
    name = input("Enter your name: ")
    g = NewGame(name)

main()
