# import pygame library
import pygame
# import pygame.locals for easier access to key coordinates
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)
# import pygame-menu to create menu buttons
import pygame_menu
#importing mixer for sounds
from pygame import mixer
#preset the mixer init arguments
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=4096)

#initiating pygame
pygame.init()



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
        # get the image, position it at (0, 0) and draw it onto the screen
        self.screen.blit(self.background, (0, 0))
        #pygame.display.flip()

    def platforms(self, position_1, position_2, width, height):
        # define platform colour
        self.color = (255, 0, 0)
        # draw the platform onto the screen
        self.platform = pygame.draw.rect(self.screen, self.color,
        pygame.Rect(position_1, position_2, width, height))
        # use pygame.display.flip() to see the platforms
        # pygame.display.flip()

class Player:
    #first - placing our player
    def __init__(self):
        self.xcord = 20
        self.ycord = 400
        self.image = pygame.image.load("ludzik-removebg.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #adding horizontal velocity, vertical velocity, acceleration, max velocity
        self.h_velocity = 0
        self.v_velocity = 0
        self.accel = 0.5
        self.max_velocity = 3
        #to set hitbox collision
        self.hitbox = pygame.Rect(self.xcord, self.ycord, self.width, self.height)

    def tick(self, keys):
        if keys[pygame.K_LEFT] and self.h_velocity > self.max_velocity * -1:
            self.h_velocity -= self.accel
            step_sound.play(-1)
        if keys[pygame.K_RIGHT] and self.h_velocity < self.max_velocity:
            self.h_velocity += self.accel
            step_sound.play(-1)
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            if self.h_velocity > 0:
                self.h_velocity -= self.accel
                step_sound.stop()
            elif self.h_velocity < 0:
                self.h_velocity += self.accel
                step_sound.stop()
        self.xcord += self.h_velocity
        self.hitbox = pygame.Rect(self.xcord, self.ycord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.xcord, self.ycord))

class Bush:
    #first - placing our bush
    def __init__(self):
        self.xcord = 350
        self.ycord = 23
        self.image = pygame.image.load("blueberry_bush-removebg.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #to set hitbox collision
        self.hitbox = pygame.Rect(self.xcord, self.ycord, self.width, self.height)
    def tick(self):
        self.hitbox = pygame.Rect(self.xcord, self.ycord, self.width, self.height)
    def draw(self):
        window.blit(self.image, (self.xcord, self.ycord))

class Berry:
    #first - placing our berry
    def __init__(self):
        self.xcord = 350
        self.ycord = 50
        self.image = pygame.image.load("blueberry-removebg.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    def tick(self):
        pass
    def draw(self):
        window.blit(self.image, (self.xcord, self.ycord))

class Music:

    def __init__(self):
        pygame.mixer.music.load("music.wav")
        #looping main music
        pygame.mixer.music.play(-1)
        #adjusting volume
        pygame.mixer.music.set_volume(0.3)

    #function for adjusting sound in menu
    def adjust_volume(self,value,loudness):
        if loudness == 0:
            pygame.mixer.music.set_volume(0.00)
        if loudness == 1:
            pygame.mixer.music.set_volume(0.1)
        if loudness == 2:
            pygame.mixer.music.unpause()
            pygame.mixer.music.set_volume(0.2)
        if loudness == 3:
            pygame.mixer.music.unpause()
            pygame.mixer.music.set_volume(0.3)

step_sound = pygame.mixer.Sound("steps.wav")
step_sound.set_volume(0.1)

# choosing the style of the font for texts
pygame.font.init()
font = pygame.font.SysFont("cambria", 20)
window = pygame.display.set_mode((500, 500))


kibo_bg = Background()
ground = Background()
platform_1 = Background()
platform_2 = Background()
platform_3 = Background()
platform_4 = Background()
volume = Music()


# Main loop:
def main():
    run = True
    player = Player()
    #making a list, then we will add our bush to the list
    bushes = []
    #making a list, then we will add our berry to the list
    berries = []
    bush = 0
    berry = 0
    background = pygame.image.load("forest.jpg")
    welcome = font.render("Witaj w świecie Kibo-II!", True, (0,0,0))
    background.blit(welcome, (50, 50))

    while run:

        ground.platforms(0, 470, 500, 30)
        platform_1.platforms(78, 370, 64, 10)
        platform_2.platforms(182, 303, 75, 15)
        platform_3.platforms(289, 240, 62, 10)
        platform_4.platforms(370, 200, 120, 15)
        kibo_bg.bg_image()

        keys = pygame.key.get_pressed()

        #adding bush to the list
        if bush == 0:
            bushes.append(Bush())
        for bush in bushes:
            bush.tick()
        for berry in berries:
            berry.tick()

        #if the player collides with the bush, we delete the bush and we add berry to the list
        for bush in bushes:
            if player.hitbox.colliderect(bush.hitbox):
                bushes.remove(bush)
                berries.append(Berry())

        player.tick(keys)
        window.blit(background, (0, 0 ))
        player.draw()

        #drawing our bush and our berry
        for bush in bushes:
            bush.draw()
        for berry in berries:
            berry.draw()
        pygame.display.update()

        # look at every event in the queue
        for event in pygame.event.get():

            # did the user click the window close button? If so, stop the loop.
            if event.type == QUIT:
                pygame.quit()

            # did the user hit a key?
            if event.type == KEYDOWN:
                # was it the escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    pygame.quit()



# calling the game
def start_the_game():
    if __name__ == "__main__":
        main()

# defining menu options
main_menu = pygame_menu.Menu("Menu", 500, 500, theme=pygame_menu.themes.THEME_GREEN)
main_menu.add.button("Zacznij grę", start_the_game)
main_menu.add.selector("Poziom głośności:", [("Max",3),("2",2),("1",1),("0", 0)], onchange = volume.adjust_volume)
main_menu.add.button("Wyjdź", pygame_menu.events.EXIT)

# calling menu
main_menu.mainloop(window)



pygame.quit()
