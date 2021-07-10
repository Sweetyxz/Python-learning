import pygame


class Ship:
    """飞船类"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # 变成矩形操作
        self.rect.midbottom = self.screen_rect.midbottom  # 矩形放在底部中央

    def biteme(self):
        self.screen.blit(self.image, self.rect)  # 绘制图像
