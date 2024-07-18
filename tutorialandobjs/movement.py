import pygame
class movement:
    def __init__(self,x,y,width,height):
        pass
        self.rect = pygame.Rect(x,y,width,height)
        self.vel = 0
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.up_count = 0
        self.down_count = 0
        self.gravity_value = 0
        self.stop_count = 0
    def speed(self,velocity,x_vel,y_vel):
        self.vel = velocity
        self.x_speed = x_vel
        self.y_speed = y_vel
    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    
    def stop(self):
        self.stop_count = 0
        self.x_vel = self.vel
        self.y_vel = self.vel
        self.stop_count +=1
        if self.stop_count >= 1:
            self.x_vel = 0
            self.y_vel = 0
    
    
    
    def move(self,dx,dy):
        pass
        self.rect.x += dx
        self.rect.y += dy
    def move_down(self,vel):
        pass
        self.y_vel = -vel
        if self.direction != "down":
            self.direction = "down"
            self.animation_count = 0
    
    def move_up(self,vel):
        pass
        self.y_vel = vel
        if self.direction != "up":
            self.direction = "up"
            self.animation_count = 0
            
        
    def move_right(self,vel):
        pass
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0    
            
    def move_left(self,vel):
        pass
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    def damage(self):
        self.dmg = True
        self.invencibility = False
        pass
    def diagonal_left(self):
        pass
    def diagonal_right(self):
        pass
    def colision_mask(self):
        pass
    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
    
        
        

   
