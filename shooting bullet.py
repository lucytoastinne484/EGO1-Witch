import pygame as engine#we will use the lib to create this game

import os as system#we will use it to bring the files and manipulate the os

import random as rand#we will use it for critical atack gimmick

import math as calc#eventually i will make a use of this lib

from os import listdir as list_dir#we import this to load sprites

from os.path import isfile, join#we use this to process files and use directories

import numpy as np#and we have another lib for calcule

import time as t #t stands for time here 

engine.init()#start the game


engine.display.set_caption("movement test and learning")#game´s title

window = engine.display.set_mode((600,400))#window setup where our game
#is going to run

player_pos = engine.Vector2(window.get_width()/2,window.get_height()/2)
#we use the above class to create the player position
obj_x = 0
obj_y = 0
obj_pos = obj_x,obj_y#objs position to create our scenarios and stuff
dt = 30#dt represents our player speed to move itself
GRAVITY_coeficient = 40 #value of gravity in our game

bullet_pos = engine.Vector2(window.get_width()/2,window.get_height()/2)


key_count = 0 

class movement:
    def __init__(self):
        self.GRAVITY_coeficient = 40
        self.speed = 30



def main(window):
    pass
    clock = engine.time.Clock()
    FPS = 60 #how many frames our game will have 
    run = True#this make our game run and stop 
    while run:#this is where our loop will run#

        for event in engine.event.get():#this for loop will make sure our game is going to
                                        #going to stop
            if event.type == engine.QUIT:
                run = False
                break
            
            window.fill("purple")#this command we use to fill the bg
            #with pruple
            
            
            #here we create our player sprite
            engine.draw.circle(window, "green", player_pos, 40)
            #here we will create a bullet 
            engine.draw.circle(window, "white", bullet_pos, 10)
            #Menu concept
            engine.draw.rect(window, "white", engine.Rect(0, 350, 50, 50),2)
            #minimap concept design#
            engine.draw.circle(window, "white", (550,50), 40)
            
            #---------------------------#
            menu_ui_path = r"C:\Users\Computador\EGO1Project\gameimgs\219f296a8ac18a0b9fcc819216e02834.jpg"
            keys = engine.key.get_pressed()#define kesy interaction
            cursor = engine.mouse.get_pos()#defines a cursor
            mouse = engine.mouse.get_pressed()# defines mouse controls
            
            #cursor i accidentaly made 
            engine.draw.circle(window,"black",cursor,10)
            #colision and rect functions in python#
            engine.Rect((10,10),(10,10)) #this command create a rect coordinate
            r = engine.Rect(1,2,3,4)#its seems like i can iterate through this obj
            x,y,z,h = r
            #except use a var to make a OOP with this case
            
            #in this test i will print a copy of the previous rect i created 
            x = engine.Rect.copy(r)#sucessuful test
            
            
            #this test will move our rect previously created 
            def move_rect(self,x,y):
                return engine.Rect.move_ip(x, y)
            
            
            
            
            #keys that we are using to move our player
            if keys[engine.K_w] and dt <= GRAVITY_coeficient:#move up our player
                player_pos.y -= dt
            if keys[engine.K_s] and dt <= GRAVITY_coeficient:#move down our player
                player_pos.y += dt
            if keys[engine.K_a] and dt <= GRAVITY_coeficient:#move our player to left
                player_pos.x -= dt
            if keys[engine.K_d] and dt <= GRAVITY_coeficient:#move our player to right
                player_pos.x += dt
            if keys[engine.K_e]:#this command change our player color to red
                pass
                engine.draw.circle(window, "red", player_pos, 40)
            if keys[engine.K_q]:#makes our player acelarate#
                pass
                dt * 2
            if keys[engine.K_r]:
                pass
                dt/2
            if keys[engine.K_SPACE]:
                #this command will make our player shoot a bullet to left
                pass
                bullet_pos.x -= dt
            if keys[engine.K_RIGHT]:
                pass
                bullet_pos.x += dt
                #this command will make our player shoot a bullet to right
            if keys[engine.K_ESCAPE]:
                pass #makes our game stop
                engine.quit()
            if key_count >= 1 and GRAVITY_coeficient == 40:
                dt * 2 
            if keys[engine.K_8]:#this will change the color of our cursor to red
                engine.draw.circle(window, "red", cursor, 10)
            if keys[engine.K_9]:#makes our menu grow bigger
                engine.draw.rect(window,"red",engine.Rect(0, 10, 400, 500))
                engine.draw.rect(window,"white",engine.Rect(0, 10, 400, 500),3)
                
                
            

             
                
            #the command bellow i use to update the elements previous putted in
            #the main function
            engine.display.flip()
            df = clock.tick(FPS)/1000#df coeficient is a another coeficient i
            #used to make the game run

    engine.quit()#this function from pygame make our game stop running
            




if __name__ == "__main__":
    main(window)# this if statement we use to run the main
    #function that uses the window argument to run