import pygame
import sys
from pygame.sprite import Sprite
from random import randint


class Screen():
    def __init__(self):
        pygame.init()
        self.Screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Star Show")
        self.bg_color = (255, 255, 255)
        self.stars = pygame.sprite.Group()
        self.creat_star_row()

    def creat_star_row(self):
        new_star = Star(self)
        star_width = new_star.rect.width + 10
        star_height = new_star.rect.height + 10
        allow_x = 600 - 2 * star_width
        max_x_num = allow_x // star_width

        allow_y = 800 - 2 * star_height
        max_y_num = allow_y // star_height

        for j in range(max_y_num):
            random_number = randint(2, max_x_num)  # 每行随机个星星
            print(random_number)
            allow_x_star = allow_x // random_number
            for i in range(1, random_number):
                rect_x = star_width + allow_x_star * i
                rect_y = star_height + star_height * j
                self.creat_star(rect_x, rect_y)

    def creat_star(self, rect_x, rect_y):
        new_star = Star(self)
        new_star.rect.x = rect_x
        new_star.rect.y = rect_y
        self.stars.add(new_star)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        self.Screen.fill(self.bg_color)
        self.stars.draw(self.Screen)
        pygame.display.flip()

    def run(self):
        while True:
            self.check_event()
            self.update_screen()


class Star(Sprite):
    """docstring for Star"""
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load("star.jpg")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


if __name__ == '__main__':
    st = Screen()
    st.run()
