import pygame
from pygame.sprite import Sprite


class Ship(
    Sprite
):  # класс инициализирует корабль и задает ему начальную позицию, в дальнейшем будет реализовано поведение объекта
    def __init__(
        self, game_settings, screen
    ):  # класс получает два параметра, ссылка self и объект surface на котором выводится корабль
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings  # Инициализируем корабль и задаем его начальную позицию/ Значение game_settings будет передаваться в аргументе при создании экземпляра Ship

        # Загрузка изображения кораблю и получение прямоугольника
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = (
            self.image.get_rect()
        )  # получаем прямоугольик объекта представляющего корабль
        self.screen_rect = (
            screen.get_rect()
        )  # получаем атрибут get_rect (прямоугольник поверхности) поверхности surface

        self.ch_image = pygame.image.load("images/crosshairs-146113_6401.bmp")
        self.ch_rect = self.ch_image.get_rect()

        """В Данных строках мы присваиваем координаты корабля относительно объекта экрана """
        self.rect.centerx = (
            self.screen_rect.centerx
        )  # работая с объектом rect доступны координаты всех сторон и центра
        self.rect.bottom = (
            self.screen_rect.bottom
        )  # тем самым задаем позицию прямоугольнику (centerx, top, bottom, left, right)

        self.ch_rect.centerx = self.screen_rect.centerx
        self.ch_rect.bottom = self.screen_rect.centerx

        self.ship_center = float(
            self.rect.centerx
        )  # Приводим переменную расположения корабля к вещественному типу float
        self.ch_center = float(self.ch_rect.centerx)  # Расположение прицела

        self.moving_right = False  # Флаг перемещение вправо/влево
        self.moving_left = False

    def center_ship(self):
        """Размещение корабля в снизу по центру"""
        self.ship_center = self.screen_rect.centerx
        self.ch_center = self.screen_rect.centerx

    def update(self):
        """ Метод отвечающий за перемещение вправо/влево"""
        # Если значение которое возвр коорд праваго края прямоугольника корабля меньше правого края прямогульника экрана то поехали
        if (
            self.moving_right and self.rect.right < self.screen_rect.right
        ):  # Если флаг перемещения, который замыкается в значении True при возникновении события KEYDOWN, позиция корабля и прицела смещается на 1px
            self.ship_center += self.game_settings.ship_speed_factor
            self.ch_center += self.game_settings.ship_speed_factor
        if (
            self.moving_left and self.rect.left > 0
        ):  # Если значение которое возвр коорд левого края прямоугольника корабля больше по оси ОХ нуля то поехали
            self.ship_center -= self.game_settings.ship_speed_factor
            self.ch_center -= self.game_settings.ship_speed_factor

        self.rect.centerx = (
            self.ship_center
        )  # Обновление позиции корабля и прицела с учетом смещения (float)
        self.ch_rect.centerx = self.ch_center

    def blitme(self):
        """Рисует корабль в текущей позиции. выводит изображение на экран в позиции заданной self.rect"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.ch_image, self.ch_rect)
