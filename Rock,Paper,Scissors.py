#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
guess = random.choice(["ROCK","PAPER","SCISSORS"])
Wins,Losses,Tie = 0,0,0

#Intro to the game
while True:
 print("ROCK, PAPER, SCISSORS\n")
 print("%d Wins, %d Loss, %d Ties" %(Wins,Losses,Tie))

 choice = str(input("Enter your move: (r)ock (p)aper (s)cissors or (q)quit\n"))

#Ask player to make a choice
 if choice == "r":
    print("ROCK versus...")
 elif choice == "p":
    print("PAPER versus...")
 elif choice == "s":
    print("SCISSORS versus...")
 elif choice == "q":
    print("Thanks for playing!")
    break
    
 print(guess)

#Determine who wins

 if (choice == "p" and guess == "ROCK") or (choice == "s" and guess == "PAPER") or (choice == "r" and guess == "SCISSORS"):
    print("You Win!")
    Wins += 1
 elif  (choice == "r" and guess == "PAPER") or (choice == "p" and guess == "SCISSORS") or (choice == "s" and guess == "ROCK"):
    print("You Lose!")
    Losses += 1
 elif (choice == "r" and guess == "ROCK") or (choice == "p" and guess == "PAPER") or (choice == "s" and guess == "SCISSORS"):
    print("It's a Tie")
    Tie += 1

