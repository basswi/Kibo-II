# import pygame library
import pygame, sys
# import pygame.locals for easier access to key coordinates
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN)
# import tkinter to create menu buttons
from tkinter import *

#initiating pygame
pygame.init()

# choosing the style of the font for texts
pygame.font.init()
font = pygame.font.SysFont("cambria", 20)
window = pygame.display.set_mode((500, 500))



class Background:
    def __init__(self):
        # define constansts for the screen width and hight
        self.screen_width = 500
        self.screen_height = 500
        # initiating the screen
        self.screen = pygame.display.set_mode((self.screen_width,
        self.screen_height))

    def bg_image(self):
        pygame.display.set_caption("Kibo II")
        self.background = pygame.image.load("forest.jpg")
        self.screen.blit(self.background, (0, 0))
        # pygame.display.flip()

    def platforms(self, position_1, position_2, width, height):
        self.color = (255, 0, 0)
        self.platform = pygame.draw.rect(self.screen, self.color,
        pygame.Rect(position_1, position_2, width, height))
        pygame.display.flip()


kibo_bg = Background()
ground = Background()
platform_1 = Background()
platform_2 = Background()
platform_3 = Background()
platform_4 = Background()

class Physic:
    def __init__(self, x, y, width, height, acc, max_vel):
        self.h_velocity = 0  #horizontal velocity
        self.v_velocity = 0  #vertical velocity
        self.acc = acc
        self.max_vel = max_vel
        self.width = width
        self.height = height
        self.x_cord = x
        self.y_cord = y
        self.pre_x = x
        self.pre_y = y

    def physic_tick(self, floors):
        self.v_velocity += 0.6
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.x_cord += self.h_velocity
        self.y_cord += self.v_velocity
        for floor in floors:
            if floor.hitbox.colliderect(self.hitbox):
                # self.x_cord = self.pre_x
                self.y_cord =  self.pre_y
                self.v_velocity = 0

        self.pre_x = self.x_cord
        self.pre_y = self.y_cord

#adding the Player
class Player(Physic):
    def __init__(self):
        self.image = pygame.image.load("ludek3.png")
        width = self.image.get_width()
        height = self.image.get_height()
        super().__init__(30, 360, width, height, 0.5, 5)
        self.speed = 4
        self.h_velocity = 0
        self.acc = 1
        self.max_vel = 5 #maximum velocity

    def tick(self, keys, floors):
        self.physic_tick(floors)
        if keys[pygame.K_LEFT] and self.h_velocity > self.max_vel * -1:
            self.h_velocity -= self.acc
        if keys[pygame.K_RIGHT] and self.h_velocity < self.max_vel:
            self.h_velocity += self.acc
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            if self.h_velocity > 0:
                self.h_velocity -= self.acc
            elif self.h_velocity < 0:
                self.h_velocity += self.acc

        self.x_cord += self.h_velocity
        self.y_cord += self.v_velocity
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Floor:
    def __init__(self, x, y, width, height):
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, (51, 40, 10), self.hitbox)


# define menu method with buttons
def main_menu():

    # variable to keep the main loop running
    running = True
    while running:

        # look at every event in the queue
        for event in pygame.event.get():

            # did the user click the window close button? If so, stop the loop.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # did the user hit a key?
            if event.type == KEYDOWN:
                # was it the escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()





# Main loop:
run = True
player = Player()
floors = [Floor(20, 480, 760 , 8)]
while run:
    ground.platforms(0, 470, 500, 30)
    platform_1.platforms(78, 370, 64, 10)
    platform_2.platforms(182, 303, 75, 15)
    platform_3.platforms(289, 240, 62, 10)
    platform_4.platforms(370, 200, 120, 15)
    kibo_bg.bg_image()
    keys = pygame.key.get_pressed()
    player.tick(keys, floors)
    player.draw()
    for floor in floors:
        floor.draw(window)
    pygame.display.update()

pygame.quit()
