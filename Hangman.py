import random
hangman=["""
    +---+
    |   |
        |
        |
        |
        |
==========""","""
    +---+
    |   |
    0   |
        |
        |
        |
==========""","""
    +---+
    |   |
    0   |
    |   |
        |
        |
==========""","""
    +---+
    |   |
    0   |
   /|   |
        |
        |
==========""","""
    +---+
    |   |
    0   |
   /|\  |
        |
        |
==========""","""
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
==========""","""
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
==========="""]

list=["aniket","tiwari","anikettiwari","mango","apple","friend","sneke","pizza","house","home","moon","sun","ram","sita","bharat","water","drink"]
# print(list)
mwrong=len(hangman)-1
list1=random.choice(list)
right_guess="-" * len(list1)
print(list1)
print(right_guess)
wrong_guess=0
used_letters=[]
print("welomr to hangman")
print("try to guess the list")

while wrong_guess<mwrong and right_guess!=list1:
    print(hangman[wrong_guess])
    print("used_lettar",used_letters)
    print("right guess",right_guess)
    guess=input("enter your guess")
    guess=guess.lower()

    while guess in used_letters:
        print("you have alreadey guessed that letter",guess)
        guess=input("enter your guess")
        guess=guess.lower()

    used_letters.append(guess)
    if guess in list1:
        print("you have guess right")

        new_right_guess=""
        for i in range(len(list1)):
           if guess==list1[i]:
            new_right_guess+=guess
           else:
            new_right_guess+=right_guess[i]
   
        right_guess=new_right_guess
    else:
        print("sorry you are wrong")
        wrong_guess+=1

if wrong_guess==mwrong:
    print(hangman[wrong_guess])
    print("you have been hanged")
    print("the right word is ",list1)
else:
    print("you have won")

