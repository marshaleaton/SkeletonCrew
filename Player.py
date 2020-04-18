import pygame


class Player(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, position):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load("Assets/images/player.png")
       self.position = position
       self.speed = 5
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.mask = pygame.mask.from_surface(self.image)

    def move_down(self):
        self.position = tuple(map(lambda i, j: i + j, self.position, (0,self.speed)))

    def move_up(self):
        self.position = tuple(map(lambda i, j: i - j, self.position, (0,self.speed)))

    def move_left(self):
        self.position = tuple(map(lambda i, j: i - j, self.position, (self.speed, 0)))

    def move_right(self):
        self.position = tuple(map(lambda i, j: i + j, self.position, (self.speed, 0)))