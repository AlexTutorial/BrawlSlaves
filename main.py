try:
    import random
    import pygame
    import level
    from splashes import splashes
    from pygame.locals import *
    from brawlers import all_brawlers, all_brawlers_list
    from pygame_widgets.progressbar import ProgressBar
    import pygame_textinput
    import pygame_widgets
    from pygame_widgets.button import Button
except:
    import os
    os.system("pip install pygame pygame_textinput pygame_widgets")
    import random
    import pygame
    import level
    from splashes import splashes
    from pygame.locals import *
    from brawlers import all_brawlers, all_brawlers_list
    from pygame_widgets.progressbar import ProgressBar
    import pygame_textinput
    import pygame_widgets
    from pygame_widgets.button import Button

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
pygame.display.set_mode((600, 400))
pygame.display.update()
screen = pygame.display.set_mode((600, 400))
not_available = pygame.image.load("Sprites/not_available.jpg")
gem = pygame.image.load("Sprites/gem.jpg")
case = pygame.image.load("Sprites/case.jpg")
bws_imgs = {bw: pygame.image.load(f"Sprites/{bw}.jpg") for bw in all_brawlers_list}
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


def load_game(game_type):
    pass


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


def show_brawlers(play, brawl, way, shop_btt):
    play.hide()
    brawl.hide()
    way.hide()
    shop_btt.hide()
    i = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_menu()
                if event.key == pygame.K_LEFT and i >= 1:
                    i -= 1
                if event.key == pygame.K_RIGHT and i <= 1:
                    i += 1
        clock.tick(120)

        # ______________________________#
        screen.fill(GREEN)
        text1 = font.render('Все бойцы', True, (250, 250, 250))
        screen.blit(text1, (220, 10))
        text2 = font.render(f'{all_brawlers_list[i].replace("_", " ")}', True, (250, 50, 50))
        screen.blit(text2, (200, 50))
        text2 = font.render(f'{all_brawlers[all_brawlers_list[i]].replace("_", " ")}', True, (250, 250, 250))
        screen.blit(text2, (200, 300))
        if all_brawlers_list[i] not in level.brawlers:
            screen.blit(not_available, (50, 300))
        screen.blit(bws_imgs[all_brawlers_list[i]], (200, 100))
        # ______________________________#

        pygame_widgets.update(events)
        pygame.display.update()


def open_case(btt):
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
                else:
                    break
            level.brawlers.append(new_bw)
            while True:
                events = pygame.event.get()
                clock.tick(120)
                screen.fill(BLUE)
                screen.blit(bws_imgs[new_bw], (200, 100))
                text1 = font.render('НОВЫЙ БОЕЦ!!!!', True, (180, 180, 180))
                screen.blit(text1, (75, 50))
                text2 = font.render(f'{new_bw}', True, (250, 50, 50))
                screen.blit(text2, (400, 50))
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


def show_shop(play_btt, brawlers_btt, way, shop_btt):
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


def show_menu(submit=None):
    nick = level.name
    cups = level.cups
    selected_brawler = random.choice(level.brawlers)
    scal = 10
    while scal < cups:
        scal *= 10
    if submit is not None:
        submit.disable()
        submit.hide()
    game_type = "fight"
    way = ProgressBar(screen, 50, 345, 200, 40, lambda: cups/scal, curved=True)
    play_btt = Button(screen, 500, 350, 80, 30, hoverColour=(255, 55, 100), colour=(255, 5, 55), radius=5, text='Играть!', onClick=lambda: load_game(game_type))
    brawlers_btt = Button(screen, 50, 150, 80, 30, hoverColour=(255, 55, 100), colour=(255, 5, 55), radius=5,
                      text='Бойцы', onClick=lambda: show_brawlers(play_btt, brawlers_btt, way, shop_btt))
    shop_btt = Button(screen, 50, 110, 80, 30, hoverColour=(55, 255, 100), colour=(5, 255, 55), radius=5,
                          text='Магаз', onClick=lambda: show_shop(play_btt, brawlers_btt, way, shop_btt))
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
        text2 = font.render(f'{selected_brawler.replace("_", " ")}', True, (250, 250, 250))
        screen.blit(text2, (200, 50))
        screen.blit(bws_imgs[selected_brawler], (200, 100))
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
