import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # 子弹类
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.color = self.settings.bullet_color
        self.speed = self.settings.bullet_speed

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(
            self.screen, self.color, self.rect)  # 用来填充子弹矩形rect位置的颜色