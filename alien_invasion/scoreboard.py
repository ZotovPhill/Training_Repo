import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    def __init__(self, game_settings, screen, stats):
        """Инициализируем атрибуты количества очков"""
        self.game_settings = game_settings
        self.screen = screen
        self.stats = stats

        self.screen_rect = screen.get_rect()

        # Настраиваем шрифты для поля вывода очков
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 60)
        self.prep_score()  # Метод преобразования текущего счета в изображение на экране
        self.prep_record_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразование счета в изображение"""
        rounded_score = int(round(self.stats.score, -1))  # Округление числа до десятков
        score_str = "{:,}".format(rounded_score)  # Группы разрядов раделяются запятой
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20

    def prep_record_score(self):
        round_record = int(round(self.stats.record, -1))
        record_str = "{:,}".format(round_record)
        self.record_image = self.font.render(record_str, True, self.text_color)

        self.record_rect = self.record_image.get_rect()
        self.record_rect.right = self.screen_rect.right
        self.record_rect.top = 20

    def prep_level(self):
        self.level_font = pygame.font.SysFont(None, 200)
        self.level_image = self.level_font.render(
            str(self.stats.level), True, self.text_color
        )

        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.screen_rect.centerx

    def prep_ships(self):
        """Вывод изображения осавшихся кораблей на интерфейс"""
        self.ships = (
            Group()
        )  # Создаем группу которая будет хранить в себе спрайты объестов Ship
        for ship_number in range(self.stats.ships_count):
            ship = Ship(
                self.game_settings, self.screen
            )  # Создаем экземпляр типа Ship и размещаем их рядом друг с другом
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Вывод изображения на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.record_image, self.record_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(
            self.screen
        )  # Метод draw вызываем для группы, pygame рисует прорисовывает отдельно каждый

