import pygame
from Player import Player
from Office.Wall import Wall
from Office.WaterCooler import WaterCooler
from Office.Tree import Tree
from Office.Desk import Desk
from Office.Background import Background

class Level(object):

    def __init__(self):
        # Sprites for the level
        self.walls = []
        self.water_sources = []
        self.plants = []
        self.furniture = []
        self.background_image = None
        self.showStructure = True
        self.player = None
        self.level_number = 0

    # Take a level definition as a python dict
    def load_level(self, level_definition, display_width, display_height):
        self.background = Background(level_definition.get("background image", "Assets/backgrounds/officeBackground"),
                                     display_width, display_height)
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
                self.player.has_water = False
                plant.watered = True
                return True
        return False

    def check_for_completion(self):
        for plant in self.plants:
            if not plant.watered:
                return False
        return True


    def draw_level(self, game_display):
        game_display.blit(self.background.image, (0, 0))
        game_display.blit(self.player.image, self.player.position)
        if self.showStructure:
            for wall in self.walls:
                wall.draw(game_display)
            for plant in self.plants:
                plant.draw_rect(game_display)
            for water_source in self.water_sources:
                water_source.draw_rect(game_display)
