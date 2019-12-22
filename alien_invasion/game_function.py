import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from milky_way import MilkyWay
from random import randint


def check_keydown_events(
    event, game_settings, screen, ship, aliens, bullets, stats, scoreboard
):  # Выделим события отпускания и нажатия в отдельные методы, параметр event получает при вызове а вызов происходит в check_event
    if event.key == pygame.K_RIGHT:  # Проверка является ли нажатой следующая клавиша
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # Отслеживаем событие нажатия пробела
        fire_bullet(event, game_settings, screen, ship, bullets)
    elif (
        event.key == pygame.K_q
    ):  # Отбарабатываем нажатие клавиши q, если нажата выходим из игры
        sys.exit()
    elif (
        event.key == pygame.K_r
    ):  # Если пользователь нажал на кнопку R происзодит моментальный перезапуск игры
        restart_game(game_settings, screen, ship, aliens, bullets, stats, scoreboard)
    elif (
        event.key == pygame.K_s and stats.game_active
    ):  # Если нажата кнопка S игра замирает и у пользователя есть возможность оценить шансы или сделать перерыв
        stats.game_active = False
    elif (
        not stats.game_active and event.key == pygame.K_s
    ):  # Повторное нажатие S вернет игру в активное состояние
        stats.game_active = True


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:  # Проверка является ли нажатой следующая клавиша
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_event(
    game_settings, screen, ship, aliens, bullets, stats, play_button, scoreboard
):
    """Обрабатывается нажатия клавиш"""
    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
        ):  # Обрабатывается событие нажатия крестика для закрытия проги
            sys.exit()
        elif (
            event.type == pygame.MOUSEBUTTONDOWN
        ):  # Обнаруживаем откработку события нажатия клавиши мыши
            (
                mouse_x,
                mouse_y,
            ) = (
                pygame.mouse.get_pos()
            )  # Возвращает кортеж с координатами x, y точки щелчка
            check_play_button(
                game_settings,
                screen,
                ship,
                aliens,
                bullets,
                stats,
                play_button,
                mouse_x,
                mouse_y,
                scoreboard,
            )  # координаты передаются в функцию
        if (
            event.type == pygame.KEYDOWN
        ):  # Обработка события нажития клавиши(момент нажатия)
            check_keydown_events(
                event, game_settings, screen, ship, aliens, bullets, stats, scoreboard
            )  # Тут происходит вызов метода keydown (event передется из цикла перехвата событий event.get(), сюда же не забываем передать параметр ship)
        if event.type == pygame.KEYUP:  # Обработка события нажития отпускания клавиши
            check_keyup_event(event, ship)


def check_play_button(
    game_settings,
    screen,
    ship,
    aliens,
    bullets,
    stats,
    play_button,
    mouse_x,
    mouse_y,
    scoreboard,
):
    button_clicked = play_button.rect.collidepoint(
        mouse_x, mouse_y
    )  # Метод проверяет находится ли точка в пределах кнопки
    if (
        button_clicked and not stats.game_active
    ):  # реагирование на нажатие кнопки в том случае если игра не активна
        restart_game(game_settings, screen, ship, aliens, bullets, stats, scoreboard)


def restart_game(game_settings, screen, ship, aliens, bullets, stats, scoreboard):
    pygame.mouse.set_visible(
        False
    )  # Скрывает курсор когда состояние игры активно, снизу когда корабль будет уничтожен тот же вызов метода со значением True возварщает видимость курсору
    stats.reset_stats()  # Обновляет статистику игры
    stats.game_active = True  # Переводим флаг в состояние True
    aliens.empty()  # Очищаем список пришельцев и пуль, убираем с экрана,
    bullets.empty()
    create_fleet(
        game_settings, screen, aliens, ship
    )  # Заново пересоздаем флот пришелцев
    ship.center_ship()  # Выравниваем корабль игрока
    game_settings.initialize_dynamic_settings()  # По нажатию на кнопку play возвращаем исходные параметры настроек, выболняем сброс настроек
    scoreboard.prep_score()
    scoreboard.prep_record_score()
    scoreboard.prep_level()
    scoreboard.prep_ships()


def fire_bullet(event, game_settings, screen, ship, bullets):
    if (
        len(bullets) < game_settings.bullets_allowed
    ):  # Проверка если количество элементов списка(bullets) меньше свойстава bullets_allowed в settings разрешаем создать объект bullet
        new_bullet = Bullet(
            game_settings, ship, screen
        )  # Создаем объект экземпляр Bullet
        bullets.add(new_bullet)  # Добавляем объект в группу bullets


def update_bullets(bullets, aliens, game_settings, screen, ship, stats, scoreboard):
    """Функция обновления и уничтожения пуль, вызов функции проверки сопряжения коллизий"""
    bullets.update()
    for (
        bullet
    ) in (
        bullets.copy()
    ):  # Прямые манипуляции со спиком могут вызвать ошибки our of range, поэтому следует перебирать копию группы(метод copy() позволяет изм содержимое bullets)
        if (
            bullet.rect.bottom <= 0
        ):  # Программа проверяет каждую пулю и определяет вышла ли она за верхний край(rect создается в точку корабля, потому координата y его равна положению корабля, bottom мы получаем свойство данного прямоугольника)
            bullets.remove(bullet)
    check_bullet_alien_collisions(
        bullets, aliens, game_settings, screen, ship, stats, scoreboard
    )


def check_bullet_alien_collisions(
    bullets, aliens, game_settings, screen, ship, stats, scoreboard
):
    # Проверка попаданий в пришельцев, каждый раз когда между пулей и пришельцем обнаруживается перекрытие groupcollide() добавляет пару ключ-значение в возвр словарь
    # При обнаружении попадания удалить пулю и пришельца, 2 True говорят о том что объекты необъодимо удалить
    collisions = pygame.sprite.groupcollide(
        bullets, aliens, game_settings.bullets_through, True
    )
    if collisions:  # Если было зафиксировано попадание
        for (
            aliens
        ) in (
            collisions.values()
        ):  # Перебирает все значения которые попали в список collisions (список представляет собой спиосок пришельцев в которых попала одна пуля)
            stats.score += game_settings.alien_score * len(
                aliens
            )  # Определение score в stats увеличивается на величину определенную в game_settings умноженную на количество пришельцев в списке
        scoreboard.prep_score()  # Обновляем изображение scoreboard
        check_record(stats, scoreboard)
    if len(aliens) == 0:  # Проверка если в группе aliens отсуттствут элементы alien
        bullets.empty()  # Удаляем все оставшиеся элементы в группе Bullets
        game_settings.increase_speed()  # Вызывает метод увеличивающий скорость пришельцев и уменьшающая скорость корабля
        create_fleet(
            game_settings, screen, aliens, ship
        )  # то вызываем метод  create_fleet который начинает обработку создания объектов группы Aliens
        stats.score += 100
        scoreboard.prep_score()
        stats.level += 1
        scoreboard.prep_level()


def check_record(stats, scoreboard):
    """Функция проверяет больше ли текущее значение очков значения рекорда"""
    if stats.score > stats.record:
        stats.record = stats.score
        scoreboard.prep_record_score()  # Если проверка положительная обновляет текущее значение рекорда


def get_number_aliens_x(
    game_settings, alien_width
):  # Получаем количество пришельцев на ряд
    avaliable_space_x = (
        game_settings.screen_width - 2 * alien_width
    )  # Вычисляем доступное пространство (ширина экрана заданная в settings уменьшить уже отрисованного пришельца и расстояние от края на ширину пришельца)
    number_aliens_x = int(
        avaliable_space_x / (2 * alien_width)
    )  # Вычисляем количество пришельцев на ряд (для получение целого числа округляем с помозью приведения к int)(доступное место деленное на ширину пришельца и интервал между ними)
    return number_aliens_x


def get_number_rows(
    game_settings, alien_height, ship_height
):  # Метод вычисляет количество рядов прищелцев помещающихся на экране
    available_space_x = (
        game_settings.screen_height - (3 * alien_height) - ship_height
    )  # Доступное пространство = высота экрана - высота корабля - (высота пришельца * 3)
    number_rows = int(
        available_space_x / (2 * alien_height)
    )  # Количество рядов = Доступное пространство / (высота пришельца + интервал(равный высоте пришельца))
    return number_rows  # Метод возвращает число рядов


def create_alien(
    game_settings, screen, aliens, alien_number, row_number
):  # Методо создает пришельца
    alien = Alien(
        game_settings, screen
    )  # Создание экземпляра класса Alien с параметрами игровых функций и параметром поверхности
    alien_width = (
        alien.rect.width
    )  # Определяем ширину объекта alien как ширина прямоугольника (объект.параметр_прямоулольника_определенный_alien.свойство)
    alien.x = (
        alien_width + 2 * alien_width * alien_number
    )  # Обновленная позиция пришельца, каждый пришелец смещается на одну ширину от левого поля
    alien.rect.x = alien.x  # Помещаем прямоугольник колизию пришельца в позицию х
    alien.rect.y = (
        alien.rect.height + 2 * alien.rect.height * row_number
    )  # Помещаем прямоугольник колизию пришельца в позицию х
    aliens.add(alien)  # Добавляем полученный объект в список Group() Sprite


def create_fleet(game_settings, screen, aliens, ship):
    alien = Alien(
        game_settings, screen
    )  # Создание экземпляра класса Alien с параметрами игровых функций и параметром поверхности
    number_aliens_x = get_number_aliens_x(
        game_settings, alien.rect.width
    )  # Количество пришельцев получаем из метода get_number путем присвоения переменной значения возвращаемого функцией
    number_rows = get_number_rows(game_settings, alien.rect.height, ship.rect.height)
    for row_number in range(
        number_rows
    ):  # Вложеный цикл, заполняем первый ряд весь, потом второй и тд...
        for alien_number in range(
            number_aliens_x
        ):  # В цикле пробегаем по количеству пришельцев и на каждой итерации создаем объект пришельца
            create_alien(
                game_settings, screen, aliens, alien_number, row_number
            )  # Вызываем метод create_alien


def ship_hit(
    game_settings, stats, screen, ship, aliens, bullets, scoreboard, rip_ship=1
):
    """Обрабатывает столкновение корабля с пришельцем"""
    stats.ships_count -= rip_ship  # Уменьшаем количество кораблей, не обращаемся к settings, тк необходимо инициировать для каждой сессии количество равное ship_count
    scoreboard.prep_ships()
    if (
        stats.ships_count > 0
    ):  # Если значение ships_count больше нуля разрешаем уничножать корабль
        aliens.empty()  # Очищаем списки (убираем с экрана)
        bullets.empty()

        game_settings.decrease_speed()  # Уменьшаем скорость пришельцев, увеличиваем скорость корабля

        create_fleet(game_settings, screen, aliens, ship)  # Создаем новый флот
        ship.center_ship()  # Размещаем корабль в центре

        if stats.level > 1:
            stats.level -= 1  # Уменьшаем номер уровня отображаемый на экране
        scoreboard.prep_level()  # Обновляем изображение

        sleep(
            0.5
        )  # Делает паузу перед тем как перейти к отрисовке экрана в функиции update_screen()
    else:  # В противном случае активируем флаг и переводим его в позицию False
        stats.game_active = False
        pygame.mouse.set_visible(
            True
        )  # Возвращает курсор из невидимого состояния для повторного нажатия кнопки Play


def check_aliens_bottom(
    game_settings, screen, ship, aliens, bullets, stats, scoreboard
):
    """Проверяет достигли ли пришельцы низа экрана"""
    screen_rect = screen.get_rect()  # Получаем приямоугольник экрана
    for (
        alien
    ) in (
        aliens.sprites()
    ):  # Для любого объекта из группы спрайтов пришельцев, если объект достиг низа прямоугольной области экрана вызываем функцию ship_hit() и выходим из цикла
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard, 4)
            break


def create_stars(game_settings, screen, milky_way):
    star = MilkyWay(game_settings, screen)
    for star in range(20):
        displacement_x = randint(1, 23)
        displacement_y = randint(0, 800)
        star = MilkyWay(game_settings, screen)
        star_width = star.rect.width
        star.star_x = star_width + 2 * star_width * displacement_x
        star.rect.x = star.star_x
        star.star_y = star.rect.height + 2 * star.rect.height + displacement_y
        star.rect.y = star.star_y
        milky_way.add(star)


def new_stars(game_settings, screen, milky_way):
    if len(milky_way) < 20:
        create_stars(game_settings, screen, milky_way)


def update_stars(game_settings, screen, milky_way):
    milky_way.update()
    for star in milky_way.copy():
        if star.rect.bottom >= game_settings.screen_height:
            milky_way.remove(star)
    new_stars(game_settings, screen, milky_way)


def check_fleet_edges(game_settings, aliens):
    """Реагирует на достижение пришельцев края экрана"""
    for (
        alien
    ) in (
        aliens.sprites()
    ):  # Перебирает каждого пришельца в группе и для каждого объекта
        if (
            alien.check_edges()
        ):  # Вызывает метод проверки выхода объекта за пределы экрана
            change_fleet_direction(
                game_settings, aliens
            )  # Если выполняется то изменяем позицию вызвав функцию  ниже
            break


def change_fleet_direction(game_settings, aliens):
    """Опускает весь флот и меняет направление флота"""
    for alien in aliens.sprites():
        alien.rect.y += (
            game_settings.fleet_drop_speed
        )  # Для каждого пришельца уменьшаем позицию y на величину из settings
    game_settings.fleet_direction *= (
        -1
    )  # Дополнительно изменяем модификатор направления на противоположный


def update_aliens(game_settings, screen, ship, aliens, bullets, stats, scoreboard):
    """Обновляет позиции всех пришельцев во флоте"""
    check_fleet_edges(
        game_settings, aliens
    )  # функция при каждом обновлении пришельца выполняет проверку объектов выхода за границу экрана
    aliens.update()  # Метод update() примененный к группе автоматически применяется для каждого пришельца
    # Метод проверяет соприкосновение объектов, в данном случае метод пробегает в цикле по группе aliens и возвращает первого пришельца который соприкоснулся с кораблем
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(
            game_settings, stats, screen, ship, aliens, bullets, scoreboard
        )  # Вызываем функцию обработки столконовения корабля с пришельцем
    check_aliens_bottom(
        game_settings, screen, ship, aliens, bullets, stats, scoreboard
    )  # Проверка пришельцев, добравшихся до нижнего края экрана


def updata_screen(
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
):
    """Обновляет изображение на экране и отображает новый экран"""
    screen.fill([255, 255, 255])  # метод заполняющий экран цветом
    screen.blit(background.image, background.rect)
    scoreboard.show_score()
    # screen.blit(game_settings.space_image, screen.get_rect()) # Задний фон реализован с помощью метода blit, который заполняет экран картинкой, сама картинка загрузается в модуле settings
    for bullet in bullets.sprites():  # Возвращаем список всех спрайтов в группе
        bullet.draw_bullet()  # Чтобы нарисовать пули выпущенные на экране программа перебирает спрайты в bullet и вызывает для каждого draw_bullet()
    milky_way.draw(screen)
    ship.blitme()  # Вызов метода вывода на экран модели космического корабля, реализованная в модуле ship.py
    # milky_way.draw(screen)
    aliens.draw(screen)
    # alien.blitme() # Вызов метода отображения на экране модели корабля пришельцев, реализованого в модуле alien.py(в основном классе вызывается метод update_screen в который передается в кач-ве параметра ссылка на объект alien)
    if not stats.game_active:  # Если игра не активна
        play_button.draw_button()

    pygame.display.flip()  # Отображение последнего прорисованного экрана

