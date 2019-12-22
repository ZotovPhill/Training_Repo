import pygame
from pygame.sprite import Sprite


class Alien(
    Sprite
):  # Класс наследует от Sprite для группировки отдельных элементов по аналогии с пулями
    def __init__(
        self, game_settings, screen
    ):  # Инициализируем пришельца и задаем ему начальную позицию
        super().__init__()  # Наседуем элементы родительского класса Sprite
        self.screen = screen  # Инициализируем параметры
        self.game_settings = game_settings

        self.image = pygame.image.load(
            "images/spaceships.bmp"
        )  # Загружаем картинку космического корабля пришельцев
        self.rect = (
            self.image.get_rect()
        )  # Создаем прямоугольную область и оборачиваем в нее изображение методом get_rect()
        self.screen_rect = (
            screen.get_rect()
        )  # Прямой необходимости пока не наблюдается, в дальнейшем возможно пригодится для отображения границ

        self.rect.x = (
            self.rect.width
        )  # Каждый новый пришелец появляется в левом верхнем углу экрана, его координаты задаются
        self.rect.y = self.rect.height

        self.x = float(
            self.rect.x
        )  # Сохранение точной позиции пришельца, приведение к типу float

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if (
            self.rect.right >= screen_rect.right
        ):  # проверка если атрибут пришельца будет больше атрибуту правого края экрана, вернуть True
            return True
        elif (
            self.rect.left <= 0
        ):  # если позиция прямоугольника пришельца меньше или 0 то вернуть True
            return True

    def update(self):
        """Перемещает пришельца вправо"""
        self.x += (
            self.game_settings.alien_speed_factor * self.game_settings.fleet_direction
        )  # При каждом обновлении пришельца позиция его смещается на величину скорости, в данном случае если значение будет отрицательным смещение будет в обратную сторону
        self.rect.x = (
            self.x
        )  # Значение используется для обновления прямоугольника пришельца

    def blitme(
        self,
    ):  # Выводит изображение методом blit в который передаются параметры изображение и прямоугольная оболочка
        self.screen.blit(self.image, self.rect)
