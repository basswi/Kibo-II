import pygame

pygame.init()

class Background:
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
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

# Main loop
kibo_bg = Background()
ground = Background()
platform_1 = Background()
platform_2 = Background()
platform_3 = Background()
platform_4 = Background()

# Main loop:
run = True

while run:
    ground.platforms(0, 470, 500, 30)
    platform_1.platforms(78, 370, 64, 10)
    platform_2.platforms(182, 303, 75, 15)
    platform_3.platforms(289, 240, 62, 10)
    platform_4.platforms(370, 200, 120, 15)
    kibo_bg.bg_image()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()
pygame.quit()

print("Test git")
