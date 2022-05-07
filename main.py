try:
    import random
    import pygame
    import level
    from splashes import splashes
    from pygame.locals import *
    from brawlers import all_brawlers, all_brawlers_list, brawlers_data
    from pygame_widgets.progressbar import ProgressBar
    import pygame_textinput
    import pygame_widgets
    from pygame_widgets.button import Button
    from pygame_widgets.dropdown import Dropdown
except:
    import os
    os.system("pip install pygame pygame_textinput pygame_widgets")
    import random
    import pygame
    import level
    from splashes import splashes
    from pygame.locals import *
    from brawlers import all_brawlers, all_brawlers_list, brawlers_data
    from pygame_widgets.progressbar import ProgressBar
    import pygame_textinput
    import pygame_widgets
    from pygame_widgets.button import Button
    from pygame_widgets.dropdown import Dropdown

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

pygame.init()
data = "Data/level.py"
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 36)
font16 = pygame.font.SysFont('arial', 16)
pygame.display.set_mode((600, 400))
pygame.display.update()
pygame.display.set_caption("BrawlSlaves")
screen = pygame.display.set_mode((600, 400))
not_available = pygame.image.load("Sprites/not_available.jpg")
box = pygame.image.load("Sprites/box.jpg")
bullet = pygame.image.load("Sprites/bullet.png")
gem = pygame.image.load("Sprites/gem.png")
case = pygame.image.load("Sprites/case.png")
bws_imgs = {bw: pygame.image.load(f"Sprites/{bw}.png") for bw in all_brawlers_list}
# for bw in level.brawlers:
#     bws_imgs[bw] =


def save_name(name, enter):
    with open("level.py", "w") as lvl:
        lvl.write(f"isFirstBoot = False \nname = '{name}'\ncups=0\ngems=10\nbrawlers=['Van_Darkholm']")
        lvl.close()
    enter.disable()
    enter.hide()
    policy()


def policy():
    submit = Button(screen, 150, 360, 90, 30, radius=20, text='Согласен', onClick=lambda: show_menu(submit=submit))
    while True:
        clock.tick(120)
        # ___________________________________________#
        screen.fill(LIGHT_BLUE)
        events = pygame.event.get()

        text1 = font.render('Политика конфиденциальности', True, (180, 180, 180))
        screen.blit(text1, (10, 50))
        text2 = font.render('1)Пользователь не может жаловаться.', True, (255, 255, 255))
        text3 = font.render('2)Все данные об использовании', True, (255, 255, 255))
        text4 = font.render('собираются и отправляются в ФСБ.', True, (255, 255, 255))
        screen.blit(text2, (10, 90))
        screen.blit(text3, (10, 130))
        screen.blit(text4, (10, 170))

        # ___________________________________________#
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        pygame_widgets.update(events)
        submit.listen(events)
        submit.draw()

        pygame.display.update()


def gen_opponent(opp_x, opp_y, my_x, my_y, opp_bw, filled_range, my_hp, opp_hp):
    img = bws_imgs[opp_bw]
    img = pygame.transform.scale(img, (50, 50))
    screen.blit(img, (opp_x, opp_y))
    # events = pygame.event.get()
    opp_x_range = [i for i in range(opp_x, opp_x + 50)]
    opp_y_range = [i for i in range(opp_y, opp_y + 50)]
    if opp_y - my_x > 50:
        opp_y -= 1
        if list(set(opp_y_range) & set(filled_range[1])) and list(set(opp_x_range) & set(filled_range[0])):
            opp_y += 1
        if opp_x > 300:
            opp_x -= 1
        else:
            opp_x += 1

    elif my_x - opp_y > 50:
        opp_y += 1
        if list(set(opp_y_range) & set(filled_range[1])) and list(set(opp_x_range) & set(filled_range[0])):
            opp_y -= 10
        if opp_x > 300:
            opp_x -= 1
        else:
            opp_x += 1

    if opp_x - my_y > 50:
        opp_x -= 1
        if list(set(opp_y_range) & set(filled_range[1])) and list(set(opp_x_range) & set(filled_range[0])):
            opp_x += 1
        if opp_y > 200:
            opp_y -= 1
        else:
            opp_y += 1

    elif my_y - opp_x > 50:
        opp_x += 1
        if list(set(opp_y_range) & set(filled_range[1])) and list(set(opp_x_range) & set(filled_range[0])):
            opp_x -= 1
        if opp_y > 200:
            opp_y -= 1
        else:
            opp_y += 1

    # for event in events:
    #     if event.type == pygame.QUIT:
    #         exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         this_opp_x = opp_x
        #         this_opp_y = opp_y
        #         bullet_x = my_x
        #         bullet_y = my_y
    screen.blit(img, (opp_x, opp_y))
    return [opp_x, opp_y, my_hp, opp_hp]


def gen_world():
    filled_x_range = []
    filled_y_range = []
    for i in range(8):
        if i in [3, 4]:
            continue
        screen.blit(box, (115, i*50))
        filled_y_range.extend(iter(range(i*50, i*50 + 50)))
        filled_x_range.extend(iter(range(115, 115 + 50)))
    for i in range(8):
        if i in [3, 4]:
            continue
        screen.blit(box, (445, i*50))
        filled_y_range.extend(iter(range(i*50, i*50 + 50)))
        filled_x_range.extend(iter(range(445, 445 + 50)))

    for i in range(8):
        if i in [3, 4]:
            continue
        screen.blit(box, (275, i*50))
        filled_y_range.extend(iter(range(i*50, i*50 + 50)))
        filled_x_range.extend(iter(range(275, 275 + 50)))
    return [filled_x_range, filled_y_range]


def run_fight(selected_bw): # sourcery no-metrics skip: low-code-quality
    counter = 0
    my_x = 70
    my_y = 10
    opp_x = 540
    opp_y = 70
    sp = random.choice(splashes)
    my_hp = brawlers_data[selected_bw]['hp']
    opponent = random.choice(all_brawlers_list)
    opp_hp = brawlers_data[opponent]['hp']
    load = ProgressBar(screen, 150, 345, 200, 40, lambda: counter / 100, curved=True, completedColour=(255, 220, 0))
    while True:
        clock.tick(120)
        counter += 1
        # ___________________________________________#
        screen.fill((112, 180, 60))
        events = pygame.event.get()

        text1 = font.render('Загрузка...', True, (255, 255, 255))
        screen.blit(text1, (225, 50))
        text1 = font16.render(f'{sp}', True, (255, 255, 255))
        screen.blit(text1, (130, 300))
        if counter > 100:
            flag = False
            pressed_key = ""
            while True:
                my_x_range = [i for i in range(my_x, my_x+50)]
                my_y_range = [i for i in range(my_y, my_y + 50)]
                screen.fill((176, 191, 26))
                events = pygame.event.get()
                clock.tick(120)
                load.hide()
                text1 = font16.render('Моя команда', True, (255, 255, 255))
                screen.blit(text1, (20, 10))
                text1 = font16.render('Противники', True, (255, 255, 255))
                screen.blit(text1, (505, 10))
                img = bws_imgs[selected_bw]
                img = pygame.transform.scale(img, (50, 50))
                screen.blit(img, (my_y, my_x))
                filled_range = gen_world()
                opp_pos = gen_opponent(opp_x, opp_y, my_x, my_y, opponent, filled_range, my_hp, opp_hp)
                opp_x, opp_y, my_hp, opp_hp = opp_pos[0], opp_pos[1], opp_pos[2], opp_pos[3]
                for event in events:
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        flag = True
                        if event.key == pygame.K_LEFT:
                            pressed_key = "L"
                            my_y -= 1
                            if list(set(my_x_range) & set(filled_range[1])) and list(set(my_y_range) & set(filled_range[0])):
                                my_y += 10
                        if event.key == pygame.K_RIGHT:
                            pressed_key = "R"
                            my_y += 1
                            if list(set(my_x_range) & set(filled_range[1])) and list(set(my_y_range) & set(filled_range[0])):
                                my_y -= 10
                        if event.key == pygame.K_UP:
                            pressed_key = "U"
                            my_x -= 1
                            if list(set(my_x_range) & set(filled_range[1])) and list(set(my_y_range) & set(filled_range[0])):
                                my_x += 10
                        if event.key == pygame.K_DOWN:
                            pressed_key = "D"
                            my_x += 1
                            if list(set(my_x_range) & set(filled_range[1])) and list(set(my_y_range) & set(filled_range[0])):
                                my_x -= 10
                    elif event.type == pygame.KEYUP:
                        pressed_key = ""
                        flag = False
                if flag:
                    if pressed_key == "L":
                        my_y -= 1
                        if list(set(my_x_range) & set(filled_range[1])) and list(set(my_y_range) & set(filled_range[0])):
                            my_y += 10
                    elif pressed_key == "R":
                        my_y += 1
                        if list(set(my_x_range) & set(filled_range[1])) and list(set(my_y_range) & set(filled_range[0])):
                            my_y -= 10
                    elif pressed_key == "U":
                        my_x -= 1
                        if list(set(my_x_range) & set(filled_range[1])) and list(set(my_y_range) & set(filled_range[0])):
                            my_x += 10
                    elif pressed_key == "D":
                        my_x += 1
                        if list(set(my_x_range) & set(filled_range[1])) and list(set(my_y_range) & set(filled_range[0])):
                            my_x -= 10
                if my_x <= 0:
                    my_x += 5
                elif my_x >= 350:
                    my_x -= 5
                elif my_y <= 0:
                    my_y += 5
                elif my_y >= 550:
                    my_y -= 5

                pygame_widgets.update(events)
                pygame.display.update()

        # ___________________________________________#
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        pygame_widgets.update(events)
        pygame.display.update()


def load_game(game_type, play, brawl, way, shop_btt, gt_dpd, sbw):
    gt_dpd.hide()
    play.hide()
    brawl.hide()
    way.hide()
    shop_btt.hide()
    if game_type == "fight":
        run_fight(sbw)


def fist_boot():
    name_input = pygame_textinput.TextInputVisualizer()
    enter = Button(screen, 150, 100, 50, 30, text='Да', radius=20, onClick=lambda: save_name(name_input.value, enter))
    while True:
        clock.tick(120)
        # ___________________________________________#
        screen.fill(LIGHT_BLUE)
        events = pygame.event.get()

        # Feed it with events every frame
        name_input.update(events)
        # Blit its surface onto the screen
        screen.blit(name_input.surface, (10, 100))
        text1 = font.render('Придумайте ник', True, (180, 180, 180))
        screen.blit(text1, (10, 50))
        text2 = font.render('Вы сможете изменить его позже', True, (180, 180, 180))
        screen.blit(text2, (10, 200))

        # ___________________________________________#
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        pygame_widgets.update(events)
        enter.listen(events)
        enter.draw()

        pygame.display.update()


def show_brawlers(play, brawl, way, shop_btt, gt_dpd):
    gt_dpd.hide()
    play.hide()
    brawl.hide()
    way.hide()
    shop_btt.hide()
    i = 0
    select_btt = Button(screen, 5, 355, 80, 30, hoverColour=(55, 255, 100), colour=(5, 255, 55), radius=5,
                     text='Выбрать', onClick=lambda: show_menu(sel_b=all_brawlers_list[i], sel_btt=select_btt))
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    select_btt.hide()
                    show_menu()
                if event.key == pygame.K_LEFT and i >= 1:
                    i -= 1
                if event.key == pygame.K_RIGHT and i <= 3:
                    i += 1
        clock.tick(120)

        # ______________________________#
        screen.fill(GREEN)
        text1 = font.render('Все бойцы', True, (250, 250, 250))
        screen.blit(text1, (220, 10))
        text2 = font.render(f'{brawlers_data[all_brawlers_list[i]]["name"]}', True, (250, 50, 50))
        screen.blit(text2, (200, 50))
        text2 = font.render(f'{all_brawlers[all_brawlers_list[i]].replace("_", " ")}', True, (250, 250, 250))
        screen.blit(text2, (200, 300))
        text2 = font16.render(f'Здоровье: {brawlers_data[all_brawlers_list[i]]["hp"]}', True, (250, 250, 250))
        screen.blit(text2, (10, 100))
        text2 = font16.render(f'Урон: {brawlers_data[all_brawlers_list[i]]["dmg"]}', True, (250, 250, 250))
        screen.blit(text2, (10, 120))
        text2 = font16.render(f'С супером: {brawlers_data[all_brawlers_list[i]]["Sdmg"]}', True, (250, 250, 250))
        screen.blit(text2, (10, 140))
        if all_brawlers_list[i] not in level.brawlers:
            screen.blit(not_available, (5, 300))
            select_btt.hide()
        else:
            select_btt.show()
        screen.blit(bws_imgs[all_brawlers_list[i]], (200, 100))
        # ______________________________#

        pygame_widgets.update(events)
        pygame.display.update()


def open_case(btt):   # sourcery no-metrics skip: merge-duplicate-blocks
    btt.hide()
    btt.disable()
    if level.gems < 10:
        show_menu()
    while True:
        level.gems -= 10
        events = pygame.event.get()
        clock.tick(120)

        # ______________________________#
        screen.fill(LIGHT_BLUE)
        rnd = random.randint(0, 100)
        if rnd in [5, 14, 23, 35, 48, 56, 67, 72, 89, 97]:
            new_bw = random.choice(all_brawlers_list)
            while True:
                if new_bw in level.brawlers:
                    new_bw = random.choice(all_brawlers_list)
                elif level.brawlers == all_brawlers_list:
                    break
                else:
                    break
            level.brawlers.append(new_bw)
            while True:
                events = pygame.event.get()
                clock.tick(120)
                screen.fill(BLUE)
                screen.blit(bws_imgs[new_bw], (200, 100))
                text1 = font.render('НОВЫЙ БОЕЦ!!!!', True, (180, 180, 180))
                screen.blit(text1, (75, 20))
                text2 = font.render(f'{brawlers_data[new_bw]["name"]}', True, (250, 50, 50))
                screen.blit(text2, (200, 60))
                text2 = font.render('Нажми пробел для продолжения', True, (180, 180, 180))
                screen.blit(text2, (50, 350))
                for event in events:
                    if event.type == QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            with open("level.py", "w") as lvl:
                                lvl.write(
                                    f"isFirstBoot = False \nname = '{level.name}'\ncups={level.cups}\ngems={level.gems}\nbrawlers={level.brawlers}")
                                lvl.close()
                            show_menu()
                pygame.display.update()

        level.gems += random.randint(0, 9)
        with open("level.py", "w") as lvl:
            lvl.write(f"isFirstBoot = False \nname = '{level.name}'\ncups={level.cups}\ngems={level.gems}\nbrawlers={level.brawlers}")
            lvl.close()
        show_menu()
        # ______________________________#

        pygame_widgets.update(events)
        for event in events:
            if event.type == QUIT:
                exit()
        pygame.display.update()


def show_shop(play_btt, brawlers_btt, way, shop_btt, gt_dpd):
    gt_dpd.hide()
    play_btt.hide()
    brawlers_btt.hide()
    way.hide()
    shop_btt.hide()
    buy_btt = Button(screen, 215, 225, 80, 30, hoverColour=(55, 255, 100), colour=(5, 255, 55), radius=5,
                     text='Купить (10)', onClick=lambda: open_case(buy_btt))
    while True:
        events = pygame.event.get()
        clock.tick(120)

        # ______________________________#
        screen.fill(LIGHT_BLUE)
        screen.blit(case, (200, 100))

        screen.blit(gem, (400, 10))
        text3 = font.render(f'{level.gems}', True, (250, 250, 250))
        screen.blit(text3, (450, 10))
        # ______________________________#

        pygame_widgets.update(events)
        for event in events:
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    buy_btt.hide()
                    buy_btt._hidden = True
                    buy_btt.disable()
                    init_game()
        pygame.display.update()


def show_menu(submit=None, sel_b=None, sel_btt=None):
    nick = level.name
    cups = level.cups
    if sel_b is None:
        sel_b = random.choice(level.brawlers)
    else:
        seleced_brawler = sel_b
    scal = 10
    while scal < cups:
        scal *= 10
    if submit is not None:
        submit.disable()
        submit.hide()
    if sel_btt is not None:
        sel_btt.disable()
        sel_btt.hide()
    gt_dpd = Dropdown(
        screen, 475, 275, 100, 50, name='Режим игры',
        choices=[
            'Бой 1 на 1',
            'Бой 3 на 3',
            'Тренировка',
        ],
        borderRadius=3, colour=pygame.Color('orange'), values=["fight", "fight3x3", 'tren'], direction='up', textHAlign='left'
    )
    way = ProgressBar(screen, 50, 345, 200, 40, lambda: cups/scal, curved=True)
    play_btt = Button(screen, 475, 350, 100, 50, hoverColour=(255, 55, 100), colour=(255, 5, 55), radius=5, text='Играть!', onClick=lambda: load_game(gt_dpd.getSelected(), play_btt, brawlers_btt, way, shop_btt, gt_dpd, sel_b))
    brawlers_btt = Button(screen, 50, 150, 80, 30, hoverColour=(255, 55, 100), colour=(255, 5, 55), radius=5,
                      text='Бойцы', onClick=lambda: show_brawlers(play_btt, brawlers_btt, way, shop_btt, gt_dpd))
    shop_btt = Button(screen, 50, 110, 80, 30, hoverColour=(55, 255, 100), colour=(5, 255, 55), radius=5,
                          text='Магаз', onClick=lambda: show_shop(play_btt, brawlers_btt, way, shop_btt, gt_dpd))
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        clock.tick(120)

        # ______________________________#
        screen.fill(LIGHT_BLUE)
        text1 = font.render(f'{cups}/{scal}', True, (180, 180, 180))
        screen.blit(text1, (75, 300))
        text2 = font.render(f'{brawlers_data[sel_b]["name"]}', True, (250, 250, 250))
        screen.blit(text2, (200, 50))
        screen.blit(bws_imgs[sel_b], (200, 100))
        screen.blit(gem, (400, 10))
        text3 = font.render(f'{level.gems}', True, (250, 250, 250))
        screen.blit(text3, (450, 10))
        # ______________________________#

        if scal < cups:
            scal *= 10
        pygame_widgets.update(events)
        play_btt.listen(events)
        play_btt.draw()
        pygame.display.update()


def init_game():
    version = pygame.version.ver
    if level.isFirstBoot:
        fist_boot()
    else:
        show_menu(submit=None)


if __name__ == '__main__':
    init_game()
