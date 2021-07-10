import sys
import pygame
from setting import settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)  # self指向当前实例

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.biteme()
        pygame.display.flip()  # 绘制的屏幕可见

    def run_game(self):
        while True:
            self.check_event()
            self.update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
