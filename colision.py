import pygame
class Colision_handle:
    pass
def __init__(self):
    pass
def colision(self,player,objs,dx):
    pass
    player.move(dx, 0)
    player.update()
    objects = []
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object
def obj_colision(self):
    pass
def handle_move(self):
    pass
def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects