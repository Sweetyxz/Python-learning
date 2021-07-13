import sys
import pygame
from pygame.sprite import Sprite


# 12-1 12-2 12-3 1204 12-5
'''
class blue_window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.bg_color = (0, 0, 255)
        self.char = character(self)
        pygame.display.set_caption("blue window")

    def keydown_check(self, event):
        if event.key == pygame.K_LEFT:
            self.char.move_left = True
        elif event.key == pygame.K_RIGHT:
            self.char.move_right = True
        elif event.key == pygame.K_UP:
            self.char.move_up = True
        elif event.key == pygame.K_DOWN:
            self.char.move_down = True

    def keyup_check(self, event):
        if event.key == pygame.K_LEFT:
            self.char.move_left = False
        elif event.key == pygame.K_RIGHT:
            self.char.move_right = False
        elif event.key == pygame.K_UP:
            self.char.move_up = False
        elif event.key == pygame.K_DOWN:
            self.char.move_down = False

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)  # 检查按键按下后输出的值
                self.keydown_check(event)
            elif event.type == pygame.KEYUP:
                self.keyup_check(event)

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.char.blitme()
        pygame.display.flip()

    def run(self):
        while True:
            self.check_event()
            self.char.move()
            self.update_screen()


class character:
    def __init__(self, window):
        self.screen = window.screen
        self.screen_rect = window.screen.get_rect()
        self.image = pygame.image.load('characters.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def move(self):
        if self.move_left and self.rect.left > 0:
            self.rect.x -= 1
        elif self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        elif self.move_up and self.rect.top > 0:
            self.rect.y -= 1
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    bw = blue_window()
    bw.run()
'''


# 12-6
class blue_window:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.bg_color = (0, 0, 255)
        self.char = character(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("blue window")

    def keydown_check(self, event):
        if event.key == pygame.K_UP:
            self.char.move_up = True
        elif event.key == pygame.K_DOWN:
            self.char.move_down = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def keyup_check(self, event):
        if event.key == pygame.K_UP:
            self.char.move_up = False
        elif event.key == pygame.K_DOWN:
            self.char.move_down = False

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)  # 检查按键按下后输出的值
                self.keydown_check(event)
            elif event.type == pygame.KEYUP:
                self.keyup_check(event)

    def fire_bullet(self):
        new_bullet = bullet(self)
        self.bullets.add(new_bullet)

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.char.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def run(self):
        while True:
            self.check_event()
            self.char.move()
            self.bullets.update()
            for bullet in self.bullets:
                if bullet.rect.left > 500:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            self.update_screen()


class character:
    def __init__(self, window):
        self.screen = window.screen
        self.screen_rect = window.screen.get_rect()
        self.image = pygame.image.load('characters.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.left
        self.move_up = False
        self.move_down = False

    def move(self):
        if self.move_up and self.rect.top > 0:
            self.rect.y -= 1
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.bullet_speed = 1
        self.color = (60, 60, 60)
        self.height = 10
        self.width = 30

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midleft = ai_game.char.rect.midleft

    def update(self):
        self.rect.x += self.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(
            self.screen, self.color, self.rect)


if __name__ == '__main__':
    bw = blue_window()
    bw.run()
