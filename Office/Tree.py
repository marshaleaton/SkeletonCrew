import pygame
from Path import base_path

class Tree(object):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, position):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 50
        self.x_offset = 5
        self.y_offset = 20
        self.dry = pygame.image.load(base_path + "Assets/images/tree_dry.png")
        self.wet = pygame.image.load(base_path + "Assets/images/tree_wet.png")
        self.image = self.dry
        self.color = (0, 100, 0)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.watered = False
        self.position = position
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = pygame.Rect(position[0]-self.x_offset, position[1]+self.y_offset, self.width, self.height)

    def draw_rect(self, game_display):
        pygame.draw.rect(game_display, self.color, (self.position[0]-self.x_offset, self.position[1]+self.y_offset, self.width, self.height), 0 )
    def water(self):
        self.watered = True
        self.image = self.wet