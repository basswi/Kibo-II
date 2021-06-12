# import pygame and sys library
import pygame, sys
# import pygame.locals for easier access to key coordinates
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN,
                           MOUSEBUTTONDOWN, K_RETURN, QUIT)
# import pygame-menu to create menu buttons
import pygame_menu
#importing mixer for sounds
from pygame import mixer
import random
#preset the mixer init arguments
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=4096)

#initiating pygame
pygame.init()

clock = clock = pygame.time.Clock()

class Background:

    def __init__(self):
        # define constansts for the screen width and hight
        self.screen_width = 500
        self.screen_height = 500
        # initiating the screen
        self.screen = pygame.display.set_mode((self.screen_width,
        self.screen_height))

    def bg_image(self):
        # replaced this to lines 56-57
        # # set game window name
        # pygame.display.set_caption("Kibo II")

        # load image to create a background object
        self.background = pygame.image.load("forest.jpg")
        # get the image, position it at (0, 0) and draw it onto the screen
        self.screen.blit(self.background, (0, 0))
        #pygame.display.flip()

    def platforms(self, position_1, position_2, width, height):
        # define platform colour
        self.color = (255, 0, 0)
        # draw the platform onto the screen
        self.hitbox = pygame.draw.rect(self.screen, self.color,
        pygame.Rect(position_1, position_2, width, height))
        # use pygame.display.flip() to see the platforms
        # pygame.display.flip()


# define class for intro to our game
class instructions():

    # set background for intro
    def __init__(self):
        self.bg_menu = pygame.image.load("forest-menu.jpg")
        # set game window name
        pygame.display.set_caption("Kibo II")

    def welcome_text(self):
        # clearing background
        window.blit(self.bg_menu, [0, 0])
        # print welcome text on the screen
        welcome = font.render("Witaj w naszym Zaczarowanym Lesie!", True, (0,0,0))
        window.blit(welcome, [140, 50])
        # print instruction1 on the screen
        instruction1 = font.render("Aby przejść do rozgrywki naciśnij ekran w "
                                   "dowolnym miejscu.", True, (0,0,0))
        window.blit(instruction1, [50, 420])
        # flip the screen to show results of printing texts
        pygame.display.flip()

    def clicking(self):
        # to prevent adding text one on the top of another
        self.welcome_text()

        # rendering texts
        text1 = font.render("Pozwól, że wprowadzę Cię, w jakim celu się tu "
                            "spotykamy...", True, (0,0,0))
        window.blit(text1, [50,100])

        text2 = font.render("W naszej okolicy od dawna grasuje wilk i nikt nie "
                            "jest w stanie go", True, (0,0,0))
        text3 = font.render(" wypędzić. Miejscowi mieszkańcy ukryli się lub "
                            "przeprowadzili", True, (0,0,0))
        text4 = font.render("za góry i lasy. ", True, (0,0,0))
        text5 = font.render("Niestety nie wszystkim się to udało... Mały gołąbek"
                            "został złapany", True, (0,0,0))
        text6 = font.render("przez wilka. Aby go uwolnić potrzebujemy Ciebie, "
                            "abyś go", True, (0,0,0))
        text7 = font.render("pokonał/pokonała. My niestety nie wiemy, jak "
                            "to zrobić. ", True, (0,0,0))
        text8 = font.render("Może Tobie się to uda? Jest tylko jedna rzecz, o "
                            "której musisz ", True, (0,0,0))
        text9 = font.render("pamiętać: nikt nie może Cię zobaczyć!", True, (0,0,0))
        good_luck = font.render("Powodzenia!", True, (0,0,0))

        window.blit(text2, [50,120])
        window.blit(text3, [50,140])
        window.blit(text4, [50,160])
        window.blit(text5, [50,200])
        window.blit(text6, [50,220])
        window.blit(text7, [50,240])
        window.blit(text8, [50,260])
        window.blit(text9, [50,280])
        window.blit(good_luck, [50,340])

        # flip the screen to show results of printing texts
        pygame.display.flip()



class Player:
    #first - placing our player
    def __init__(self):
        self.xcord = 20
        self.ycord = 400
        self.image = pygame.image.load("red-riding-hood-removebg.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.width =  50
        self.height = 50
        #adding horizontal velocity, vertical velocity, acceleration, max velocity
        self.h_velocity = 0
        self.v_velocity = 0
        self.accel = 5
        self.max_velocity = 3
        #to set hitbox collision
        self.hitbox = pygame.Rect(self.xcord, self.ycord, self.width, self.height)
        # variables for jump function
        self.is_jumping = False
        self.jump_count = 10
        self.jump_height = 10

    #pulling player to lowest layer
    def gravity(self):
        if self.ycord != 400:
            self.ycord += 5
            if self.ycord > 400:
                self.ycord == 400

    #not pulling player when on platform
    def onplatform(self):
        if self.ycord !=400:
            self.ycord += 0

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
        pygame.time.delay(10)

        #instances
        ground.platforms(0, 470, 500, 30)
        platform_1.platforms(78, 370, 64, 10)
        platform_2.platforms(182, 303, 75, 15)
        platform_3.platforms(289, 240, 62, 10)
        platform_4.platforms(370, 200, 120, 15)

        #CAUTION, SPAGHETTI COLLISION
        if self.hitbox.colliderect(ground.hitbox):
            self.ycord = 400

        if self.hitbox.colliderect(platform_1.hitbox):
            self.onplatform()
            #self.stop_jump()
            self.ycord = 316

        if self.hitbox.colliderect(platform_2.hitbox):
            self.onplatform()
            #self.stop_jump()
            self.ycord = 303-54

        if self.hitbox.colliderect(platform_3.hitbox):
            self.onplatform()
            #self.stop_jump()
            self.ycord = 240-54

        if self.hitbox.colliderect(platform_4.hitbox):
            self.onplatform()
            #self.stop_jump()
            self.ycord = 200-54

    def jump(self):
        # if user hits K_UP
        if self.is_jumping == True:
            # decrease y coordinate
            self.ycord -= self.jump_height * 2.5
            self.jump_height -= 1
            # stop jumping when jump_height reaches -10
            if self.jump_height < - 10:
                self.is_jumping = False
                self.jump_height = 10
        pygame.time.delay(10)

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


class Enemy:
    def __init__(self):
        self.xcord = 280
        self.ycord = 345
        self.image = pygame.image.load("wilczek.png")
        self.image = pygame.transform.scale(self.image, (150, 140))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.xcord, self.ycord, self.width, self.height)
        self.howl_timer = 50000

    def howling(self):
        self.howl_timer += pygame.time.get_ticks()/1000
        print(self.howl_timer)
        if self.howl_timer > 50000:
            random.choice(wolf_sounds).play()
            self.howl_timer = 0

    def tick(self):
        self.hitbox = pygame.Rect(self.xcord, self.ycord, self.width, self.height)
    def draw(self):
        window.blit(self.image, (self.xcord, self.ycord))


class Victim:
    def __init__(self):
        self.xcord = 420
        self.ycord = 395
        self.image = pygame.image.load("golomp-removebg.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.xcord, self.ycord, self.width, self.height)
        self.is_jumping = False
        self.jump_count = 10
        self.jump_height = 10

    def jump(self):
        if self.is_jumping == True:
            # decrease y coordinate
            self.ycord -= self.jump_height * 0.8
            self.jump_height -= 1
            # stop jumping when jump_height reaches -10
            if self.jump_height < - 10:
                self.is_jumping = False
                self.jump_height = 10

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


#sound library
step_sound = pygame.mixer.Sound("steps.wav")
step_sound.set_volume(0.1)
jump_sound = pygame.mixer.Sound('jump.wav')
jump_sound.set_volume(0.3)

wolf_sounds= [pygame.mixer.Sound('wolf.wav'), pygame.mixer.Sound('growl.wav')]
wolf_sounds[0].set_volume(0.05)
wolf_sounds[1].set_volume(0.1)

# choosing the style of the font for texts
pygame.font.init()
font = pygame.font.SysFont("gabriola", 20)
window = pygame.display.set_mode((500, 500))


kibo_bg = Background()
ground = Background()
platform_1 = Background()
platform_2 = Background()
platform_3 = Background()
platform_4 = Background()
volume = Music()


# function for gameplay
def start_the_game():
    player = Player()
    enemy = Enemy()
    victim = Victim()

    #making a list, then we will add our bush to the list
    bushes = []
    #making a list, then we will add our berry to the list
    berries = []
    bush = 0
    berry = 0
    background = pygame.image.load("forest.jpg")

    # set variable to keep the loop running
    running = True
    while running:

        ground.platforms(0, 470, 500, 30)
        platform_1.platforms(78, 370, 64, 10)
        platform_2.platforms(182, 303, 75, 15)
        platform_3.platforms(289, 240, 62, 10)
        platform_4.platforms(370, 200, 120, 15)
        kibo_bg.bg_image()

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

        keys = pygame.key.get_pressed()
        player.tick(keys)
        player.jump()
        player.gravity()
        enemy.tick()
        window.blit(background, (0, 0 ))
        player.draw()
        enemy.draw()
        enemy.howling()
        victim.draw()
        victim.jump()

        #drawing our bush and our berry
        for bush in bushes:
            bush.draw()
        for berry in berries:
            berry.draw()

        #drawing our bush and our berry
        for bush in bushes:
            bush.draw()
        for berry in berries:
            berry.draw()

        for event in pygame.event.get():
            # check if it's quiting
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    # change is_jumping from False to True to make player jump
                    player.is_jumping = True
                    jump_sound.play()
                # if it's escape close the game
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            random_jump = random.randint(1, 3)
            if random_jump == 3:
                victim.is_jumping = True

        pygame.display.update()

# define main funtion of the game
def main():

    # set variable to keep the main loop running
    run = True
    # call introduction
    history = instructions()
    history.welcome_text()
    # main loop
    while run:

        # look at every event in the queue
        for event in pygame.event.get():

            # check if it's quiting
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # check if the user hit a key
            if event.type == KEYDOWN:
                # if it's escape close the game
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_RETURN:
                    history.clicking()

            if event.type == MOUSEBUTTONDOWN:
                start_the_game()


# calling the game
def start_the_intro():
    if __name__ == "__main__":
        main()

# defining menu options
main_menu = pygame_menu.Menu("Menu", 500, 500, theme=pygame_menu.themes.THEME_GREEN)
main_menu.add.button("Zacznij grę", start_the_intro)
main_menu.add.selector("Poziom głośności:", [("Max",3),("2",2),("1",1),("0", 0)], onchange = volume.adjust_volume)
main_menu.add.button("Wyjdź", pygame_menu.events.EXIT)

# calling menu
main_menu.mainloop(window)


# this line is unnecessary
# pygame.quit()
