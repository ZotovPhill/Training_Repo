import sys
import pygame
from threading import Timer


class Settings:
    def __init__(self):
        """Иинциализируем настойки игры, переносим файл конфигурации и параметров игры в отдельный модуль"""
        # задаем настройки экрана и цвет фона
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (142, 148, 231)

        self.ship_count = 3

        self.alien_speed_factor = 3
        self.fleet_drop_speed = 20
        self.fleet_direction = 1  # '1' - вправо/ '-1' - влево

        self.star_speed_factor = 15

        # Задаем параметры пули
        self.bullet_height = 15
        self.bullet_color = (230, 50, 50)
        self.bullets_allowed = 10

        self.game_temp = 1.1
        self.score_modificator = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 10

        self.alien_speed_factor = 3
        self.fleet_drop_speed = 20
        self.fleet_direction = 1  # '1' - вправо/ '-1' - влево
        self.alien_score = 25

        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullets_through = False

    def increase_speed(self):
        self.ship_speed_factor = self.ship_speed_factor - (
            self.alien_speed_factor * 0.01
        )
        self.alien_speed_factor *= self.game_temp
        self.alien_score = int(self.alien_score * self.score_modificator)

    def decrease_speed(self):
        self.ship_speed_factor = self.ship_speed_factor + (
            self.alien_speed_factor * 0.01
        )
        self.alien_speed_factor /= self.game_temp

