import pygame
from Office.Background import Background
from Player import Player




pygame.init()
pygame.key.set_repeat(10)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode(())
pygame.display.set_caption('Skeleton Crew')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
background = Background(display_width, display_height)
player = Player()

def renderScreen(x, y):
    gameDisplay.blit(background.image, (x, y))
    gameDisplay.blit(player.image, player.position)


x = (display_width * 0.0)
y = (display_height * 0.0)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_LEFT:
                player.move_left()
    print(pygame.sprite.collide_mask(background, player))

    gameDisplay.fill(white)
    renderScreen(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()