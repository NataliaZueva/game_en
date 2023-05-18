import pygame
import colors

color = colors.Color()


class Player(object):
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.coordinate = 30
        self.size = pygame.Surface((120, 300))
        self.step = 0  # Нажата ли одна из клавиш движения
        self.inventory = []
        self.animation = 0
        self.rotate = "right"

    # Проверка зажаты ли клавиши движения (Вынесена сюда для удобства)
    # Отредактировать в соответствии с выбранной расскладкой !!!
    def walk(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.animation = 0
                self.step = -5
                self.rotate = "left"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.animation = 0
                self.step = 5
                self.rotate = "right"
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d]:
                self.animation = 0
                self.step = 0

    # Отрисовка персонажа на экране
    def draw(self, setting, height = 300):
        if self.step == 0:
            if self.animation > 60:
                self.animation = 0
            img = "Ayur\\" + str(self.rotate) + "\\" + str(self.rotate) + "-stand-" + str(self.animation // 31 + 1) + ".png"
            img = pygame.image.load(img)
            self.rect = self.image.get_rect(center=(self.coordinate + 60, height + 150))
            setting.screen.blit(img, self.rect)
            self.animation += 1
        else:
            if self.animation > 30:
                self.animation = 0
            img = "Ayur\\" + str(self.rotate) + "\\" + str(self.rotate) + "-" + str(self.animation // 4) + ".png"
            img = pygame.image.load(img)
            self.rect = self.image.get_rect(center=(self.coordinate + 60, height + 150))
            setting.screen.blit(img, self.rect)
            self.animation += 1
