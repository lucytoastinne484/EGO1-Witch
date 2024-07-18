#This is our __init__.py file#
import pygame as engine #This will create a enviroment that most likely is a engine
import math as calcule
import numpy as np
from os import listdir as dir_list
from os.path import isfile, join 

engine.init()#Then we start it using this function of the module


WIDTH = 0
HEIGHT = 0
GRAVITY_VALUE = 0
JUMPS = 0
FALLS = 0
DEATHS = 0
LIFES = 0
MESSAGE=""
diretion = ""
RED = 0
GREEN = 0
BLUE = 0
COLOR = (RED,GREEN,BLUE)
CHAR_MASK = None
OBJ_MASK = None
SPRITE_DIR = ""
X_SPEED : float = 0
Y_SPEED : float = 0


if __name__ == "__main__":
    engine.init()
        


