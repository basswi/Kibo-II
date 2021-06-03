# import pygame library
import pygame, sys
# import pygame.locals for easier access to key coordinates
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN)
# import tkinter to create menu buttons
from tkinter import *
#importing mixer for sounds
from pygame import mixer

#initiating pygame
pygame.init()

# choosing the style of the font for texts
pygame.font.init()
font = pygame.font.SysFont("cambria", 20)

class Background:
    def __init__(self):
        # define constansts for the screen width and hight
        self.screen_width = 500
        self.screen_height = 500
        # initiating the screen
        self.screen = pygame.display.set_mode((self.screen_width,
        self.screen_height))

    def bg_image(self):
        # set game window name
        pygame.display.set_caption("Kibo II")
        # load image to create a background object
        self.background = pygame.image.load("forest.jpg")
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def platforms(self, position_1, position_2, width, height):
        self.color = (255, 0, 0)
        self.platform = pygame.draw.rect(self.screen, self.color,
        pygame.Rect(position_1, position_2, width, height))
        # pygame.display.flip()


kibo_bg = Background()
ground = Background()
platform_1 = Background()
platform_2 = Background()
platform_3 = Background()
platform_4 = Background()

class Physic:
    def __init__(self, x, y, width, height, acc, max_vel):
        self.h_velocity = 0
        self.v_velocity = 0  #pion
        self.acc = acc  #przyspieszenie
        self.max_vel = max_vel
        self.width = width
        self.height = height
        self.x_cord = x
        self.y_cord = y
        self.pre_x = x
        self.pre_y = y

    def physic_tick(self, grounds):
        self.v_velocity += 0.7
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.x_cord += self.h_velocity
        self.y_cord += self.v_velocity

        for ground in grounds:
            if ground.hitbox.colliderect(self.hitbox):
                # self.x_cord = self.pre_x
                self.y_cord =  self.pre_y
                self.v_velocity = 0

        self.pre_x = self.x_cord
        self.pre_y = self.y_cord

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
while run:
    ground.platforms(0, 470, 500, 30)
    platform_1.platforms(78, 370, 64, 10)
    platform_2.platforms(182, 303, 75, 15)
    platform_3.platforms(289, 240, 62, 10)
    platform_4.platforms(370, 200, 120, 15)
    kibo_bg.bg_image()

pygame.quit()

print("Test git")
