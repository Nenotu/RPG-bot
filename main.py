import random
import telebot
from telebot import types
import time

token = '5606527576:AAFTY1rPjdsZIUTXNE3A2SpakvPoto1mGXs'
bot = telebot.TeleBot(token)
hp = 1000
damage = 1000
exp = 0
lvl = 1
race = ''
profesion = ''
current_drop = ()
current_drop_category = ''
replace_item_index = 0
equip_item_category = ""
equip_item = {'оружие': (), 'броня': ()}
race_database = {'Эльф': {'hp': 10, 'damage': 14},
                 'Гном': {'hp': 12, 'damage': 13},
                 'Гоблин': {'hp': 13, 'damage': 11},
                 'Дворф': {'hp': 15, 'damage': 12}}
profesion_database = {'Лучник': {'hp': 35, 'damage': 20},
                      'Бард': {'hp': 30, 'damage': 30},
                      'Воин': {'hp': 45, 'damage': 15},
                      'Волшебник': {'hp': 35, 'damage': 25}}
inventory = {'оружие': [], 'броня': [], 'кушалка': []}  # (меч, обычный, 500)
weapon_name = ['Меч', 'Лук', 'Книга']
rare = {1: 'Обычный', 2: 'Редкий', 3: 'Эпический', 4: 'Легендарный'}
armor_type_list = ['Шлем', 'Нагрудник', 'Ботинки']
food_type_list = ['Искушение Адепта', 'Креветочные печенья сакуры', 'Мондштадтские оладушки']
enemy_name = ['Слайм', 'Крыса', 'Хиличурл']
victim = None

def create_monster():
    rnd_name = random.choice(enemy_name)
    hp_enemy = 0
    exp_drop = 0
    if rnd_name == enemy_name[0]:
        hp_enemy = 50
        exp_drop = 20
    elif rnd_name == enemy_name[1]:
        hp_enemy = 30
        exp_drop = 10
    elif rnd_name == enemy_name[2]:
        hp_enemy = 80
        exp_drop = 30
    damage_enemy = random.randrange(20, 50)
    return [rnd_name, hp_enemy, damage_enemy, exp_drop]


def game_start():
    hp = 1000
    damage = 1000
    inventory = {'оржие': [], 'броня': [], 'кушалка': []}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать игру')
    btn2 = types.KeyboardButton('История игры')
    markup.add(btn1, btn2)
    return markup


def make_race_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Эльф'
    btn2 = 'Гном'
    btn3 = 'Гоблин'
    btn4 = 'Дворф'
    btn5 = 'Возвращаемся в лагерь'
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup


def make_profesion_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Лучник'
    btn2 = 'Бард'
    btn3 = 'Воин'
    btn4 = 'Волшебник'
    btn5 = 'Возвращаемся в лагерь'
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup


def start_quest():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Отправляемся в путь'
    btn2 = 'Возвращаемся в лагерь'
    markup.add(btn1, btn2)
    return markup


def keep_going():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Продолжаем путешествие'
    btn2 = 'Возвращаемся в лагерь'
    markup.add(btn1, btn2)
    return markup


def bully():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Принять свою участь'
    btn2 = 'БЕЖАТЬ!!!'
    btn3 = "Открыть инвентарь"
    btn4 = 'Возвращаемся в лагерь'
    markup.add(btn1, btn2, btn3, btn4)
    return markup


def battle():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Атаковать'
    btn2 = 'Блокировать'
    markup.add(btn1, btn2)
    return markup


def return_():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Возвращаемся в лагерь'
    markup.add(btn1)
    return markup


def replace_item():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Заменить'
    btn2 = 'Не заменять'
    markup.add(btn1, btn2)
    return markup


def add_item():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Добавить'
    btn2 = 'Не добавлять'
    markup.add(btn1, btn2)
    return markup

def search_body():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Уйти'
    btn2 = 'Обыскать труп'
    btn3 = types.KeyboardButton('Возвращаемся в лагерь')
    markup.add(btn1, btn2, btn3)
    return markup

def want_to_replace():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Хочу'
    btn2 = 'Не хочу'
    btn3 = types.KeyboardButton('Возвращаемся в лагерь')
    markup.add(btn1, btn2, btn3)
    return markup

def categories_to_change():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Оружие'
    btn2 = 'Броня'
    btn3 = 'Кушалка'
    markup.add(btn1, btn2, btn3)
    return markup

def create_weapon():
    damage = 0
    wpn_type = weapon_name[random.randrange(0, 3)]
    wpn_rare = random.choices(list(rare.keys()), weights=[4, 3, 2, 1])
    if wpn_rare[0] == 1:
        damage += 20
    elif wpn_rare[0] == 2:
        damage += 33
    elif wpn_rare[0] == 3:
        damage += 46
    elif wpn_rare[0] == 4:
        damage += 60
    return wpn_type, rare[wpn_rare[0]], damage


def create_armor():
    hp = 0
    arm_type = armor_type_list[random.randrange(0, 3)]
    arm_rare = random.choices(list(rare.keys()), weights=[4, 3, 2, 1])
    if arm_rare[0] == 1:
        hp += 20
    elif arm_rare[0] == 2:
        hp += 33
    elif arm_rare[0] == 3:
        hp += 46
    elif arm_rare[0] == 4:
        hp += 60
    return arm_type, rare[arm_rare[0]], hp


def create_food():
    hp = 0
    food_type = food_type_list[random.randrange(0, 3)]
    food_rare = random.choices(list(rare.keys()), weights=[4, 3, 2, 1])
    if food_rare[0] == 1:
        hp += 20
    elif food_rare[0] == 2:
        hp += 33
    elif food_rare[0] == 3:
        hp += 46
    elif food_rare[0] == 4:
        hp += 60
    return food_type, rare[food_rare[0]], hp

def item_existence_check(message, current_drop_category):
    i = 0
    for item in inventory[current_drop_category]:
        if item[0] == current_drop[0]:
            replace_item_index = i
            bot.send_message(message.chat.id,
                             text='В вашем инвентаре уже есть похожий предмет. Заменить его?',
                             reply_markup=replace_item())
            return replace_item_index
        i += 1
    else:
        bot.send_message(message.chat.id, text='Добавить этот предмет в инвентарь?',
                         reply_markup=add_item())


def form_inventory_msg(category_list):
    msg = ''
    for i in category_list:
        msg += f'<b>{i[0].upper() + i[1:]}</b>:\n'
        j = 0
        for item in inventory[i]:
            msg += f'{j + 1}. {item[0]} - {item[1]} - {item[2]}\n'
            j += 1
    msg += 'Хотите ли вы надеть/поменять что-либо из инвентаря?'
    return msg

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text='Не хочешь поиграть, Джорди? ', reply_markup=game_start())

@bot.message_handler(content_types=['text'])
def game_body(message):
    global hp, damage, race, profesion, victim, exp, lvl, inventory, current_drop_category, current_drop, \
        replace_item_index, equip_item_category, equip_item
    if message.text == 'Начать игру':
        bot.send_message(message.chat.id, text='Выбери расу, мой дорогой друг.',
                         reply_markup=make_race_menu())

    if message.text == 'История игры':
        bot.send_message(message.chat.id,
                         text='Ты проснулся, не помня ничего.\nПозади тебя был водопад, а рядом разбитая лодка.\nВпереди был беспросветный лес.\n"Где мои вещи?"\n"И где вообще я?"\n"Надо все разузнать..." - подумал ты.',
                         reply_markup=game_start())
        photo = open(r"img\лес.jpg", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()

    if message.text == 'Возвращаемся в лагерь':
        bot.send_message(message.chat.id, text='Не хочешь поиграть, Джорди? ', reply_markup=game_start())

    if message.text == 'Эльф' or message.text == 'Гном' or message.text == 'Гоблин' or message.text == 'Дворф':
        race = message.text
        path = r"race\\" + message.text + '.jpg'
        img = open(path, 'rb')
        hp += race_database[message.text]['hp']
        damage += race_database[message.text]['damage']
        bot.send_photo(message.chat.id, img,
                       caption=f'Вы {message.text},\nУ вас {hp} хп, \nТакже {damage} урона,\nВыберите класс',
                       reply_markup=make_profesion_menu())
        img.close()

    if message.text == 'Лучник' or message.text == 'Бард' or message.text == 'Воин' or message.text == 'Волшебник':
        profesion = message.text
        hp += profesion_database[message.text]['hp']
        damage += profesion_database[message.text]['damage']
        photo_path = r"race\\" + race + '_' + profesion + '.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(message.chat.id, photo,
                         caption=f'Вы {profesion} - {race},\nУ вас {hp} хп, \nТакже {damage} урона,\nОтправляемся в путь?',
                         reply_markup=start_quest())
        photo.close()

    if message.text == 'Отправляемся в путь' or message.text == 'Продолжаем путешествие':
        event = random.randint(1, 2)
        if event == 1:
            bot.send_message(message.chat.id,
                             text=f'Вы никого не встретили,\nИдем дальше?\n(Хочешь вернуться в лагерь?)',
                             reply_markup=keep_going())
        elif event == 2:
            victim = create_monster()
            bot.send_message(message.chat.id,
                             text=f'Вы наткнулись на {victim[0]},\nУ него {victim[1]} хп,\nА также {victim[2]} урона,\nПринять сражение?\n(Хочешь вернуться в лагерь?)',
                             reply_markup=bully())

    if message.text == 'Принять свою участь':
        bot.send_message(message.chat.id, text='Вы насторожились \nИ стали думать что применить', reply_markup=battle())

    if message.text == 'Атаковать':
        victim[1] -= damage
        if victim[1] <= 0:
            exp += victim[3]
            if exp >= lvl * 100:
                lvl += 1
                damage += lvl * 2
                hp += lvl * 3
                bot.send_message(message.chat.id, text='ПОДНЯТИЕ УРОВНЯ!!!')
            thing = random.randrange(0, 3)
            if thing == 0:
                current_drop_category = 'оружие'
                current_drop = create_weapon()
                bot.send_message(message.chat.id,
                                 text=f'Вам выпало новое оружие: {current_drop[0]} - {current_drop[1]} - {current_drop[2]}')
                # проверка на наличие похожего оружия
                replace_item_index = item_existence_check(message, current_drop_category)
            elif thing == 1:
                current_drop_category = 'броня'
                current_drop = create_armor()
                bot.send_message(message.chat.id,
                                 text=f'Вам выпала новая броня: {current_drop[0]} - {current_drop[1]} - {current_drop[2]}')
                # проверка на наличие похожего оружия
                replace_item_index = item_existence_check(message, current_drop_category)
            elif thing == 2:
                current_drop_category = 'кушалка'
                current_drop = create_food()
                bot.send_message(message.chat.id,
                                 text=f'Вам выпала новая кушалка: {current_drop[0]} - {current_drop[1]} - {current_drop[2]}')
                # проверка на наличие похожего оружия
                replace_item_index = item_existence_check(message, current_drop_category)
        elif victim[1] > 0:
            hp -= victim[2]
            bot.send_message(message.chat.id, text=f'Монстр вас атаковал')
            if hp > 0:
                bot.send_message(message.chat.id, text=f'У {victim[0]}, осталось {victim[1]} хп')
                bot.send_message(message.chat.id, text=f'У вас осталось хп {hp}', reply_markup=battle())
            elif hp <= 0:
                bot.send_message(message.chat.id, text='Game Over', reply_markup=return_())

    if message.text == 'Блокировать':
        # а если щита нет?
        bot.send_message(message.chat.id,
                         text=f'Вы заблокировали {damage}')  # урон равный щиту

    if message.text == 'БЕЖАТЬ!!!':
        event = random.randint(1, 2)
        if event == 1:
            hp -= victim[2]
            bot.send_message(message.chat.id,
                             text=f'{victim[0]} - крыса,\nОн не стал ждать и сделал,\nУДАР В СПИНУ!!! \nУ вас осталось хп {hp}')
        elif event == 2:
            bot.send_message(message.chat.id, text="Вы успешно сбежали от монстра", reply_markup=keep_going())

    if message.text == 'Добавить':
        inventory[current_drop_category].append(current_drop)
        bot.send_message(message.chat.id, text=f'{current_drop_category} успешно добавлено в инвентарь',
                         reply_markup=keep_going())

    if message.text == 'Не добавлять':
        bot.send_message(message.chat.id, text='Понятно всё с тобой, зажравшийся p2w',
                         reply_markup=keep_going())

    if message.text == 'Заменить':
        inventory[current_drop_category][replace_item_index] = current_drop
        bot.send_message(message.chat.id, text=f'{current_drop_category} успешно заменено',
                         reply_markup=keep_going())

    if message.text == 'Не заменять':
        bot.send_message(message.chat.id, text='Ладно. Дальше идём?',
                         reply_markup=keep_going())

    if message.text == 'Открыть инвентарь':
        msg = ''
        if len(inventory['оружие']) > 0 or len(inventory['броня']) > 0 or len(inventory['кушалка']) > 0:
            not_empty_categories_list = []
            for i in inventory.keys():
                if len(inventory[i]) > 0:
                    not_empty_categories_list.append(i)
            msg = form_inventory_msg(not_empty_categories_list)
            bot.send_message(message.chat.id, text=msg, parse_mode='HTML', reply_markup=want_to_replace())
        else:
            bot.send_message(message.chat.id, text='Инвентарь пуст 😱', parse_mode='HTML', reply_markup=bully())

    if message.text == 'Хочу':
        bot.send_message(message.chat.id, text='Предметы из какой категории вы хотите надеть/поменять?', reply_markup=categories_to_change())

    if message.text == 'Не хочу':
        bot.send_message(message.chat.id, text='Как вам будет угодно', reply_markup=bully())

    if message.text == 'Оружие':
        equip_item_category = 'оружие'
        bot.send_message(message.chat.id, text='Введите номер оружия, которое вы хотите надеть/поменять')
    if message.text == 'Броня':
        equip_item_category = 'броня'
        bot.send_message(message.chat.id, text='Введите номер брони, которую вы хотите надеть/поменять')
    if message.text == 'Кушалка':
        equip_item_category = 'кушалка'
        bot.send_message(message.chat.id, text='Введите номер еды, которой вы хотите восполнить свое здоровье')

    if message.text.isdigit(): # проверить, что ввели числа. Можно использовать ф-ю is_digit()
        choice = int(message.text) - 1
        while choice >= len(inventory[equip_item_category]) or choice < 0:
            bot.send_message(message.chat.id, text='Введите номер СУЩЕСТВУЮЩЕГО предмета', reply_markup=bully())
        else:
            if equip_item_category == 'кушалка':
                hp += inventory[equip_item_category][choice][2]
                del inventory[equip_item_category][choice]
                bot.send_message(message.chat.id, text=f'Как прекрасно что мы поели\nВаше здоровье раняется {hp}  еденицам',
                                 reply_markup=bully())
            elif equip_item[equip_item_category] == ():
                equip_item[equip_item_category] = inventory[equip_item_category][choice]
                if equip_item_category == 'оружие':
                    damage += equip_item[equip_item_category][2]
                    bot.send_message(message.chat.id, text=f'Ты успешно взял предмет\nТвой урон равняется {damage}еденицам',
                                     reply_markup=bully())
                elif equip_item_category == 'броня':
                    hp += equip_item[equip_item_category][2]
                    bot.send_message(message.chat.id, text=f'Ты успешно надел предмет\nТвое здоровье равняется {damage}еденицам',
                                     reply_markup=bully())
            else:
                old_item =  equip_item[equip_item_category]
                new_item = inventory[equip_item_category][choice]
                equip_item[equip_item_category] = new_item
                if equip_item_category == 'оружие':
                    damage = damage - old_item[2] + new_item[2]
                    bot.send_message(message.chat.id, text=f'Ты успешно поменял оружие\nТвой урон равняется {hp}еденицам',
                                     reply_markup=bully())
                elif equip_item_category == 'броня':#если значение hp меньше брони то hp = 1
                    hp = hp - old_item[2] + new_item[2]
                    bot.send_message(message.chat.id, text=f'Ты успешно поменял броню\nТвое здоровье равняется {hp}еденицам',
                                     reply_markup=bully())


bot.polling(non_stop=True)