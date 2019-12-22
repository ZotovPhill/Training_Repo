import pygame
from pygame.sprite import Sprite #стандартный класс для видимых объектов

class Bullet(Sprite): # Класс Bullet наследует от класса Sprite (работая со спрайтами мы группируем связанные элементы и выполняем операцию со всеми элементами группы одновременно)
    def __init__(self, game_settings, ship, screen):
        #Создает объект пули в текущей позиции корабля
        super(Bullet, self).__init__() # Реализация наследования от Sprite / в Python3 синтаксис можно записать в форме super().__init__()
        self.screen = screen

        # Создание пули в позиции (0, 0) и назначение правильной позиции, пуля строится с нуля при помощи класса pygame.Rect()
        # В кач-ве параметров задаем парметры прямоугольника(коорд левого правого угла X, Y, ширина, высота)
        self.rect = pygame.Rect(0,0, game_settings.bullet_width, game_settings.bullet_height) 
        self.rect.centerx = ship.rect.centerx # Перемещаем модель центра пули в нужное место в центр и верхушку прямоугольника корабля
        self.rect.top = ship.rect.top
        

        # Позиция пули хранится в вещественном формате (тк пуля будет перемещаться по оси Y то нет необходимости задавать координаты х)
        self.y = float(self.rect.y)

        # Настройки цвета и скорости сохраняются в переменных
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
            # Перемещение пули вверх по экрану
        self.y -= self.speed_factor # Текущая позиции - величина текущей скорости (соответствует уменьшению координаты у)
        self.rect.y = self.y # Обновление текущей позиции прямоугольники

    def draw_bullet(self):
            # Вывод пули на экран
        pygame.draw.rect(self.screen, self.color, self.rect) # метод из pygame в кач-ве параметров выделяем экран прорисовки объекта, цвет и сам объект прямоугольника