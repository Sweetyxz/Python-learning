import sys
import pygame
from setting import settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.aliens = pygame.sprite.Group()

        self.creat_aliens()

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

    def fire_bullet(self):  # 子弹添加到编组中
        if len(self.bullets) < self.settings.bullet_number_allowed:
            bullet = Bullet(self)  # 实例化bullet元素
            self.bullets.add(bullet)  # 添加到编组中

    def creat_aliens(self):  # 创建外星人编组
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        avail_space_x = self.settings.screen_width - alien_width * 2
        number_alien_x = avail_space_x // (alien_width * 2)

        ship_height = self.ship.rect.height
        avail_space_y = (self.settings.screen_height - 
            (alien_height * 3) - ship_height)
        number_rows = avail_space_y // (2 * alien_height)
        for row in range(number_rows):
            for alien_number in range(number_alien_x):
                self.creat_alienrow(alien_number, row)

    def creat_alienrow(self, alien_number, alien_row):  # 添加指定位置的外星人
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + alien_width * 2 * alien_number
        alien.y = alien_height + alien_height * 2 * alien_row
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def update_aliens(self):  # 外星人不断移动
        self.cheak_edge()
        self.aliens.update()

    def cheak_edge(self):  # 检测外星人是否到达边缘
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.alien_down()
                break

    def alien_down(self):  # 外星人到达边缘后下沉 改变方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_direction *= -1

    def update_screen(self):  # 屏幕更新
        self.screen.fill(self.settings.bg_color)
        self.ship.biteme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)  # aliens编组的绘制
        pygame.display.flip()  # 绘制的屏幕可见

    def update_buttle(self):  # 更新子弹
        self.bullets.update()

        for bullet in self.bullets.copy():  # 使用编组的副本,子弹从屏幕消失时，移除子弹
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(  # 检测碰撞
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()  # 删除子弹中的余下sprite
            self.creat_aliens()

    def run_game(self):  # 循环判断事件更新屏幕
        while True:
            self.check_event()
            self.ship.updata()
            self.update_buttle()
            self.update_aliens()
            self.update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
