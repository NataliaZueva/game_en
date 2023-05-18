import pygame
import colors

color = colors.Color()


def _1_load(setting, size, shift, player):
    setting.screen.blit(bg1, (0 + shift, 0))
    player.draw(setting, 400)


def _2_load(setting, size, shift, player):
    setting.screen.blit(bg2, (0 + shift, 0))
    IS.draw(setting, size / 2 - 60 + shift)
    player.draw(setting)


def _3_load(setting, size, shift, player):
    setting.screen.blit(bg3, (0 + shift, 0))
    YS.draw(setting, 2105 + shift)
    egor.draw(setting, 4357 + shift)


def _4_load(setting, size, shift, player):
    setting.screen.blit(bg4, (0 + shift, 0))
    player.draw(setting)


def _5_load(setting, size, shift, player):
    setting.screen.blit(bg5, (0 + shift, 0))
    player.draw(setting)


_1 = {"screen": _1_load, "size": 2689, "scene_boundaries": [20, 579]}
_2 = {"screen": _2_load, "size": 1200, "scene_boundaries": [20, 1200 / 2 - 300]}
_3 = {"screen": _3_load, "size": 5562, "scene_boundaries": [130, 150]}
_4 = {"screen": _4_load, "size": 2878, "scene_boundaries": [130, 150]}
_5 = {"screen": _5_load, "size": 1200, "scene_boundaries": [20, 1200 / 2]}
bg1 = pygame.image.load("location/1.png")
bg2 = pygame.image.load("location/2.png")
bg3 = pygame.image.load("location/3.png")
bg4 = pygame.image.load("location/4.png")
bg4 = pygame.transform.scale(bg4, (2878, 720))
bg5 = pygame.image.load("location/05.png")


class NPC(object):
    def __init__(self, directory, breath):
        self.animation = 0
        self.directory = directory
        self.image = pygame.image.load("NPC\\" + str(self.directory) + "\\npc-1.png")
        self.breath = breath

    def draw(self, setting, coordinate):
        if self.animation > self.breath:
            self.animation = 0
        img = "NPC\\" + str(self.directory) + "\\npc-" + str(self.animation // (self.breath // 2 + 1) + 1) + ".png"
        img = pygame.image.load(img)
        rect = self.image.get_rect(center=(coordinate + 60, 300 + 130))
        setting.screen.blit(img, rect)
        self.animation += 1


egor = NPC("egor", 70)
YS = NPC("iovleva", 75)
IS = NPC("petrushin", 65)
