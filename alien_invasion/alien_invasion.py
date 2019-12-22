import sys  # Модуль будет завершать игру по команде игрока
import pygame
from ship import Ship
from alien import Alien
from milky_way import MilkyWay
import game_function as gf
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from background import Background
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Инициализирует игру
    pygame.init()

    game_settings = Settings()
    stats = GameStats(game_settings)

    # Создается объект экрана, задается разрешение и задается надпись на экране
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )  # Аргументы представляют собой кортеж, определяющий размеры игрового поля. Объект screen называется поверхностью
    # Анимация этой поверхности автоматом перерисовывается при каждом проходе основного игрового цикла игры

    scoreboard = Scoreboard(game_settings, screen, stats)

    ship = Ship(
        game_settings, screen
    )  # Создаем объект корабля и передаем в него параметр поверхности
    background = Background([0, 0])

    bullets = (
        Group()
    )  # Создание группы для хранения пуль, создание экземпляра класса pygame.sprite.Group, представляющая список с расширенной функциональностью
    aliens = Group()
    milky_way = Group()

    gf.create_fleet(game_settings, screen, aliens, ship)
    gf.create_stars(game_settings, screen, milky_way)

    pygame.display.set_caption("Alien Invasion")

    play_button = Button(game_settings, screen, "Play!")

    # Запуск основного чикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_event(
            game_settings, screen, ship, aliens, bullets, stats, play_button, scoreboard
        )  # Обработка нажатий клавиш, реализованная в отдельном модуле,
        # требуется передать в качестве параметра ship и  для обработки событий управления кораблем и bullets при обработке клавиши пробел для выстрела
        if stats.game_active:
            ship.update()
            gf.update_stars(game_settings, screen, milky_way)
            gf.update_bullets(
                bullets, aliens, game_settings, screen, ship, stats, scoreboard
            )  # Удаление пуль, вышедших за край экрана и обновлене пуль
            gf.update_aliens(
                game_settings, screen, ship, aliens, bullets, stats, scoreboard
            )  # Вызывает функцию в game_function для изменения позиции пришельцев. Позиции обновляются после обработки пуль, для дальнейшей проверки попадания
        gf.updata_screen(
            game_settings,
            screen,
            ship,
            bullets,
            aliens,
            milky_way,
            background,
            stats,
            play_button,
            scoreboard,
        )  # Функция обновления экрана, передается 4 параметра(класс конфига, объект экрана, объект корабля и пуля для перерисовки выводимой на экран)


run_game()
