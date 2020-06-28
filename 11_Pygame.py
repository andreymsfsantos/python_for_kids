#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pygame


# In[ ]:


import pygame
import time

# print (pygame.ver)

pygame.init()  # initializing pygame

# Stting up the game screen - color
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# Setting up the game secreen - size
screen_width = 400
screen_height = 600
game_screen = pygame.display.set_mode((screen_width, screen_height))
game_screen.fill(black)

while True:
    pygame.draw.circle(game_screen, red, (250, 300), 20)          #circle
    pygame.draw.rect(game_screen, blue, (20, 20, 50, 80))         #rectangle
    pygame.draw.ellipse(game_screen, white, (300, 200, 40, 80))   # ellipse
    pygame.display.update()


# In[ ]:


#python sample.py # to test your code

# Moving objects with the keyboard

pygame.key.get_pressed() # working with the keyboard
pygame.key.set_repeat()  # control how the computer takes the input when a user presses a key

