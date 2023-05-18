import dialogs_list
import diologs
import colors
import fightscreept

color = colors.Color()


class Location_set(object):
    def __init__(self, location, stage):
        self.lang = {"Русский": "ru", "English": "en"}
        self.location = location
        self.stage = stage
        self.objects_name = []
        self.hitbox = []
        self.scripts = []
        self.open_location_script = []

    def _1(self, inventory, language):
        scene_size = 1600
        self.objects_name = {"ru": ["Войти в Библиотеку"], "en": ["log in to the library"]}
        self.hitbox = [[1700, 2040]]
        self.scripts = [[Scripts.move, {"location_name": "02", "player_position": 120, "shift": 0}]]
        return self.objects_name[self.lang[language]]

    def _2(self, inventory, language):
        scene_size = 1200
        self.objects_name = {
            "ru": ["Выйти из Библиотеки", "Поговорить с Иваном Сергеевичем"],
            "en": ["Exit the library", "Talk to Ivan Sergeevich"]
        }
        self.hitbox = [[20, 100], [scene_size / 2 - 160, scene_size / 2 + 160]]
        self.scripts = [
            [Scripts.move, {"location_name": "01", "player_position": 595, "shift": -1195}],
            [Scripts.autor_script, _01]
        ]
        return self.objects_name[self.lang[language]]

    def _3(self, inventory, language):
        if self.stage == 1 and "mug" not in inventory:
            self.open_location_script = [
                [Scripts.diolog, {"id": dialogs_list._016, "inventory": ["mug"], "stage": 0}]
            ]
        if self.stage == 2 and "tea" not in inventory:
            self.open_location_script = [
                [Scripts.diolog, {"id": dialogs_list._019, "inventory": ["mug", "tea"], "stage": 0}]
            ]
        self.objects_name = {"ru": ["Выйти из кабинета"], "en": ["Exit the cabinet"]}
        self.hitbox = [[130, 230]]
        self.scripts = [[Scripts.move, {"location_name": "04", "player_position": 529, "shift": -1676}]]
        other_activity = {
            "ru": ["Поговорить с Юлией Сергеевной"] * 2 + ["Поговорить с Егором"] * 2 + ["Взять кружку", ""],
            "en": ["Talk to Yulia Sergeevna"] * 2 + ["Talk to Egor"] * 2 + ["Take a mug", ""],
            "pos": [[1957, 2305]] * 2 + [[4241, 4569]] * 2 + [[3538, 3618], [200, 210]],
            "scr": [
                [Scripts.empty_diolog, {"id": dialogs_list.e_1, "inventory": [], "stage": 0}],
                [Scripts.autor_script, _02],
                [Scripts.empty_diolog, {"id": dialogs_list.e_0, "inventory": [], "stage": 0}],
                [Scripts.diolog, {"id": dialogs_list._003, "inventory": ["quest"], "stage": 0}],
                [Scripts.diolog, {"id": dialogs_list._004, "inventory": ["mug"], "stage": 0}],
                [Scripts.autor_script, _06, "touch"]
            ]
        }
        if "mug" not in inventory and "quest" in inventory:
            self.append_activity(other_activity, -2, self.lang[language])
        if "quest" not in inventory:
            self.append_activity(other_activity, 3, self.lang[language])
        else:
            self.append_activity(other_activity, 2, self.lang[language])
        if "tea" in inventory or "quest" not in inventory:
            self.append_activity(other_activity, 0, self.lang[language])
        else:
            self.append_activity(other_activity, 1, self.lang[language])
        if self.stage == 2 and all(x in inventory for x in ["mug", "tea", "boiled water"]):
            self.append_activity(other_activity, 5, self.lang[language])
            self.scripts.pop(0)
            self.hitbox.pop(0)
            self.objects_name[self.lang[language]].pop(0)
        return self.objects_name[self.lang[language]]

    def _4(self, inventory, language):
        self.objects_name = {"ru": [], "en": []}
        self.hitbox, self.scripts = [], []
        other_activity = {
            "ru": ["Зайти в кабинет"] * 2 + ["Постучать"] * 2, "en": ["Exit the cabinet"] * 2 + ["Knock"] * 2,
            "pos": [[2019, 2475]] * 2 + [[1323, 1547]] * 2,
            "scr": [
                [Scripts.move, {"location_name": "03", "player_position": 140, "shift": 0}],
                [Scripts.move, {"location_name": "05", "player_position": 120, "shift": 0}],
                [Scripts.autor_script, _03], [Scripts.diolog, {"id": dialogs_list._021, "inventory": [], "stage": 0}]
            ]
        }

        if all(x in inventory for x in ["mug", "tea", "boiled water"]) and self.stage != 2:
            self.append_activity(other_activity, 1, self.lang[language])
        else:
            self.append_activity(other_activity, 0, self.lang[language])
        if all(x in inventory for x in ["mug", "tea", "quest"]) and "boiled water" not in inventory:
            self.append_activity(other_activity, 2, self.lang[language])
        else:
            self.append_activity(other_activity, 3, self.lang[language])
        return self.objects_name[self.lang[language]]

    def _5(self, inventory, language):
        self.objects_name = {"ru": [], "en": []}
        self.hitbox, self.scripts = [], []
        other_activity = {
            "ru": [""] * 2, "en": [""] * 2, "pos": [[180, 200]] * 2,
            "scr": [[Scripts.autor_script, _04, "Touch"], [Scripts.autor_script, _05, "Touch"]]
        }
        self.append_activity(other_activity, self.stage, self.lang[language])
        return self.objects_name[self.lang[language]]

    # Функция добавляет активные объекты по мере необходимости
    def append_activity(self, activity, index, language):
        self.objects_name[language].append(activity[language][index])
        self.hitbox.append(activity["pos"][index])
        self.scripts.append(activity["scr"][index])


class Scripts(object):
    def __init__(self, id, value, type=None):
        # type вид активации: None -> нажатие e, Touch -> Персонаж тронул Хитбокс объекта
        self.id = id
        self.value = value
        self.type = type

    def start(self, setting):
        return self.id(self, setting)

    # Возращаются все возможные значения для игры
    # return location, inventory, stage
    def move(self, setting):
        location = {
            "name": self.value["location_name"], "player": self.value["player_position"], "shift": self.value["shift"]
        }
        return location, [], 0

    def diolog(self, setting):
        diologs.Diologs(self.value['id'], setting)
        return {}, list(self.value["inventory"]), self.value['stage']

    def empty_diolog(self, setting):
        lang = {"Русский": "ru", "English": "en"}
        self.value['id'][lang[setting.language]] = self.value['id']["funk"](lang[setting.language])
        diologs.Diologs(self.value['id'], setting)
        return {}, list(self.value["inventory"]), self.value['stage']

    def take(self, setting):
        return {}, list(self.value["inventory"]), 0

    # доработать!!!!
    def fight(self, setting):
        fightscreept.fight(setting.screen, self.value)
        return {}, [], 0

    def autor_script(self, setting):
        location = {}
        inventory = []
        stage = 0
        for i in self.value:
            sc = Scripts(i[0], i[1])
            loc, inv, st = sc.start(setting)
            if loc != {}:
                location = loc
            if len(inv) != 0:
                for i in inv:
                    inventory.append(i)
            stage += st
        return location, inventory, stage


_01 = [
    [Scripts.diolog, {"id": dialogs_list._001, "inventory": [], "stage": 0}],
    [Scripts.move, {"location_name": "03", "player_position": 524, "shift": -4109}],
    [Scripts.diolog, {"id": dialogs_list._002, "inventory": [], "stage": 0}]
]
_02 = [
    [Scripts.diolog, {"id": dialogs_list._005, "inventory": [], "stage": 0}],
    [Scripts.fight, "I am Ayur"],
    [Scripts.diolog, {"id": dialogs_list._006, "inventory": [], "stage": 0}],
    [Scripts.fight, "I am from the second group"],
    [Scripts.diolog, {"id": dialogs_list._007, "inventory": [], "stage": 0}],
    [Scripts.fight, "I NEED TO FIND SOME TEA"],
    [Scripts.diolog, {"id": dialogs_list._008, "inventory": ["tea"], "stage": 0}]
]
_03 = [
    [Scripts.diolog, {"id": dialogs_list._009, "inventory": [], "stage": 0}],
    [Scripts.fight, "I am a student from the second group"],
    [Scripts.diolog, {"id": dialogs_list._010, "inventory": [], "stage": 0}],
    [Scripts.fight, "I need some boiling water"],
    [Scripts.diolog, {"id": dialogs_list._011, "inventory": ["boiled water"], "stage": 0}],
]
_04 = [
    [Scripts.diolog, {"id": dialogs_list._012, "inventory": [], "stage": 0}],
    [Scripts.diolog, {"id": dialogs_list._013, "inventory": [], "stage": 0}],
    [Scripts.diolog, {"id": dialogs_list._014, "inventory": [], "stage": 0}],
    [Scripts.move, {"location_name": "03", "player_position": 524, "shift": -4109}],
    [Scripts.diolog, {"id": dialogs_list._015, "inventory": ["reset"], "stage": 1}],
    [Scripts.diolog, {"id": dialogs_list._002, "inventory": [], "stage": 0}]
]
_05 = [
    [Scripts.diolog, {"id": dialogs_list._017, "inventory": [], "stage": 0}],
    [Scripts.move, {"location_name": "03", "player_position": 524, "shift": -4109}],
    [Scripts.diolog, {"id": dialogs_list._018, "inventory": ["reset"], "stage": 1}],
    [Scripts.diolog, {"id": dialogs_list._002, "inventory": [], "stage": 0}]
]

_06 = [
    [Scripts.diolog, {"id": dialogs_list._020_1, "inventory": [], "stage": 0}],
    [Scripts.diolog, {"id": dialogs_list._020_2, "inventory": ["end"], "stage": 1}],
]
