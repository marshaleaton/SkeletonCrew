from Player import Player
from Office.Wall import Wall
from Office.WaterCooler import WaterCooler
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

    # Take a level definition as a python dict
    def load_level(self, level_definition, display_width, display_height):
        self.background = Background(level_definition.get("background image", "Assets/backgrounds/officeBackground"),
                                     display_width, display_height)
        self.player = Player(level_definition.get("player", {}).get("position", (0, 0)))
        self.showStructure = level_definition.get("structure", False)
        self.walls = self.createWalls(level_definition.get("walls", []))
        self.water_sources = self.create_water_features(level_definition.get("water sources", []))


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

    def draw_level(self, game_display):
        pass
