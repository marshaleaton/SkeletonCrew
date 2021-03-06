import pygame


class Wall(object):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, position, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.color = (0,0,128)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.position = position
        self.width = width
        self.height = height
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = pygame.Rect(position[0], position[1], width, height)

    def draw(self, game_display):
        pygame.draw.rect(game_display, self.color, (self.position[0], self.position[1], self.width, self.height), 0 )