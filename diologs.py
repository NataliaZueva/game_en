import pygame
import menu
import colors
import dialogs_list

color = colors.Color()

class Diologs(object):
    def __init__(self, id, setting):
        language = {"Русский": "ru", "English": "en"}
        self.person = id['person_' + language[setting.language]]
        self.with_who = id['with_who']
        self.who_talk = id['who_talk']
        self.fill = id['fill']
        self.message = id[language[setting.language]]
        self.cicle(setting)

    def cicle(self, setting):
        for i in range(len(self.who_talk)):
            windows(setting, self.person[self.who_talk[i]], text_separation(self.message[i]), self.with_who, self.fill)


def windows(setting, who_says, text, who_second, fill):
    clock = pygame.time.Clock()
    Ayur = Character("left", "Ayur\\right\\right-stand-", 35, setting.wight)
    if who_second != "" and who_second != "NB" and who_second != "Au":
        second_person = Character("right", who_second, 40, setting.wight)
    while 1:
        clock.tick(10)
        setting.screen.blit(fill[0], (fill[1], 0))
        Ayur.draw(setting.screen)
        if who_second != "" and who_second != "NB" and who_second != "Au":
            second_person.draw(setting.screen)
        font = pygame.font.SysFont('Comic Sans MS', 40)
        pygame.draw.rect(setting.screen, color.WHITE, (-1, 450, setting.wight + 2, 400))
        pygame.draw.rect(setting.screen, color.GREY_BLUE, (-1, 450, setting.wight + 2, 50))
        menu.text(setting.screen, font, str(who_says) + ":", setting.wight / 4, 470, color.BLACK)
        font = pygame.font.SysFont('Comic Sans MS', 25)
        y = 530
        for i in text:
            message = font.render(i, True, color.BLACK)
            text_rect = message.get_rect(center=(0, y))
            text_rect.left = setting.wight / 6
            setting.screen.blit(message, text_rect)
            y += 30
        menu.text(setting.screen, font, "E", setting.wight - 20, 700, color.PURPLE)
        pygame.display.update()
        if button(setting):
            break


def button(setting):
    for event in pygame.event.get():
        if event.type == pygame.QUIT and menu.are_you_sure(setting):
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e or event.key == pygame.K_RETURN:
                return True
    return False


def show_character(setting, who, emotion, left_right):
    img = str(who)
    if left_right == "left":
        pygame.draw.rect(setting.screen, color.WHITE, (50, 50, 300, 500))
    else:
        pygame.draw.rect(setting.screen, color.WHITE, (setting.wight - 350, 50, 300, 500))


def text_separation(text):
    text = text.split(' ')
    message = []
    box = ""
    for i in text:
        if len(box + i) + 1 > 58:
            message.append(box)
            box = i
        else:
            box += " " + i
    message.append(box)
    return message


class Character(object):
    def __init__(self, position, directory, breath, wight):
        self.animation = 0
        if position == "left":
            self.position = 90
        else:
            self.position = wight - 200
        self.directory = directory
        self.image = pygame.image.load(str(directory)+"1.png")
        self.breath = breath

    def draw(self, screen, size = (176, 650)):
        if self.animation > self.breath:
            self.animation = 0
        img = str(self.directory) + str(self.animation // (self.breath // 2 + 1) + 1) + ".png"
        img = pygame.image.load(img)
        img = pygame.transform.scale(img, size)
        rect = self.image.get_rect(center=(self.position, 300))
        screen.blit(img, rect)
        self.animation += 1