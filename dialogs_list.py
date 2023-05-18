import random
import pygame

emp = {"ru": ["Хмммм?", "Тебе что-то нужно?"], "en": ["Hmmmm?", "Do you need something?"]}

bg2 = pygame.image.load("location/2.png")
bg3 = pygame.image.load("location/3.png")
bg4 = pygame.image.load("location/4.png")
bg4 = pygame.transform.scale(bg4, (2878, 720))
bg5 = pygame.image.load("location/05.png")


def funk_e0(language):
    if language == 'ru':
        return [(emp["ru"] + ["Я хочу чая"])[random.randint(0, 2)]]
    elif language == 'en':
        return [(emp["en"] + ["I want tea"])[random.randint(0, 2)]]


def funk_e1(language):
    if language == 'ru':
        return [(emp["ru"] + ["Аюр, не забывай о проекте", "Я сейчас занята", "Вам нужно работать над проектом"])[
                    random.randint(0, 4)]]
    elif language == 'en':
        return [(emp["en"] + ["Ayur, don't forget about the project", "You need to work on a project",
                              "I'm busy right now"])[
                    random.randint(0, 4)]]


_001 = {
    'person_ru': ["Аюр", "Иван Сергеевич"], 'person_en': ["Ayur", "Ivan Sergeyevich"],
    'with_who': "NPC\\petrushin\\npc-", 'who_talk': [1, 0, 1, 1, 0], 'fill': [bg2, 0],
    'ru': [
        "Аюр, я ждал тебя", "Иван Сергеевич!",
        "Ты поступил к нам в ФБКи как и говорило пророчество, с этих пор ФБКи изменится",
        "Но к сожалению авторы смогли позволить только мое Комео", "Что!?"
    ],
    'en': [
        "Ayur, I've been waiting for you", "Ivan Sergeyevich!",
        "You came to us in FBKi as the prophecy said, from now on, FBKi will change",
        "But unfortunately the authors could only allow my cameo", "What!?"
    ]
}
_002 = {
    'person_ru': ["Аюр", "Юлия Сергеевна", "Мысли Аюра"], 'person_en': ["Ayur", "Yulia Sergeevna", "Ayur's Thoughts"],
    'with_who': 'NPC\\iovleva\\npc-', 'who_talk': [1, 0, 1, 2, 2, 2], 'fill': [bg3, -4109],
    'ru': [
        "Аюр!", "А да!?",
        "Я хотела напомнить что скоро у вас будет сдача проектов по английскому. На следующей неделе " + \
        "вы должны показать что у вас готово", "А! На следующей неделе!?",
        "Что теперь делать? Ведь мы даже ещё не начали работу", "Надо поговорить c Егором"
    ],
    'en': [
        "Ayur!", "Oh?",
        "I wanted to remind you that soon you will have the delivery of projects in English. Next week you have to " + \
        "show what you have ready", "Ah! Next week!?", "What should I do now? We haven't even started work yet",
        "I need to talk to Egor"
    ]
}
_003 = {
    'person_ru': ["Аюр", "Егор", "Мысли Аюра"], 'person_en': ["Ayur", "Egor", "Ayur's Thoughts"],
    'with_who': "NPC\\egor\\npc-", 'who_talk': [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 2], 'fill': [bg3, -3615],
    'ru': [
        "Егор!", "Да?", "Ты слышал? Нам нужно уже закончить работу, а мы её ещё не начинали.",
        "А, да? Может позже?", 'Какой "позже", у нас осталась неделя до первого показа!',
        "Ну у меня нет настроения, так ещё сегодня и две пары английского", "...",
        "Раз у нас две пары давай будем пить чай во время работы!", "Ладно с чаем я работать согласен",
        "Но к сожалению я оставил кружку в общаге, так что чая мне не видать",
        "Но если ты ПРИНЕСЕШЬ мне чай, я сегодня же сяду за проект",
        "Отлично! я смог убедить его работать. Я знаю что кипяток можно взять на кафедре, но вот чашка и " + \
        "чайный пакетик..."
    ],
    'en': [
        "Egor!", "Yes?", "Did you hear that? We need to finish the work already, and we haven't started it yet.",
        "Oh, really? Maybe later?", 'What a "later", we have a week left before the first show!',
        "But I'm not in the mood, besides, there will be two pairs of English today", "...",
        "Since we have two pairs, let's drink tea while working!", "Okay, I agree to work with tea",
        "But unfortunately I left the mug in the dorm, so I won't see any tea",
        "But if you BRING me tea, I'll sit down for the project today.",
        "Great! I managed to convince him to work. I know I can get boiling water in the teacher's room, but here's " + \
        "a cup and a tea bag..."
    ]
}

_004 = {
    'person_ru': ["Мысли Аюра"], 'person_en': ["Ayur's Thoughts"], 'with_who': "", 'who_talk': [0],
    'fill': [bg3, -3000],
    'ru': ["Надеюсь никто не обидится если я её возьму"], 'en': ["I hope no one will be offended if I take it"]
}

_005 = {
    'person_ru': ["Аюр", "Юлия Сергеевна", "Мысли Аюра"], 'person_en': ["Ayur", "Yulia Sergeevna", "Ayur's Thoughts"],
    'with_who': "NPC\\iovleva\\npc-", 'who_talk': [0, 1, 0, 1, 0, 2, 0, 1, 1, 0, 1], 'fill': [bg3, -1624],
    'ru': [
        "Юлия Сергеевна", "Да?", "Я бы хотел попросить у вас чайный покетик",
        "Хорошо, я дам тебе чайный пакетик, но ты должен ответить на 3 моих вопроса на английском", "...",
        "Мне так не хочется сейчас повторять правила, но я должен это сделать, ради чая, ради Егора",
        "Хорошо, я отвечу на ваши вопросы", "Для начала я напомню тебе правила составления ПРЕДЛОЖЕНИЙ на английском",
        "Сначала СУЩЕСТВИТЕЛЬНОЕ, затем ГЛАГОЛ, а после все остальное", "Понял", "Первый вопрос: кто ты?"
    ],
    'en': [
        "Yulia Sergeevna", "Yes?", "I would like to ask you for a tea bag",
        "OK, I'll give you a tea bag, but you have to answer my 3 questions in English", "...",
        "I don't want to repeat the rules now, but I have to do it, for the sake of tea, for Egor's sake",
        "Alright, I'll answer your questions",
        "To begin with, I'll remind you of the rules for making SENTENCES in English",
        "First the NOUN, then the VERB, and then everything else", "I understood", "The first question is: who are you?"
    ]
}

_006 = {
    'person_ru': ["Юлия Сергеевна"], 'person_en': ["Yulia Sergeevna"], 'with_who': "NPC\\iovleva\\npc-",
    'who_talk': [0], 'fill': [bg3, -1624],
    'ru': ["Второй: из какой ты группы?"],
    'en': ["Second: what group are you from?"]
}

_007 = {
    'person_ru': ["Юлия Сергеевна"], 'person_en': ["Yulia Sergeevna"], 'with_who': "NPC\\iovleva\\npc-",
    'who_talk': [0], 'fill': [bg3, -1624],
    'ru': ["Третий: что тебе нужно сделать?"],
    'en': ["The third: what do you need to do?"]
}

_008 = {
    'person_ru': ["Аюр", "Юлия Сергеевна", "Мысли Аюра"], 'person_en': ["Ayur", "Yulia Sergeevna", "Ayur's Thoughts"],
    'with_who': "NPC\\iovleva\\npc-", 'who_talk': [1, 1, 2, 2, 2, 0], 'fill': [bg3, -1624],
    'ru': [
        "Вобще-то я хотела услышать, что тебе нужно сделать домашнее задание.", "Но вообщем не важно, вот твой пакетик",
        "Ура! Ещё один фрагмент чая собран!", "Фрагмент? что я только что сказал?", "А ладно неважно",
        "Спасибо вам Юлия Сергеевна"
    ],
    'en': [
        "Actually, I wanted to hear that you need to do your homework.",
        "But in general, it doesn't matter, here's your tea bag",
        "Hurray! Another fragment of tea has been collected!", "A fragment? What did I just say?",
        "Oh, well, it doesn't matter", "Thank you Yulia Sergeevna"
    ]
}

_009 = {
    'person_ru': ["Мысли Аюр", "ВанБум"], 'person_en': ["Ayur's Thoughts", "van Boom"],
    'with_who': "NPC\\vanboom\\door2.", 'who_talk': [1, 0, 0], 'fill': [bg4, -901],
    'ru': [
        "Hello, who are you? (Здравствуйте, кто вы?)",
        "Ой! что мне теперь делать? ВанБум понимает только на английском!",
        "Ну что же пришло время вспомнить все чему меня учила Юлия Сергеевна!"
    ],
    'en': [
        "Hello, who are you?", "Oh! What should I do now? van Boom understands only English!",
        "Well, it's time to remember everything that Yulia Sergeevna taught me!"
    ]
}

_010 = {
    'person_ru': ["Мысли Аюр", "ВанБум"], 'person_en': ["Ayur's Thoughts", "van Boom"],
    'with_who': "NPC\\vanboom\\door2.", 'who_talk': [1, 0, 0], 'fill': [bg4, -901],
    'ru': ["What are you need? (что тебе нужно?)", "Ай! Как же будет кипяток на английском?!", "Точно! Boiled water"],
    'en': ["What are you need?", "Ah! How will the boiling water be in English?!", "Precisely! Boiled water"]
}

_011 = {
    'person_ru': ["Мысли Аюр", "ВанБум", "Аюр"], 'person_en': ["Ayur's Thoughts", "VanBoom", "Ayur"],
    'with_who': "NPC\\vanboom\\door2.", 'who_talk': [1, 0, 2], 'fill': [bg4, -901],
    'ru': ["No problem here", "Фух, я все сказал верно. Егор, жди меня с чаем!", "Thank you!"],
    'en': ["No problem here", "Phew, I said it right. Egor, wait for me with tea!", "Thank you!"]
}

_012 = {
    'person_ru': ["Аюр"], 'person_en': ["Ayur"], 'with_who': "", 'who_talk': [0, 0], 'fill': [bg5, 0],
    'ru': ["Чего!?", "Куда делся кабинет?"], 'en': ["What!?", "Where did the office go?"]
}

_013 = {
    'person_ru': ["Аюр", "Кто-то"], 'person_en': ["Ayur", "Somebody"], 'with_who': "NB",
    'who_talk': [1, 0, 0], 'fill': [bg5, 0],
    'ru': [
        "Извини, Аюр, твой Егор в другом замке!", "Мы не в Марио что бы так шутить!",
        "Девочки, это уже не смешно!"
    ],
    'en': [
        "Sorry, Ayur, your Egor is in another castle!", "We are not in Mario to joke like that!",
        "Girls, it's not funny anymore!"
    ]
}

_014 = {
    'person_ru': ["Аюр", "Наташа и Юля"], 'person_en': ["Ayur", "Natasha and Yulia"], 'with_who': "Au",
    'who_talk': [0, 0, 1, 1, 0], 'fill': [bg5, 0],
    'ru': [
        "Серьезно!", "Где концовка!", "Ну извини, мы немного не успели...",
        "Но если тебе хочется ты можешь попробовать снова", "Что!?"
    ],
    'en': [
        "Seriously", "Where is the ending!", "Well, sorry, we didn't have time...",
        "But if you want to, you can try again.", "What!?"
    ]
}

_015 = {
    'person_ru': ["Аюр"], 'person_en': ["Ayur"], 'with_who': "", 'who_talk': [0], 'fill': [bg3, -4109],
    'ru': ["Блин!"], 'en': ["Damn!"]
}

_016 = {
    'person_ru': ["Мысли Аюра"], 'person_en': ["Ayur's Thoughts"], 'with_who': "", 'who_talk': [0, 0, 0],
    'fill': [bg3, -4109],
    'ru': ["Что!?", "Почему кружка осталась у меня?", "Ладно, тем мне меньше ходить"],
    'en': ["What!?", "Why did I keep the mug?", "Okay, the less I walk"]
}

_017 = {
    'person_ru': ["Аюр", "Наташа и Юля"], 'person_en': ["Ayur", "Natasha and Yulia"], 'with_who': "Au",
    'who_talk': [0, 1, 0], 'fill': [bg5, 0],
    'ru': ["Вы серьезно?", "Ну мы же сказали, здесь нет конца", "Я должен пренести чай! И вы меня не остановите!"],
    'en': ["Are you serious?", "Well, we said there is no end here", "I have to bring tea! And you won't stop me!"]
}

_018 = {
    'person_ru': ["Аюр"], 'person_en': ["Ayur"], 'with_who': "", 'who_talk': [0], 'fill': [bg3, -4109],
    'ru': ["Что опять!?"], 'en': ["What again!?"]
}

_019 = {
    'person_ru': ["Мысли Аюра"], 'person_en': ["Ayur's Thoughts"], 'with_who': "", 'who_talk': [0, 0, 0],
    'fill': [bg3, -4109],
    'ru': ["Что!?", "Теперь и чайный пакетик?", "Тут явно кто-то забывает чистить инвентарь"],
    'en': ["What!?", "Now the tea bag?", "Clearly someone forgets to clean the inventory here"]
}

_020_1 = {
    'person_ru': ["Аюр", "Егор"], 'person_en': ["Ayur", "Egor"], 'with_who': "NPC\\egor\\npc-",
    'who_talk': [0, 1, 0, 1], 'fill': [bg3, -3615],
    'ru': ["Да! я же сказал, что дойду до сюда!", "Аюр, ты о чём?", "Ни о чем, вот твой чай", "Спасибо"],
    'en': ["Yes! I told you I'd get here!", "Ayur, what are you talking about?", "Nothing, here's your tea", "Thanks"]
}

_020_2 = {
    'person_ru': ["Аюр", "Егор"], 'person_en': ["Ayur", "Egor"], 'with_who': "NPC\\egor\\mug-",
    'who_talk': [1, 0, 1, 0], 'fill': [bg3, -3615],
    'ru': ["Эм... Аюр...", "Да?", "Чай остыл ты можешь пренести другой?", "Да, блин!"],
    'en': ["Oh... Ayur...", "Yes?", "The tea is cold, can you bring another one?", "Damn it!"]
}

_021 = {
    'person_ru': ["Мысли Аюра"], 'person_en': ["Ayur's Thoughts"], 'with_who': "", 'who_talk': [0], 'fill': [bg4, -901],
    'ru': ["Не думаю что мне сейчас туда нужно"], 'en': ["I don't think I need to go there right now"]
}

e_0 = {
    'person_ru': ["Егор"], 'person_en': ["Egor"], 'with_who': "NPC\\egor\\npc-", 'who_talk': [0], 'fill': [bg3, -3615],
    "funk": funk_e0
}

e_1 = {
    'person_ru': ["Юлия Сергеевна"], 'person_en': ["Yulia Sergeevna"], 'with_who': "NPC\\iovleva\\npc-",
    'who_talk': [0], 'fill': [bg3, -1624], "funk": funk_e1
}
