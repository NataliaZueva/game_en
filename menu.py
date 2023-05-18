import pygame
import os
import colors

color = colors.Color()


def text(screen, font, message, x, y, color):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def text_button(screen, wight, font, message, x, y, color):
    pygame.draw.rect(screen, color, (x[0], y[0], wight / 2, 50), 1)
    text(screen, font, message, x[1], y[1], color)


def draw_triangle(setting, x, y, direction, color):
    pygame.draw.line(setting.screen, color, (x + 25, y - 15), (x + 25, y + 15), 1)
    if direction == "left":
        pygame.draw.line(setting.screen, color, (x + 10, y), (x + 25, y + 15), 1)
        pygame.draw.line(setting.screen, color, (x + 25, y - 15), (x + 10, y), 1)
    else:
        pygame.draw.line(setting.screen, color, (x + 40, y), (x + 25, y + 15), 1)
        pygame.draw.line(setting.screen, color, (x + 25, y - 15), (x + 40, y), 1)


def are_you_sure(setting):
    clock = pygame.time.Clock()
    selected_button = 0
    label = ""
    hover_area = []
    if setting.language == "Русский":
        hover_area = ["Да", "Нет"]
        label = "Вы уверены?"
    elif setting.language == "English":
        hover_area = ["Yes", "No"]
        label = "Are you sure?"
    while 1:
        clock.tick(10)
        setting.screen.fill(color.board)
        font = pygame.font.SysFont('Comic Sans MS', 50)
        text(setting.screen, font, label, setting.wight / 2, setting.height / 3, color.WHITE)
        font = pygame.font.SysFont('Comic Sans MS', 25)
        size = [5, 2]
        for i in range(len(hover_area)):
            pygame.draw.rect(setting.screen, color.BLACK if i == selected_button else color.WHITE,
                             (setting.wight / size[i], setting.height / 2 - 25, setting.wight / 4, 50), 1)
            text(setting.screen, font, hover_area[i], setting.wight / size[i] + setting.wight / 8, setting.height / 2, \
                 color.BLACK if i == selected_button else color.WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_button += 1
                elif event.key == pygame.K_LEFT:
                    selected_button -= 1
                elif event.key == pygame.K_RETURN:
                    return True if selected_button == 0 else False
        if selected_button > 1:
            selected_button = 0
        elif selected_button == -1:
            selected_button = 1


def Credits(setting):
    clock = pygame.time.Clock()
    hover_area = []
    height = 220
    if setting.language == "Русский":
        hover_area = ["Над игрой работали:", "Разработка персонажей: Наталья Зуева", "Отрисовка фонов: Наталья Зуева",
                      "Написание кода: Шабанова Юлия", "Игра создана при поддержке внутренних сил",
                      "В ролях:", "Аюр : Дондоков Аюр", "Егор : Борвенко Егор", "Наташа : Наталья Зуева",
                      "Юля : Шабанова Юлия", "Юлия Сергеевна в роли Юлии Сергеевны",
                      "Иван Сергеевич в роли Ивана Сергеевич", "Спонсоры проекта:", "Бессонница", "Ссесия",
                      "Короткий дедлайн"]
    elif setting.language == "English":
        hover_area = ["CAST:", "Character development: Natalia Zueva", "Drawing backgrounds: Natalia Zueva",
                      "Writing code: Shabanova Yulia", "The game was created with the support of internal forces",
                      "Roles played:", "Ayur : Dondokov Ayur", "Egor : Borvenko Egor", "Natasha : Natalia Zueva",
                      "Yulia : Shabanova Yulia", "Yulia Sergeevna as Yulia Sergeevna",
                      "Ivan Sergeyevich as Ivan Sergeyevich", "Project sponsors:", "Insomnia", "Session",
                      "Short deadline"]
    while 1:
        clock.tick(50)
        setting.screen.fill(color.board)
        font = pygame.font.SysFont('Comic Sans MS', 25)
        y = height
        stop_it = False
        for i in hover_area:
            text(setting.screen, font, i, setting.wight / 2, y, color.WHITE)
            y += 70
            if y > setting.height:
                break
        pygame.display.update()
        height -= 1
        if height == len(hover_area) * -70:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop_it = True
        if stop_it:
            break


class Menu(object):
    def __init__(self):
        self.hover_area = {}
        self.labels = []
        self.select_window = 0
        self.has_the_game_started = True
        self.select_button = self.left_right = 0
        self.room_id = {}
        self.language = ["English", "Русский"]
        self.scene = {"name": "01", "player": 120, "shift": 120}
        self.inventory = []
        self.stage = 0

    def change_settings(self, setting):
        self.hover_area = {}
        if setting.language == "Русский":
            self.room_id = {'01': "Вход в библиотеку", '02': "Библиотека", '03': "Кабинет группы: 2", '04': "Коридор"}
            self.labels = [["Аюр: история одного проекта", "", "Сохранить игру", "Загрузить игру", "Настройки"], "X - удалить сохранение"]
            self.hover_area = {0: ["Начать игру", "Загрузить игру", "Настройки", "Авторы", "Выход", 220], \
                               1: ["Продолжить", "Сохранить игру", "Загрузить игру", "Настройки", "Главное меню", \
                                   "Выход", 120],
                               2: ["Назад", "Новое сохранение", 100],
                               3: ["Назад", 100],
                               4: ["Язык", "Полноэкранный режим", "Применить", "Отмена", 220]
                               }

        elif setting.language == "English":
            self.room_id = {'01': "Entrance to the library", '02': "library", '03': "Group cabinet: 2", '04': "Hallway"}
            self.labels = [["Ayur: the history of one project", "", "Save", "Load", "Setting"], "X - delete save"]
            self.hover_area = {0: ["New game", "Load game", "Options", "Credits", "Exit", 220], \
                               1: ["Continue", "Save game", "Load game", "Options", "Main menu", "Exit", 120],
                               2: ["Back", "New save", 100],
                               3: ["Back", 100],
                               4: ["Language", "Fullscreen", "apply", "cancel", 220]
                               }

    def window(self, setting, scene, inventory, stage):
        pygame.mixer.music.load("music\\Tinker Time - Nathan Moore.mp3")
        pygame.mixer.music.play(-1)

        self.scene = scene
        self.inventory = inventory
        self.stage = stage

        clock = pygame.time.Clock()
        for i in range(len(self.language)):
            if self.language[i] == setting.language:
                self.left_right = i
        self.selected_button = 0
        while 1:
            if setting.menu_сhanges:  # Установка настроек
                setting.menu_сhanges = False
                self.change_settings(setting)
            clock.tick(10)
            setting.screen.fill(color.board)
            y = self.hover_area[self.select_window][-1]
            font = pygame.font.SysFont('Comic Sans MS', 25)
            if self.select_window == 4:
                for i in range(len(self.hover_area[4]) - 1):
                    if i == 0:
                        pygame.draw.rect(setting.screen, color.WHITE if i != self.selected_button else color.BLACK, \
                                         ((setting.wight / 4) * 2, y, setting.wight / 4, 50), 1)
                        text(setting.screen, font, self.language[self.left_right],
                             setting.wight / 2 + setting.wight / 8,
                             y + 25, \
                             color.WHITE if i != self.selected_button else color.BLACK)
                        draw_triangle(setting, (setting.wight / 4) * 2, y + 25, "left", \
                                      color.WHITE if i != self.selected_button else color.BLACK)
                        draw_triangle(setting, setting.wight / 2 + setting.wight / 5 + 10, y + 25, "right", \
                                      color.WHITE if i != self.selected_button else color.BLACK)
                    elif i == 1:
                        pygame.draw.rect(setting.screen, color.WHITE if i != self.selected_button else color.BLACK, \
                                         ((setting.wight / 4) * 2 + setting.wight / 9, y, 50, 50), 1)
                        if setting.full_screen == "True":
                            pygame.draw.rect(setting.screen, color.WHITE if i != self.selected_button else color.BLACK, \
                                             ((setting.wight / 4) * 2 + setting.wight / 9 + 10, y + 10, 30, 30))
                    if i < 2:
                        text(setting.screen, font, self.hover_area[4][i], setting.wight / 3, y + 25, color.WHITE)
                    else:
                        text_button(setting.screen, setting.wight, font, self.hover_area[4][i], \
                                    [setting.wight / 4, setting.wight / 2], [y, y + 25], \
                                    color.WHITE if i != self.selected_button else color.BLACK)
                    y += 70
            else:
                for i in range(len(self.hover_area[self.select_window]) - 1):
                    text_button(setting.screen, setting.wight, font, self.hover_area[self.select_window][i], \
                                [setting.wight / 4, setting.wight / 2], [y, y + 25], \
                                color.BLACK if i == self.selected_button else color.WHITE)
                    y += 70
            if self.select_window in [2, 3]:
                pygame.draw.rect(setting.screen, color.board, (0, 0, setting.wight, 90))
            if self.select_window == 0:
                font = pygame.font.SysFont('Comic Sans MS', 50)
                text(setting.screen, font, self.labels[0][self.select_window], setting.wight / 2, 120, color.WHITE)
            else:
                font = pygame.font.SysFont('Comic Sans MS', 30)
                text(setting.screen, font, self.labels[0][self.select_window], setting.wight / 2, 60, color.WHITE)
            if self.select_window == 3:
                font = pygame.font.SysFont('Comic Sans MS', 20)
                text(setting.screen, font, self.labels[1], setting.wight / 2 + setting.wight / 3, 20, color.WHITE)
            pygame.display.update()
            if self.buttons(setting):
                break
        return self.scene, self.inventory, self.stage

    def buttons(self, setting):
        for event in pygame.event.get():
            if event.type == pygame.QUIT and are_you_sure(setting):
                exit()
            if event.type == pygame.KEYDOWN:
                if self.selected_button == 0 and event.key == pygame.K_LEFT:
                    self.left_right -= 1
                if self.selected_button == 0 and event.key == pygame.K_RIGHT:
                    self.left_right += 1
                if event.key == pygame.K_ESCAPE:
                    if self.select_window == 1:
                        return True
                    elif self.select_window in [2, 3]:
                        self.select_window = 0 if self.has_the_game_started else 1
                # Удаление сохранения
                elif event.key == pygame.K_x and self.select_window == 3 and self.selected_button != 0:
                    message = self.hover_area[self.select_window][self.selected_button].split(' ')[0]
                    for i in list(os.listdir('./save/')):
                        if i.split('..')[0] == message:
                            message = i
                            break
                    os.remove('save/' + message)
                    self.reading_files
                elif event.key == pygame.K_RETURN and self.text_buttons(setting):
                    return True
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.selected_button += 1
            if self.selected_button > 4 and self.hover_area[self.select_window][-1] > 100 - \
                    (len(self.hover_area[self.select_window]) - 10) * 70:
                self.hover_area[self.select_window][-1] -= 70
        elif pygame.key.get_pressed()[pygame.K_UP]:
            self.selected_button -= 1
            if self.selected_button < len(self.hover_area[self.select_window]) and \
                    self.hover_area[self.select_window][-1] < 100:
                self.hover_area[self.select_window][-1] += 70
        if len(self.hover_area[self.select_window]) != 0 and \
                self.selected_button > len(self.hover_area[self.select_window]) - 2:
            self.selected_button = 0
            if self.select_window in [2, 3]:
                self.hover_area[self.select_window][-1] = 100
        elif self.selected_button == -1:
            self.selected_button = len(self.hover_area[self.select_window]) - 2
            if self.select_window in [2, 3] and len(self.hover_area[self.select_window]) - 2 > 8:
                self.hover_area[self.select_window][-1] = 100 - (len(self.hover_area[self.select_window]) - 10) * 70
        if self.left_right >= len(self.language):
            self.left_right = 0
        elif self.left_right < 0:
            self.left_right = len(self.language) - 1
        if self.select_window == 4:
            setting.language = self.language[self.left_right]
            self.change_settings(setting)

    def text_buttons(self, setting):
        # Начать игру или продолжить
        if self.select_window in [0, 1] and self.selected_button == 0:
            if self.select_window == 0:
                self.scene = {"name": "01", "player": 30, "shift": 0}
                self.inventory = []
                self.stage = 0
                self.select_window = 1
            self.has_the_game_started = False
            pygame.mixer.music.stop()
            return True
        # Выход
        elif self.select_window in [0, 1] and self.selected_button == len(self.hover_area[self.select_window]) - 2:
            if are_you_sure(setting):
                exit()
        # Главное меню
        elif self.select_window == 1 and self.selected_button == 4:
            if are_you_sure(setting):
                self.select_window = 0
                self.selected_button = 0
                self.has_the_game_started = True
        # Загрузить игру
        elif (self.select_window == 0 and self.selected_button == 1) or \
                (self.select_window == 1 and self.selected_button == 2):
            self.select_window = 3
            self.reading_files
        # Сохранить игру
        elif self.select_window == 1 and self.selected_button == 1:
            self.select_window = 2
            self.reading_files
        # Новое сохранение
        elif self.select_window == 2 and self.selected_button == 1:
            self.new_save(len(list(os.listdir('./save/'))) + 1)
            self.select_window = 1
            return True
        # Авторы
        elif self.select_window == 0 and self.selected_button == 3:
            Credits(setting)
        # Нажатие кнопки настройки
        elif (self.select_window == 0 and self.selected_button == 2) or \
                (self.select_window == 1 and self.selected_button == 3):
            self.selected_button = 0
            self.select_window = 4
        elif self.select_window == 4:
            # Переключение полноэкранного режима
            if self.selected_button == 1:
                setting.full_screen = "False" if setting.full_screen == "True" else "True"
                setting.change_settings
            # Применить настройки
            elif self.selected_button == 2:
                setting.record_changes
                self.selected_button = 0
                self.select_window = 0 if self.has_the_game_started else 1
            # Отменить настройки
            elif self.selected_button == 3:
                setting.read_settings_file
                self.selected_button = 0
                for i in range(len(self.language)):
                    if self.language[i] == setting.language:
                        self.left_right = i
                self.select_window = 0 if self.has_the_game_started else 1
        # Назад
        elif self.select_window in [2, 3] and self.selected_button == 0:
            self.selected_button = 0
            self.select_window = 0 if self.has_the_game_started else 1
        # Нажатое окно сохранения
        else:
            if self.has_the_game_started:
                self.save() if self.select_window == 2 else self.load()
                self.select_window = 1
            elif are_you_sure(setting):
                self.save() if self.select_window == 2 else self.load()
                self.select_window = 1
            return True
        return False

    @property
    def reading_files(self):  # Создаем из файлов сохранений список
        self.selected_button = 0
        wind = 3 if self.select_window == 2 else 2
        while len(self.hover_area[self.select_window]) != wind:
            self.hover_area[self.select_window].pop(wind - 1)
        for i in self.sort_save:
            self.hover_area[self.select_window].insert(wind - 1, self.save_name(i))
            wind += 1

    @property
    def sort_save(self):  # Функция сортирует файлы с сохранениями по возрaстанию
        save = list(os.listdir('./save/'))
        for i in range(len(save)):
            save[i] = save[i].split('.')[0]
        n = 0
        first_big_elem = ''
        while n != len(save):
            if first_big_elem == save[n]:
                break
            if int(save[n]) - 1 != n:
                if first_big_elem == '' or int(first_big_elem) > int(save[n]):
                    first_big_elem = save[n]
                save.append(save[n])
                save.pop(n)
                n -= 1
            n += 1
        return save

    def save_name(self, file):  # Читаем файлы из папки "save"
        room_name = open('save/' + str(file) + '..txt', 'r', encoding='utf-8')
        room_name = room_name.readline().replace('\n', '')
        return file + ' ' + self.room_id[room_name]

    def save(self, save_name=''):
        if save_name == '':
            save_name = self.hover_area[self.select_window][self.selected_button].split(' ')[0]
            for i in list(os.listdir('./save/')):
                if i.split('..')[0] == save_name:
                    save_name = i
                    break
        if len(save_name.split('..')) == 1:
            save_name = str(save_name) + '..txt'
        file = open('save/' + save_name, 'w', encoding='utf-8')
        file.write(self.scene['name'] + '\n')
        file.write(str(self.scene['player']) + '\n')
        file.write(str(self.scene['shift']) + '\n')
        if len(self.inventory) != 0:
            file.write('|'.join(self.inventory))
        file.write('\n')
        file.write(str(self.stage) + '\n')

    def load(self):
        save_name = self.hover_area[self.select_window][self.selected_button].split(' ')[0]
        for i in list(os.listdir('./save/')):
            if i.split('..')[0] == save_name:
                save_name = i
                break
        file = open('save/' + save_name, 'r', encoding='utf-8')
        self.scene["name"] = file.readline().replace('\n', '')
        self.scene["player"] = int(file.readline().replace('\n', ''))
        self.scene["shift"] = int(file.readline().replace('\n', ''))
        self.inventory = []
        inv = file.readline().replace('\n', '')
        if inv != '':
            self.inventory = inv.split('|')
        self.stage = int(file.readline().replace('\n', ''))
        self.has_the_game_started = False
        file.close()

    def new_save(self, file_name):
        file_name = str(file_name).split(' ')[0]
        number = int(file_name[0])
        for i in self.sort_save:
            if int(i.split('..')[0]) == number:
                number += 1
        file_name = str(number)
        self.save(str(file_name))


class Setting(object):
    def __init__(self):
        self.language = ""
        self.full_screen = self.screen = None
        self.menu_сhanges = self.game_changes = True
        self.wight = self.height = 0
        self.read_settings_file

    @property
    def change_settings(self):
        self.screen = pygame.display.set_mode((self.wight, self.height), pygame.FULLSCREEN | pygame.SCALED) \
            if self.full_screen == "True" else pygame.display.set_mode((self.wight, self.height), pygame.SCALED)

    @property
    def read_settings_file(self):
        file = open('setting.txt', 'r', encoding='utf-8')
        file = file.readline().split(" ")
        self.language, self.full_screen = file[0], file[1]
        self.wight, self.height = int(file[2]), int(file[3])
        self.menu_сhanges = self.game_changes = True
        self.change_settings

    @property
    def record_changes(self):
        self.menu_сhanges = self.game_changes = True
        file = open("setting.txt", "w", encoding='utf-8')
        file.write(str(self.language) + " " + str(self.full_screen) + " " + \
                   str(self.wight) + " " + str(self.height))
        file.close()
