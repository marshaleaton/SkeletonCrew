import pygame
from Path import base_path

class Player(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, position):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.water_level = 0
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.idle_image = pygame.image.load(base_path + "Assets/images/player/down_rest.png")
        self.image = self.idle_image
        self.position = position
        self.speed = 5
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.last_position = position
        self.animation_shift = 10
        self.animation_frame = 0
        self.up_animation = [pygame.image.load(base_path + "Assets/images/player/up_mid.png"),
                             pygame.image.load(base_path + "Assets/images/player/up_rest.png")]
        self.down_animation = [pygame.image.load(base_path + "Assets/images/player/down_mid.png"),
                               pygame.image.load(base_path + "Assets/images/player/down_rest.png")]
        self.left_animation = [pygame.image.load(base_path + "Assets/images/player/left_mid.png"),
                               pygame.image.load(base_path + "Assets/images/player/left_rest.png")]
        self.right_animation = [pygame.image.load(base_path + "Assets/images/player/right_mid.png"),
                                pygame.image.load(base_path + "Assets/images/player/right_rest.png")]
        self.rest_animation = [self.idle_image]
        self.current_animation = self.down_animation
        self.animation_key = 0

    def move_down(self):
        self.last_position = self.position
        self.position = tuple(map(lambda i, j: i + j, self.position, (0, self.speed)))
        self.update_rect()
        if self.current_animation != self.down_animation or self.animation_key >= len(self.down_animation):
            self.animation_frame = 0
            self.current_animation = self.down_animation
            self.animation_key = 0

    def move_up(self):
        self.last_position = self.position
        self.position = tuple(map(lambda i, j: i - j, self.position, (0, self.speed)))
        self.update_rect()
        if self.current_animation != self.up_animation or self.animation_key >= len(self.up_animation):
            self.animation_frame = 0
            self.current_animation = self.up_animation
            self.animation_key = 0

    def move_left(self):
        self.last_position = self.position
        self.position = tuple(map(lambda i, j: i - j, self.position, (self.speed, 0)))
        self.update_rect()
        if self.current_animation != self.left_animation or self.animation_key >= len(self.left_animation):
            self.animation_frame = 0
            self.current_animation = self.left_animation
            self.animation_key = 0

    def move_right(self):
        self.last_position = self.position
        self.position = tuple(map(lambda i, j: i + j, self.position, (self.speed, 0)))
        self.update_rect()
        if self.current_animation != self.right_animation or self.animation_key >= len(self.right_animation):
            self.animation_frame = 0
            self.current_animation = self.right_animation
            self.animation_key = 0

    def undo_last_move(self):
        self.position = self.last_position
        self.image = self.idle_image

    def update_rect(self):
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def animate(self):
        self.animation_frame += 1
        if self.animation_key >= len(self.current_animation):
            self.image = self.current_animation[len(self.current_animation)-1]
        else:
            self.image = self.current_animation[self.animation_key]
            if self.animation_frame > self.animation_shift:
                self.animation_frame = 0
                self.animation_key += 1

