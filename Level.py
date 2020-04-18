from Player import Player
from Office.Wall import Wall


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
    def loadLevel(self, level_definition):
        self.player = Player(level_definition.get("player", {}).get("position", (0, 0)))
        self.walls = self.createWalls(level_definition.get("walls", []))

    def createWalls(self, wall_definitions):
        wall_sprites = []
        for wall in wall_definitions:
            wall_sprites.append(Wall(wall.get("position", (0, 0)), wall.get("width", 0), wall.get("height", 0)))
        return wall_sprites

    def drawLevel(self, game_display):
        pass
