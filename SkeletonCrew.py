import pygame
from Player import Player
from Level import Level
from LevelDefinitions import levels

game_screen = "start"
pygame.init()
pygame.key.set_repeat(10)
display_width = 800
display_height = 650
banner_height = 50
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Skeleton Crew')
current_level = Level()
current_level.load_level(levels[0], display_width, display_height-banner_height)
max_level = 1
black = (0, 0, 0)
white = (255, 255, 255)
level_complete = False
clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if level_complete:
            current_level.level_number += 1
            if current_level.level_number > max_level:
                #Success the game is over
                pass
            else:
                current_level.load_level(levels[current_level.level_number], display_width, display_height-banner_height)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                current_level.player.move_down()
            if event.key == pygame.K_UP:
                current_level.player.move_up()
            if event.key == pygame.K_RIGHT:
                current_level.player.move_right()
            if event.key == pygame.K_LEFT:
                current_level.player.move_left()
            if event.key == pygame.K_SPACE:
                if current_level.check_for_water():
                    current_level.player.has_water = True
                if current_level.player.has_water:
                    current_level.water_plant()
                    level_complete = current_level.check_for_completion()


    if current_level.check_for_collisions():
        current_level.player.undo_last_move()



    gameDisplay.fill(white)
    current_level.draw_level(gameDisplay)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()