# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 03:13:11 2021

@author:Manish Kumar Goswami

"""
import random

import datetime

date = datetime.date.today()

time = datetime.datetime.now().time()

print("Today Date is ",date,"and time is",time)

def hangman():
    word = random.choice(["antman","aquaman","batman", "Blackpanther", "captainamerica","captainmarvel","doctorstrange", "fantasticfour", "ghostrider", "greenarrow", "greenlantern", "hellboy", "hulk", "ironman", "krrish", "spiderman", "superman", "thor", "wolverine", "wonderwoman", "xmen", "supergirl", "vision", "falcon", "wanda", "blackwidow"])
    
    validLatters = "abcdefghijklmnopqrstuvwxyz"
    
    turns = 10
    
    guessMade = ""
    
    while len(word) > 0:
        
        main = ""
        
        for letter in word:
            
            if letter in guessMade:
                
                main = main + letter
                
            else:
                
                main = main + "_"+" "
        
        if main == word:
            
            print("You guess the wright name",main,"You Win!")
            
            print("\U0001F60D   \U0001F60D   \U0001F60D   \U0001F60D   \U0001F60D   \U0001F60D")
            
            break
        
        print("Guess the word",main)
        
        guess = input()
        
        if guess in validLatters:
            
            guessMade = guessMade + guess
            
        else:
            print("Enter a valid alphabets")
            guess = input()
        
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("__________________________")
            if turns == 8:
                print("8 turns left")
                print("__________________________")
                print("             O            ")
                print("")
            if turns == 7:
                print("7 turns left")
                print("__________________________")
                print("             O            ")
                print("             |            ")
                print("")
            if turns == 6:
                print("6 turns left")
                print("__________________________")
                print("             O            ")
                print("             |            ")
                print("            /             ")
                print("")
            if turns == 5:
                print("5 turns left")
                print("__________________________")
                print("             O            ")
                print("             |            ")
                print("            / \           ")
                print("")
            if turns == 4:
                print("4 turns left")
                print("__________________________")
                print("           \ O            ")
                print("             |            ")
                print("            / \           ")
                print("")
            if turns == 3:
                print("3 turns left")
                print("__________________________")
                print("           \ O /          ")
                print("             |            ")
                print("            / \           ")
                print("")
            if turns == 2:
                print("2 turns left")
                print("__________________________")
                print("           \ O/|          ")
                print("             |            ")
                print("            / \           ")
                print("")
            if turns == 1:
                print("1 turns left")
                print("One move left be carefull other wise you will die, Take care!")
                print("__________________________")
                print("           \ O_/|         ")
                print("             |            ")
                print("            / \           ")
                print("")
            if turns == 0:
                print("You loose You have to Die HAHAHAHAHAHAHAHAH")
                print("\U0001F620   \U0001F620   \U0001F620   \U0001F620  \U0001F620  \U0001F620")
                print("__________________________")
                print("             O_|          ")
                print("            /|\           ")
                print("            / \           ")
                print("")
                break
    
print("______________________________________________________________________")

name = input("Enter you Name to start game")

print("Hello,",name.title())

print("______________________________________________________________________")

print(" ")

print("Let's Start The game",name.title())

print(" ")

print("Rule of the game:-")

print(" ")

print("Guess the Super hero name in less then 10 attempts otherwise your emojy will die ")

print(" ")

print("\U0001F620   \U0001F620   \U0001F620   \U0001F620  \U0001F620  \U0001F620")

print("______________________________________________________________________")

print(" ")

hangman()

print()













