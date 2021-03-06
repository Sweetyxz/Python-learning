import sys
import pygame
from setting import settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import Game_Stats
from button import Button
from time import sleep
from scoreboard import Scoreboard


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
        self.stats = Game_Stats(self)
        self.play_button = Button(self, 'Play')
        self.high_level = Button(self, 'High')
        self.low_level = Button(self, 'Low')
        self.sb = Scoreboard(self)

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
        elif event.key == pygame.K_p:
            self._start_game()

    def check_keyup_event(self, event):  # 飞船的松开键盘检查
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active and not self.stats.level_button_state:
            self.stats.game_active = True
            self._start_game()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            pygame.mouse.set_visible(False)

    def check_highlevel_button(self, mouse_pos):
        if self.high_level.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.settings.high_level_speed()
            self.stats.level_button_state = False

    def check_lowlevel_button(self, mouse_pos):
        if self.low_level.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.settings.init_dynamic_settings()
            self.stats.level_button_state = False

    def check_event(self):  # 事件判断
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
                self.check_highlevel_button(mouse_pos)
                self.check_lowlevel_button(mouse_pos)

    def _start_game(self):
        self.stats.reset_stats()
        self.aliens.empty()
        self.bullets.empty()
        self.creat_aliens()
        self.ship.center_ship()

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

    def cheak_edge(self):  # 检测外星人是否到达边缘
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.alien_down()
                break

    def alien_down(self):  # 外星人到达边缘后下沉 改变方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_direction *= -1

    def ship_hit(self):   # 外星人撞到飞船后进行的操作
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self.creat_aliens()
            self.ship.center_ship()

            sleep(0.5)
        else:
            with open('high_score.txt', 'w') as f:
                f.write(str(self.stats.high_score))
            self.stats.game_active = False
            self.stats.level_button_state = True
            pygame.mouse.set_visible(True)

    def check_alien_bottom(self):  # 检查外星人是否到达底部
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def update_aliens(self):  # 外星人不断移动
        self.cheak_edge()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        self.check_alien_bottom()

    def update_screen(self):  # 屏幕更新
        self.screen.fill(self.settings.bg_color)
        self.ship.biteme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)  # aliens编组的绘制
        self.sb.show_score()

        if not self.stats.game_active and not self.stats.level_button_state:
            self.play_button.draw_button()

        if self.stats.level_button_state:
            self.high_level.change_position(self.settings.screen_width/2 - self.high_level.width, self.settings.screen_height/2)
            self.low_level.change_position(self.settings.screen_width/2 + 20, self.settings.screen_height/2)
            self.high_level.draw_button()
            self.low_level.draw_button()

        pygame.display.flip()  # 绘制的屏幕可见

    def update_buttle(self):  # 更新子弹
        self.bullets.update()

        for bullet in self.bullets.copy():  # 使用编组的副本,子弹从屏幕消失时，移除子弹
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(  # 检测碰撞
            self.bullets, self.aliens, True, True)

        if collisions:  # 碰撞后分数增加
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()  # 删除子弹中的余下sprite
            self.creat_aliens()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def run_game(self):  # 循环判断事件更新屏幕
        while True:
            self.check_event()
            if self.stats.game_active:
                self.ship.updata()
                self.update_buttle()
                self.update_aliens()
            self.update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
