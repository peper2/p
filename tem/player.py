from pico2d import *
import game_world

import stage01
import char_move
class Player:
    def __init__(self):
        self.images  = [load_image("image\\char_s2.png")]
        self.x =400
        self.y = 300
        self.frame = 0
        self.velocity = game_world.GRASS_SPEED_PPS
        self.min = 0
        self.count = 0
        self.moving = False
    def draw(self):
        self.images[0].clip_draw(int(self.frame) * 60, 0, 60, 57, self.x, self.y)  # 연속된 모션 사진을 출력하기 위한 커팅작업
    def update(self):
        self.frame = (self.frame + 3 * game_world.ACTION_PER_TIME * game_world.frame_time ) % 3
        if self.moving :
            for i in stage01.stage1.box_house:
                if i.left == False and i.right == False and i.up == False and i.down == False:
                    self.moving = False
                    return
    def exit(self):
        pass

    def move_dir(self,_dir):
        self.move_update_motion()
           # self.x -= self.velocity * game_world.frame_time

    def handle_events(self):
        global running

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
                close_canvas()
            elif event.type == SDL_KEYDOWN:
                if self.moving: return
                if event.key == SDLK_RIGHT:
                    self.min = 50000

                    self.move_update_motion(1)
                    self.move_update_box(1)
                elif event.key == SDLK_LEFT:
                    self.min = -50000

                    self.move_update_motion(0)
                    self.move_update_box(0)
                elif event.key == SDLK_UP:
                    self.min = 50000

                    self.move_update_motion(2)
                    self.move_update_box(2)
                elif event.key == SDLK_DOWN:
                    self.min = -50000

                    self.move_update_motion(3)
                    self.move_update_box(3)
    def move_update_motion(self,_dir):
        self.moving = True
        if _dir == 0:
            for i in stage01.stage1.box_house:
                if self.y == i.y:
                    if self.x > i.x:
                        if self.min < i.x:
                            self.min = i.x
            self.count = (self.x  - self.min ) / 60
            self.count -= 1
            print(self.count)
           # self.x = self.min + 60
        elif _dir == 1:
            for i in stage01.stage1.box_house:
                if self.y == i.y:
                    if self.x < i.x:
                        if self.min > i.x:
                            self.min = i.x
            self.count = (self.min - self.x) / 60
            self.count -= 1
            print(self.count)
            #self.x = self.min -60
        elif _dir == 2:
            for i in stage01.stage1.box_house:
                if self.x == i.x:
                    if self.y < i.y:
                        if self.min > i.y:
                            self.min = i.y
            #self.y = self.min -60
            self.count = (self.min - self.y) / 60
            self.count -= 1
            print(self.count)
        elif _dir == 3:
            for i in stage01.stage1.box_house:
                if self.x == i.x:
                    if self.y > i.y:
                        if self.min < i.y:
                            self.min = i.y
            #self.y = self.min + 60
            self.count = (self.y - self.min) / 60
            self.count -= 1
            print(self.count)
    def move_update_box(self,_dir):

        if _dir == 0:
            for i in stage01.stage1.box_house:
                tempX = i.x + ( 60 * self.count)
                i.move_dir(0,tempX)
        if _dir == 1:
            for i in stage01.stage1.box_house:
                tempX = i.x - (60 * self.count)
                i.move_dir(1, tempX)
        if _dir == 2:
            for i in stage01.stage1.box_house:
                tempY = i.y - (60 * self.count)
                i.move_dir(2, tempY)
        if _dir == 3:
            for i in stage01.stage1.box_house:
                tempY = i.y + (60 * self.count)
                i.move_dir(3, tempY)
        self.count = 0




