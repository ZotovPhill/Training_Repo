import pygame
from pygame.sprite import Sprite


class MilkyWay(Sprite):
    def __init__(self, game_settings, screen):
        super().__init__()
        self.game_settings = game_settings
        self.screen = screen

        self.image = pygame.image.load("images/rock.bmp")

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.height = -200

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.star_x = float(self.rect.x)
        self.star_y = float(self.rect.y)

        self.star_speed = game_settings.star_speed_factor

    def update(self):
        self.star_y += self.star_speed
        self.rect.y = self.star_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
