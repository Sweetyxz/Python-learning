import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人类"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()  # 变成矩形操作
        self.rect.x = self.rect.width  # 矩形放在左上角
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)  # 关心的是外星人的水平速度
