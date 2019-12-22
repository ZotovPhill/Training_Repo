import pygame.font # Модуль позволяет выводить текст на экран
import pygame.gfxdraw

class Button():
    def __init__(self, game_settings, screen, msg):
        """Инициализируем атрибуты кнопки"""
        self.game_settings = game_settings
        self.screen = screen        
        self.screen_rect = screen.get_rect() # Получаем прямоугольник экрана

        # Назначение размеров и свойств кнопки
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255, 128)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0,0, self.width, self.height) # Создаем прямоугольник интерфейса помещаем его в позицию 0,0 с размерами self.width, self.height
        self.rect.center = self.screen_rect.center # Помещаем прямоугольник в центр экрана, создаем объект rect с атрибутом center

        self.prep_msg(msg) # Сообщение создается только один раз

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает теуст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) # Выводит строку в виде графического текста (сообщение, режим сглаживания, цвет шрифта и цвет фона)
        self.msg_image_rect = self.msg_image.get_rect() # Получаем прямоугольный объект изображения текста  
        self.msg_image_rect.center = self.rect.center # Помещаем его в центре прямоугольника интерфейса

    def draw_button(self):
        """Отображение кнопки и вывод сообщения"""
        self.screen.fill(self.button_color, self.rect) # Рисует прямоугольную часть кнопки
        self.screen.blit(self.msg_image, self.msg_image_rect) # Выводит изображение на экран