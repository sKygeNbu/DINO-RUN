import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
    def __init__(self, obstacle_type):
        self.type = obstacle_type
        image = SMALL_CACTUS if self.type == 0 else LARGE_CACTUS
        super().__init__(image, self.type)
        self.rect.y = 325 if self.type == 0 else 300

