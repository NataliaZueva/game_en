import menu
import pygame
import scene_list as sl
import scripts
import colors
import player as pl

color = colors.Color()
player = pl.Player("Ayur\left\left-stand-1.png")

scene_set = {
    "01": [sl._1, scripts.Location_set._1], "02": [sl._2, scripts.Location_set._2],
    "03": [sl._3, scripts.Location_set._3], "04": [sl._4, scripts.Location_set._4],
    "05": [sl._5, scripts.Location_set._5]
}


def text_at_center(screen, message, x, y):
    font = pygame.font.SysFont('Comic Sans MS', 20)
    text = font.render(message, True, color.BLACK)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def window():
    pygame.init()
    setting = menu.Setting()
    Menu = menu.Menu()
    clock = pygame.time.Clock()

    screen = ["01", 30, 0]
    inventory = []
    stage = 0

    scen, inv, st = Menu.window(setting, {}, [], 0)

    mug = pygame.image.load("NPC\\cup.png")
    pygame.mixer.music.load("music\\Island Dream - Chris Haugen.mp3")
    pygame.mixer.music.play(-1)

    screen[0] = scen["name"]
    player.coordinate = scen["player"]
    screen[2] = scen["shift"]
    stage += st
    if len(inv) != 0:
        for i in inv:
            inventory.append(i)
    while 1:
        clock.tick(30)

        scen = {}
        inv = []
        st = 0

        if "end" in inventory:
            menu.Credits(setting)
            Menu.has_the_game_started = True
            Menu.select_window = 0
            stage = 0
            inventory = []
            scen, inv, st = Menu.window(setting, {}, [], 0)

        if "reset" in inventory:
            inventory = []

        scene_set[screen[0]][0]["screen"](setting, scene_set[screen[0]][0]["size"], screen[2], player)
        location = scripts.Location_set(scene_set[screen[0]][1], stage)
        set = location.location(location, inventory, setting.language)

        for i in location.open_location_script:
            scen, inv, st = scripts.Scripts(i[0], i[1]).start(setting)
            inventory = inv

        if scene_set[screen[0]][0]["screen"] == sl._3_load and "mug" not in inventory:
            rect = mug.get_rect(center=(3580 + screen[2], 394))
            setting.screen.blit(mug, rect)

        if screen[0] == '03':
            player.draw(setting)

        collision = collision_check(setting, location, player.coordinate, set, screen[2])
        pygame.display.update()

        if collision != None and len(collision) != 2:
            scen, inv, st = scripts.Scripts(collision[0], collision[1]).start(setting)
            player.step = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT and menu.are_you_sure(setting):
                quit()
            player.walk(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    scen, inv, st = Menu.window(setting, {"name": screen[0], "player": player.coordinate, \
                                                          "shift": screen[2]}, inventory, stage)
                    player.step = 0
                    pygame.mixer.music.load("music\\Island Dream - Chris Haugen.mp3")
                    pygame.mixer.music.play(-1)
                if event.key == pygame.K_e:
                    if collision != None:
                        player.step = 0
                        scen, inv, st = scripts.Scripts(collision[0], collision[1]).start(setting)

        if len(list(scen.keys())) != 0:
            screen[0] = scen["name"]
            player.coordinate = scen["player"]
            screen[2] = scen["shift"]

        stage += st
        if stage + st > 2:
            stage = 2
        if len(inv) != 0:
            for i in inv:
                if i not in inventory:
                    inventory.append(i)

        if screen[2] - player.step < 0 and screen[2] + scene_set[screen[0]][0]["size"] - player.step > setting.wight \
                and player.coordinate > setting.wight / 2 - 140 and player.coordinate < setting.wight / 2:
            screen[2] -= player.step
        else:
            if player.coordinate + player.step >= scene_set[screen[0]][0]["scene_boundaries"][0] and \
                    player.coordinate + player.step <= setting.wight - scene_set[screen[0]][0]["scene_boundaries"][1]:
                player.coordinate += player.step


def collision_check(setting, location, player_position, script_name, shift):
    for i in range(len(location.scripts)):
        if player_position + 60 > location.hitbox[i][0] + shift and \
                player_position + 60 < location.hitbox[i][1] + shift:
            text_at_center(setting.screen, script_name[i], setting.wight / 2, 650)
            return location.scripts[i]
    return None


window()
