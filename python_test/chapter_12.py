import sys
import pygame

# 12-1 12-2
class blue_window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.bg_color = (0, 0, 255)
        self.char = character(self)
        pygame.display.set_caption("blue window")

    def run(self):
        self.screen.fill(self.bg_color)
        self.char.blitme()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


class character:
    def __init__(self, window):
        self.screen = window.screen
        self.screen_rect = window.screen.get_rect()
        self.image = pygame.image.load('characters.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    bw = blue_window()
    bw.run()
