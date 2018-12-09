from pico2d import *
import game_world

bb = []
import stage01
stage1 = None


class BackG:
    def __init__(self):
        self.image = load_image('image\\white.png')
        #self.frame = 0
        self.bgm = load_music('image\\back.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(400,300)




class Logo:
    def __init__(self):
        self.image = load_image('image\\logo.png')
        #print(self.image)
        self.frame = 0
        self.timer = 20
        self.onoff = True

    def draw(self):
        if self.onoff == True:
            self.image.clip_draw(self.frame * 800, 0, 800, 600, 400, 300)

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.timer -= 1
        if self.timer < 0:
            self.onoff = False


back = BackG()



logo = Logo()

import player
playerchar = None

running = True


current_time = get_time()

key_pree_time = get_time()

def update():
    global current_time,stage1,playerchar

    game_world.frame_time = (get_time() - current_time)
    current_time += game_world.frame_time


def main():
    global current_time,playerchar
    current_time = get_time()
    playerchar = player.Player()
    stage01.stage1.enter(stage01.stage01_design)
    while running:

        clear_canvas()
        game_world.blank_draw()
        playerchar.update()
        stage01.stage1.update()
        stage01.stage1.draw()
        playerchar.draw()
        update()
        playerchar.handle_events()
        update_canvas()


if __name__ == '__main__':
    main()
