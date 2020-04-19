import pygame
from Player import Player
from Office.Banner import Banner
from Office.Wall import Wall
from Office.WaterCooler import WaterCooler
from Office.Tree import Tree
from Office.Plant import Plant
from Office.Desk import Desk
from Office.Background import Background
from LevelDefinitions import levels
from Path import base_path

class Level(object):

    def __init__(self, width, height):
        # Sprites for the level
        self.max_water_level = 3
        self.level_data = levels
        self.walls = []
        self.water_sources = []
        self.plants = []
        self.furniture = []
        self.background_image = None
        self.showStructure = True
        self.player = None
        self.level_number = 0
        self.max_level = len(self.level_data)
        self.width = width
        self.height = height
        self.level_complete = False
        self.all_complete = False
        self.water_sound = pygame.mixer.Sound(base_path + "Assets/sounds/watercooler.ogg")
        self.water_sound.set_volume(.1)
        self.banner = Banner()

    # Take a level definition as a python dict
    def load_level(self):
        level_definition = self.level_data[self.level_number]
        self.background = Background(level_definition.get("background image", "Assets/backgrounds/officeBackground"),
                                     self.width, self.height)
        self.player = Player(level_definition.get("player", {}).get("starting position", (0, 0)))
        self.showStructure = level_definition.get("structure", False)
        self.walls = self.create_walls(level_definition.get("walls", []))
        self.water_sources = self.create_water_features(level_definition.get("water sources", []))
        self.plants = self.create_plants(level_definition.get("plants", []))
        self.furniture = self.create_furniture(level_definition.get("furniture", []))

    def create_walls(self, wall_definitions):
        wall_sprites = []
        for wall in wall_definitions:
            wall_sprites.append(Wall(wall.get("position", (0, 0)), wall.get("width", 0), wall.get("height", 0)))
        return wall_sprites

    def create_water_features(self, water_definitions):
        water_sprites = []
        for water_feature in water_definitions:
            if water_feature.get("type", "") == "watercooler":
                water_sprites.append(WaterCooler(water_feature.get("position", (0, 0))))
        return water_sprites

    def create_plants(self, plant_definitions):
        plant_sprites = []
        for plant in plant_definitions:
            if plant.get("type", "") == "tree":
                plant_sprites.append(Tree(plant.get("position", (0, 0))))
            elif plant.get("type", "") == "plant":
                plant_sprites.append(Plant(plant.get("position", (0, 0))))
        return plant_sprites

    def create_furniture(self, furniture_definitions):
        furniture_sprites = []
        for furniture in furniture_definitions:
            if furniture.get("type", "") == "desk":
                furniture_sprites.append(Desk(furniture.get("position", (0, 0))))
        return furniture_sprites

    def check_for_collisions(self):
        for wall in self.walls:
            if pygame.sprite.collide_rect(wall, self.player):
                return True
        return False

    def check_for_water(self):
        for water_source in self.water_sources:
            if pygame.sprite.collide_rect(water_source, self.player):
                return True
        return False

    def water_plant(self):
        for plant in self.plants:
            if pygame.sprite.collide_rect(plant, self.player):
                if not plant.watered:
                    self.player.water_level -= 1
                    plant.water()
                    return True
        return False

    def check_for_completion(self):
        for plant in self.plants:
            if not plant.watered:
                return False
        return True

    def next_level(self):
        if self.level_complete:
            self.level_complete = False
            self.level_number += 1
            if self.level_number > self.max_level-1:
                self.all_complete = True
            else:
                self.load_level()

    def handle_input(self, key):
        if key == pygame.K_DOWN or key == pygame.K_s:
            self.player.move_down()
        if key == pygame.K_UP or key == pygame.K_w:
            self.player.move_up()
        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.player.move_right()
        if key == pygame.K_LEFT or key == pygame.K_a:
            self.player.move_left()
        if key == pygame.K_SPACE:
            if self.check_for_water():
                self.player.water_level = self.max_water_level
                self.water_sound.play()
            if self.player.water_level > 0:
                self.water_plant()
                self.level_complete = self.check_for_completion()


    def draw_level(self, game_display):
        self.banner.draw(game_display, self.level_number, self.player.water_level)
        game_display.blit(self.background.image, (0, 0))
        if self.showStructure:
            for wall in self.walls:
                wall.draw(game_display)
            for plant in self.plants:
                plant.draw_rect(game_display)
            for water_source in self.water_sources:
                water_source.draw_rect(game_display)

        for plant in self.plants:
            game_display.blit(plant.image, plant.position)
        for water_source in self.water_sources:
            game_display.blit(water_source.image, water_source.position)
        for furniture in self.furniture:
            game_display.blit(furniture.image, furniture.position)
        game_display.blit(self.player.image, self.player.position)

