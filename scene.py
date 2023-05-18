import menu
import pygame
import scene_list as sl
import scripts
import colors
import player as pl

color = colors.Color()
play = pl.Player("hi")

scene_set = {
    "01": [sl._1, scripts.Location_set._1], "02": [sl._2, scripts.Location_set._2],
    "03": [sl._3, scripts.Location_set._3], "04": [sl._4, scripts.Location_set._4],
    "05": [sl._5, scripts.Location_set._5]
}


def text_at_center(screen, message, x, y):
    font = pygame.font.SysFont('Comic Sans MS', 20)
    text = font.render(message, True, color.RED)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def widget(scene, scr):
    pygame.init()
    setting = menu.Setting()
    wind(setting, scene, 0, 1, scr)


def wind(setting, scene, shift, stage, scr):
    clock = pygame.time.Clock()
    step = 0
    old_location_set = []
    inventory = []
    while 1:
        clock.tick(30)
        if "reset" in inventory:
            inventory = []

        # Функция для отрисовки карты
        scene['screen'](setting, scene['size'], shift)

        # if scene["screen"] != old_location_set:
        # вызов скриптов с их первоночальной догрузкой

        old_location_set = scene["screen"]
        # Создаем переменную для скриптов
        locl = scripts.Location_set(scr, stage)
        # Подгружаем скрипты к локации
        set = locl.location(locl, inventory, "Русский")

        # player, inventory, st = sl.Scripts(sl.Scripts.autor_script, location_set.open_location_script).start(
        #   setting)
        # stage += st
        # if ss != -1:
        #   step = ss
        # shift += step
        # print(locl.scripts)
        # scrr = scripts.Scripts(locl.scripts[0][0], locl.scripts[0][1])
        # player, inventory, st = scrr.start(setting)
        # scene = scene_set[player["name"]][0]
        # scr = scene_set[player["name"]][1]

        col = collision_check(setting, locl.scripts, locl.hitbox, play.coordinate, set, shift)

        if scene["screen"] == sl._3_load and "mug" not in inventory:
            pygame.draw.rect(setting.screen, color.RED, (1000 + shift, 500, 80, 50))

        for i in locl.hitbox:
            pygame.draw.rect(setting.screen, color.GREEN, (i[0]+ shift, 300, i[1] - i[0], 300), 1)

        play.draw(setting)

        pygame.display.update()
        ss = button(setting)
        if ss != -1 and ss != "e":
            step = ss
        elif ss == "e":
            # Получаем все данные от скрипта
            player, inventory, st = scripts.Scripts(col[0], col[1]).start(setting)
            print(player)
            if len(list(player.keys())) != 0:
                # меняем локоцию если это необходимо
                scene = scene_set[player["name"]][0]
                scr = scene_set[player["name"]][1]
                play.coordinate = player["player"]
                play.set_address
                shift = player["shift"]

        if play.coordinate > 1200 / 2 - 150 and scene["size"] > 1200 and (shift * -1) + 1200 + play.step < scene[
            "size"]:
            shift -= play.step
        else:
            play.coordinate += play.step
            play.set_address


def collision_check(setting, script, hitboxs, player_position, script_name, shift):
    for i in range(len(script)):
        if player_position + 60 > hitboxs[i][0] + shift and player_position + 60 < hitboxs[i][1] + shift:
            if len(script[i]) == 2:
                text_at_center(setting.screen, script_name[i], setting.wight / 2, 650)
                return script[i]
            ss = scripts.Scripts(script[i][0], script[i][1])
            return ss.start(setting)
    return None


def button(setting):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        play.walk(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return 40
            elif event.key == pygame.K_RIGHT:
                return -40
            elif event.key == pygame.K_e:
                return "e"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                return 0
    return -1


print(scene_set["01"][0])
widget(scene_set["02"][0], scene_set["02"][1])
