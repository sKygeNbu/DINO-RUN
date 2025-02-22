import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.choice([0, 1, 2])
            self.obstacles.append(Cactus(obstacle_type))
        
        for obstacle in self.obstacles.copy():
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)