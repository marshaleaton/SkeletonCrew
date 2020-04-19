import pygame


class WaterCooler(object):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, position):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 50
        self.image = pygame.image.load("Assets/images/watercooler.png")
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.color = (144, 202, 249)
        self.position = position
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)

    def draw_rect(self, game_display):
        pygame.draw.rect(game_display, self.color, (self.position[0], self.position[1], self.width, self.height), 0 )