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
