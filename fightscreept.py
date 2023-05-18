import pygame
import random
import colors
import diologs

color = colors.Color()

WIDTH = 1200


def texts(message, x, y, color, font, screen):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def fight(screen, text):
    clock = pygame.time.Clock()
    text = text.split(" ")
    line, schet = [], []
    select_button = 0
    falls = 0
    n = 1
    while len(line) != len(text):
        rnd = random.randint(0, len(text) - 1)
        if rnd not in line:
            line.append(rnd)
    while len(schet) != len(line): schet.append(0)
    Ayur = diologs.Character("right", "Ayur\\left\\left-stand-", 35, 1100)
    while 1:
        clock.tick(10)
        screen.fill(color.board)
        Ayur.draw(screen, (280, 1037))
        font = pygame.font.SysFont('Comic Sans MS', 50)
        y = 60
        for i in range(len(line)):
            pygame.draw.rect(screen, color.BLACK if i == select_button \
                else color.WHITE, (1200 / 5 - 70, y - 20, 1200 / 4 + 140, 60), 1)
            texts(text[line[i]], 1200 / 5 + 1200 / 8, y, color.BLACK if i == select_button \
                else color.WHITE, font, screen)
            texts(str(schet[i]) if schet[i] != 0 else "", 190, y + 10, color.BLACK if i == select_button \
                else color.WHITE, font, screen)
            y += 70
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    select_button += 1
                elif event.key == pygame.K_UP:
                    select_button -= 1
                elif event.key == pygame.K_RETURN:
                    if schet[select_button] == 0:
                        schet[select_button] = n
                    else:
                        l = schet[select_button]
                        for i in range(len(schet)):
                            if schet[i] > l:
                                schet[i] -= 1
                        schet[select_button] = 0
                        n -= 2
                    n += 1
        if select_button > len(line) - 1:
            select_button = 0
        elif select_button == -1:
            select_button = len(line) - 1
        kolvo = 0
        for i in schet:
            if i != 0:
                kolvo += 1
        if kolvo == len(schet):
            kolvo = 0
            for i in range(len(schet)):
                if schet[i] - 1 != line[i]:
                    kolvo = 1
                    for l in range(len(schet)):
                        schet[l] = 0
                    falls += 1
                    n = 0
                    break
            if kolvo == 0:
                your_result(screen, falls)
                break


def your_result(screen, falls):
    clock = pygame.time.Clock()
    n = 0
    message = ""
    Ayur = diologs.Character("right", "Ayur\\left\\left-stand-", 35, 1100)
    while n != 50:
        clock.tick(50)
        screen.fill(color.board)
        Ayur.draw(screen, (280, 1037))
        font = pygame.font.SysFont('Comic Sans MS', 50)
        if falls == 0:
            message = "PERFECT"
        elif falls > 0 and falls < 6:
            message = "GOOD"
        elif falls > 5 and falls < 11:
            message = "OOPS"
        elif falls > 10:
            message = "DO YOU SPEAK ENGLISH?"
        texts(message, 1200 / 5 + 1200 / 8, 720 / 2, color.WHITE, font, screen)
        pygame.display.update()
        n += 1
