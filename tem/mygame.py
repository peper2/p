from pico2d import *
import game_world
import player

bb = []
import stage01
stage1 = None



class Logo:
    def __init__(self):
        self.image = load_image('image\\logo.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 800, 0, 800, 600, 400, 300)

    def update(self):
        self.frame = (self.frame + 1 * game_world.ACTION_PER_TIME * game_world.frame_time *2) % 2
class Menu():
    def __init__(self):
        self.background_image = load_image("image\\main2.png")
        self.start = load_image("image\\button_1_1.png")
        self.start_down = load_image("image\\button_1_2.png")
        self.exit = load_image("image\\button_2_1.png")
        self.exit_down = load_image("image\\button_2_2.png")
        self.option = load_image("image\\button_3_1.png")
        self.option_down= load_image("image\\button_3_2.png")

        self.start_down_state = False
        self.exit_down_state = False
        self.option_down_state = False

        self.option_setting = load_image("image\\op_pop.png")
        self.option_sound_on = load_image("image\\s_on.png")
        self.option_bgm_on = load_image("image\\s_on.png")
        self.option_sound_off = load_image("image\\s_off.png")
        self.option_bgm_off = load_image("image\\s_off.png")
        self.option_setting_state = False
        self.option_sound = True
    def draw(self):
        #self.background_image.draw(int(self.frame) * 800, 0, 800, 600, 400, 300)
        self.background_image.draw(400,300)
        if self.option_setting_state == False:
            if self.start_down_state == False:
                self.start.draw(200,450)
            else: self.start_down.draw(200,450)
            if self.option_down_state == False:
                self.option.draw(200, 300)
            else : self.option_down.draw(200,300)
            if self.exit_down_state == False:
                self.exit.draw(200, 150)
            else : self.exit_down.draw(200,150)
        else :
            self.option_setting.draw(400,300)
            if self.option_sound:
                self.option_sound_on.draw(500,270)
                self.option_bgm_on.draw(500,370)
            else :
                self.option_sound_off.draw(500,270)
                self.option_bgm_off.draw(500,370)
            if self.exit_down_state == False:
                self.exit.draw(400, 75)
            else : self.exit_down.draw(400,75)
    # def update(self):
    #     self.frame = (self.frame + 1 * game_world.ACTION_PER_TIME * game_world.frame_time *2) % 2


logo = Logo()
menu = Menu()
import player
playerchar = None

running = True


current_time = get_time()

key_pree_time = get_time()



bgm = None

def handle_events():
    global menu,menu_loop,bgm
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:


            close_canvas()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT and menu.option_setting_state == False:
            if event.x >=75 and event.x <= 325 and event.y >= 100 and event.y <= 200:
                menu.start_down_state = True
            elif event.x >= 105 and event.x <= 295 and event.y >=250 and event.y <= 350:
                menu.option_down_state = True
            elif event.x >= 105 and  event.x <= 295 and event.y >= 400 and event.y <= 500:
                menu.exit_down_state = True
        elif event.type == SDL_MOUSEBUTTONUP and menu.option_setting_state == False:
            if menu.start_down_state:
                menu.start_down_state = False
                menu_loop = False
            if menu.option_down_state :
                menu.option_down_state = False
                menu.option_setting_state = True
            if menu.exit_down_state :
                close_canvas()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT and menu.option_setting_state:
            if event.x >=305 and event.x <= 495 and event.y >= 475 and event.y <= 575:
                menu.exit_down_state = True
            elif event.x >=500 and event.x <= 590 and event.y >= 190 and event.y <= 265:
                menu.option_sound = False
                bgm.pause()
            elif event.x >=410 and event.x <= 500 and event.y >= 190 and event.y <= 265:
                menu.option_sound = True
                bgm.resume()
        elif event.type == SDL_MOUSEBUTTONUP and menu.option_setting_state and menu.exit_down_state :
            menu.option_setting_state = False
            menu.exit_down_state = False

def update():
    global current_time,playerchar

    game_world.frame_time = (get_time() - current_time)
    current_time += game_world.frame_time

def main_logo():
    global logo,bgm
    bgm = load_music('image\\back.mp3')
    bgm.set_volume(20)
    bgm.repeat_play()
    while True:
        clear_canvas()
        logo.draw()
        logo.update()
        update()
        update_canvas()
        if get_time() > 3:
            del(logo)
            return
menu_loop = True
def main_menu():
    global menu
    while menu_loop:
        clear_canvas()
        menu.draw()
        handle_events()
        update()
        update_canvas()
def main():
    global current_time,playerchar

    main_logo()
    main_menu()
    current_time = get_time()
    playerchar = player.Player()
    stage01.stage1.enter(stage01.stage01_design)
    playerchar.enter(stage01.stage1)
    while running:

        clear_canvas()
        game_world.blank_draw()
        playerchar.update()

        stage01.stage1.update()
        stage01.stage1.draw()

        playerchar.draw()
        if stage01.stage1.delay_stage  and stage01.stage1.fail :
            stage01.stage1.fail_image.draw(400, 300)
        elif stage01.stage1.delay_stage == True:
            stage01.stage1.clear_image.draw(400, 300)
        update()
        playerchar.handle_events()
        update_canvas()


if __name__ == '__main__':
    main()
