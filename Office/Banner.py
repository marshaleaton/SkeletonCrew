import pygame
import os
from Path import base_path


class Banner(object):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
        self.width = 800
        self.height = 50
        self.position = (0,600)
        self.number_loc = (170, 600)
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.water_locations = [(560,602),(602, 602),(641,602)]

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(base_path+"Assets/images/bottombanner.png")
        self.water_image = pygame.image.load(base_path+"Assets/images/waterfull.png")
        self.level_images = [
            pygame.image.load(base_path + "Assets/images/1.png"),
            pygame.image.load(base_path + "Assets/images/2.png"),
            pygame.image.load(base_path + "Assets/images/3.png"),
            pygame.image.load(base_path + "Assets/images/4.png"),
            pygame.image.load(base_path + "Assets/images/5.png"),
        ]
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def draw(self, game_display, level, water_amount):
        game_display.blit(self.image, self.position)
        game_display.blit(self.level_images[level], self.number_loc)
        if water_amount > 0:
            game_display.blit(self.water_image, self.water_locations[0])
        if water_amount > 1:
            game_display.blit(self.water_image, self.water_locations[1])
        if water_amount > 2:
            game_display.blit(self.water_image, self.water_locations[2])