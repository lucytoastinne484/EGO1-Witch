#This module will define our window to display#
import pygame as engine
class window:
    def __init__(self):
        pass
    def display(self,WIDTH,HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.resizable = True
        engine.display.set_mode((WIDTH,HEIGHT))
        
        
    
    