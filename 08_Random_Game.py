#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


game_on = None
guess = None
secret = None


# In[ ]:


def difficulty_level_easy():
        global guess
        global secret
        guess = 10
        secret = int(random.randrange(0,2))
        for i in range(guess):
            guess = int(input('Guess a number (0 to 2). '))
            if i == 2:
                print ('Game over. Too many guesses. ')
                play_again()
            elif guess > secret:
                print('your guess is too high. Try again.')
            elif guess < secret:
                print('your guess is too low. Try again.')
            elif guess == secret:
                print('You win!')
                
def difficulty_level_hard():
        global guess
        global secret
        guess = 10
        secret = int(random.randrange(0,10))
        for i in range(guess):
            guess = int(input('Guess a number (0 to 9). '))
            if i == 3:
                print ('Game over. Too many guesses. ')
                play_again()
            elif guess > secret:
                print('your guess is too high. Try again.')
            elif guess < secret:
                print('your guess is too low. Try again.')
            elif guess == secret:
                print('You win!')
                
def start_game():
    global game_on
    game_on = True
    level = input('Welcome. Type easy, hard, or quit. ')
    if level == 'easy':
        difficulty_level_easy()
    elif level == 'hard':
        diffculty_level_hard()
    elif level == 'quit':
        game_on = False
        print('Thanks for playing')
        
def play_again():
    global game_on
    game_on = True
    play = input('Play again? Yes or No. ')
    if play == 'Yes':
        start_game()
    else:
        game_on = False
        print('Thanks for playing')
        play_again()
start_game()


# In[ ]:




