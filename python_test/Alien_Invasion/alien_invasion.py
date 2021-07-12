import sys
import pygame
from setting import settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = settings()

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 全屏
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
           (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # self指向当前实例

        self.bullets = pygame.sprite.Group()

    def check_keydown_event(self, event):  # 飞船的按下键盘检查
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_event(self, event):  # 飞船的松开键盘检查
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def check_event(self):  # 事件判断
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_number_allowed:
            bullet = Bullet(self)  # 实例化bullet元素
            self.bullets.add(bullet)  # 添加到编组中

    def update_screen(self):  # 屏幕更新
        self.screen.fill(self.settings.bg_color)
        self.ship.biteme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()  # 绘制的屏幕可见

    def update_buttle(self):
        self.bullets.update()

        for bullet in self.bullets.copy():  #使用编组的副本
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def run_game(self):  # 循环判断事件更新屏幕
        while True:
            self.check_event()
            self.ship.updata()
            self.update_buttle()
            self.update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
