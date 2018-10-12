#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:36:57 2018

@author: tabatalab
"""

word_list = ["affix","dummy","frame","ideal","wedge","youth"]
import random
index = random.randrange(6)

def hangman(word):
    wrong = 0
    stages = ["",
              "__________            ",
              "|                     ",
              "|        |            ",
              "|        O            ",
              "|       /|\           ",
              "|       / \           ",
              "|                     "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman's world!")
    
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Please predict one letter:")
        
        
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[0:wrong+1]))
        
        if "_" not in board:
            print("You won!")
            print(" ".join(board))
            win = True
            break
    
    if win == False:
        print("\n".join(stages))
        print("\n")
        print("You lost! The answer is {}".format(word))
        
hangman(word_list[index])