class GameStats():
    """Статистика игры"""

    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.reset_stats() 
        self.game_active = False # флаг активного состояния игры
        self.record = 0

    def reset_stats(self):
        """Инициализирует статистику, которая будет изменяться в процессе игры"""
        self.ships_count = self.game_settings.ship_count # Инициализирует количество кораблей которое будет доступно игроку
        self.score = 0 # Инициализируем количество очков
        self.level = 1