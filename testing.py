import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
background_image = pygame.image.load('Assets/backgrounds/officeBackground.png')
background_image = pygame.transform.scale(background_image, (display_width, display_height))

def car(x, y):
    gameDisplay.blit(background_image, (x, y))


x = (display_width * 0.0)
y = (display_height * 0.0)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()