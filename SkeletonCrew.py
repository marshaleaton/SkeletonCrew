import pygame
from Level import Level
from Path import base_path

from GameStates import GameState

current_state = GameState.Start
pygame.init()
pygame.key.set_repeat(10)
display_width = 800
display_height = 650
banner_height = 50
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Skeleton Crew')
level = Level(display_width, display_height-banner_height)
level.load_level()

title_image = pygame.transform.scale(pygame.image.load(base_path+"Assets/backgrounds/titlescreen.png"), (display_width, display_height))
win_screen_image = pygame.transform.scale(pygame.image.load(base_path+"Assets/backgrounds/winscreen.png"), (display_width, display_height))
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if current_state == GameState.Start:
                current_state = GameState.Game
            elif current_state == GameState.Game:
                level.handle_input(event.key)

    if current_state == GameState.Start:
        game_display.blit(title_image, (0, 0))
    elif current_state == GameState.Win:
        game_display.blit(win_screen_image, (0, 0))
    else:
        if level.all_complete:
            current_state = GameState.Win
        if level.check_for_collisions():
            level.player.undo_last_move()

        game_display.fill(white)
        level.draw_level(game_display)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()