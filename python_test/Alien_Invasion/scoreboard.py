import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    def __init__(self, aigame):
        self.aigame = aigame
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = aigame.settings
        self.stats = aigame.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 35)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):  # 显示分数部分
        rounded_score = round(self.stats.score, -1)  #round函数第二个参数表示精确到小数点后几位，设置为-1表示舍入到最近的10的整数倍
        score_str = "score:" + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):  # 最高分部分
        high_score = round(self.stats.high_score, -1)
        high_score_str = "high score:" + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def check_high_score(self):  # 检查当前分数是否超过了最高分数
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = "level:" + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.aigame)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
