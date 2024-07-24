import pygame
from os import listdir
from os.path import isfile, join
#this class we load our sprites for the animation of enemies 
#i use the os library to manipulate data of the files to make the package
#of the engine load each sprite from the repository where the project is located
#also i included a function to update sprites for characters , load scenario and 
#mainpulate animations

class Sprite(pygame.sprite.Sprite):
    pass
def __init__(self):
    pass
def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sheet(dir1,dir2,width,height,direction=False):
    file_path = join("assets",dir1,dir2)
    images = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    all_sprites = {}
    for image in images:
        sprite_sheet = pygame.image.load(join(file_path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

def update_sprite_char(self):
    pass
    GRAVITY = 1
    sprite_sheet = "idle"
    if self.hit:
        sprite_sheet = "hit"
    elif self.y_vel < 0:
        if self.jump_count == 1:
            sprite_sheet = "jump"
        elif self.jump_count == 2:
            sprite_sheet = "double_jump"
    elif self.y_vel > self.GRAVITY * 2:
        sprite_sheet = "fall"
    elif self.x_vel != 0:
        sprite_sheet = "run"
        
def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        
def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))

class Obj_Sprite(pygame.sprite.Sprite): #class that will be used to load objects and stuff#
   pass
def __init__(self, x, y, width, height, name=None):
    pass
    super().__init__()
    self.rect = pygame.Rect(x, y, width, height)
    self.image = pygame.Surface((width, height), pygame.SRCALPHA)
    self.width = width
    self.height = height
    self.name = name
def get_background(self,name,width,height):
    self.HEIGHT = height
    self.WIDTH = width
    self.width = width
    self.height = height
    width = 0
    height = 0
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    for i in range(self.WIDTH // self.width + 1):
        for j in range(self.HEIGHT // self.height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

def draw(self, win, offset_x):
       win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
def get_block(size): #this function wrote let us have our terrain #
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 128, size, size) #this envolve a bit of try and error 
    #But im pretty sure its suposed to make sure i need have some pixel understanding 
    # and also know how use this lib properly
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)
class Block(Obj_Sprite):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)







    
    
    