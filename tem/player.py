from pico2d import *
import game_world

import stage01
import mygame
import effect

fail_image = load_image("image\\fail_pop.png")
class Player:
    def __init__(self):
        self.images  = [load_image("image\\char_s2.png"),load_image("image\\char_s3.png"),load_image("image\\ball.png")]
        self.x =400
        self.y = 300
        self.frame = 0
        self.min = 0
        self.count = 0
        self.moving = False
        self.go_dir = 0      #어디방향에서 왔는지 0 1 2 3
        self.dir = 3.141592 *2
        self.close_dir = [False,False]  #좌우 위아래
        self.step_dir = 0       #아래가0 시계방향으로 증가
        self.cur_dir = 0
        self.effect = effect.Effect()
        self.gokey = False
        self.imagess = [load_image("image\\runing2.png"), load_image("image\\runing3.png")]
    def enter(self,_stage):
        self.stage = _stage
    def draw(self):
        if self.moving== False:
            #self.images[0].clip_draw(int(self.frame) * 60, 0, 60, 60, self.x, self.y)  # 연속된 모션 사진을 출력하기 위한 커팅작업
            if self.cur_dir == 0:
                self.images[0].clip_composite_draw(int(self.frame) * 60, 0, 60, 60, self.dir, '', self.x, self.y,
                                      60, 60)
            else : self.images[1].clip_composite_draw(int(self.frame) * 60, 0, 60, 60, self.dir, '', self.x, self.y,
                                      60, 60)


        elif self.moving:
            self.images[2].draw(self.x,self.y)
            self.effect.draw()

    def update(self):
        if stage01.stage1.delay_stage == False:
            self.frame = (self.frame + 4 * game_world.ACTION_PER_TIME * game_world.frame_time ) % 4
        if self.moving :
            for i in self.stage.box_house:
                if i.left == False and i.right == False and i.up == False and i.down == False:
                    self.effect.start = False

                    for i in self.stage.box_house:
                        if self.x - 60 == i.x and self.y == i.y:
                            self.close_dir[0] = True
                            if i.trap_dir == 0 and self.go_dir == 0 and i.color == 3:
                                self.death()
                            if i.trap_dir == 6 or i.trap_dir == 7 and self.go_dir == 0 :
                                self.death()
                            break
                    for i in self.stage.box_house:
                        if self.x  == i.x and self.y + 60 == i.y:
                            self.close_dir[1] = True
                            if i.trap_dir == 2 and self.go_dir == 2 and i.color == 3:
                                self.death()
                            if i.trap_dir == 7 or i.trap_dir==8 and self.go_dir == 2:
                                self.death()
                            break
                    for i in self.stage.box_house:
                        if self.x + 60 == i.x and self.y == i.y:
                            if i.trap_dir == 1 and self.go_dir == 1 and i.color == 3:
                                self.death()
                            if i.trap_dir == 8 or i.trap_dir == 9 and self.go_dir == 1:
                                self.death()

                            break
                    for i in self.stage.box_house:
                        if self.x  == i.x and self.y-60 == i.y:
                            if i.trap_dir == 3 and self.go_dir == 3 and i.color == 3:
                                self.death()
                            if i.trap_dir == 6 or i.trap_dir == 9 and self.go_dir == 3:
                                self.death()
                            break

                    if self.go_dir == 0:        #왼쪽
                        if self.close_dir[1] == True:
                            self.cur_dir = 1
                        else : self.cur_dir = 0
                        self.dir = -3.141592 /2

                    elif self.go_dir == 1:      #오른쪽
                        if self.close_dir[1] == True:
                            self.cur_dir = 0
                        else:
                            self.cur_dir = 1
                        self.dir = 3.141592 /2

                    elif self.go_dir == 2:      #위
                        if self.close_dir[0] == True:
                            self.cur_dir = 0
                        else : self.cur_dir = 1
                        self.dir = -3.141592

                    elif self.go_dir == 3:      #아래
                        if self.close_dir[0] == True:
                            self.cur_dir = 1
                        else : self.cur_dir = 0
                        self.dir = 3.141592 * 2

                    for i in range(2):
                        self.close_dir[i] = False
                    if self.effect.moving == False:
                        self.moving = False
                        self.exit()
                    break
        self.effect.update(self)
    def exit(self):
        pass
    def death(self):
        global fail_image
        stage01.stage1.fail = True
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
                if stage01.stage1.delay_stage: return
                if event.key == SDLK_LEFT or event.key == SDLK_RIGHT or event.key == SDLK_UP or event.key == SDLK_DOWN:
                    self.gokey = True
                    mygame.key_pree_time = get_time()
                if event.key == SDLK_LEFT:
                    self.min = -50000

                    self.move_update_motion(0)
                    self.move_update_box(0)
                    self.go_dir = 0
                elif event.key == SDLK_RIGHT:
                    self.min = 50000

                    self.move_update_motion(1)
                    self.move_update_box(1)
                    self.go_dir = 1
                elif event.key == SDLK_UP:
                    self.min = 50000

                    self.move_update_motion(2)
                    self.move_update_box(2)
                    self.go_dir = 2
                elif event.key == SDLK_DOWN:
                    self.min = -50000

                    self.move_update_motion(3)
                    self.move_update_box(3)
                    self.go_dir = 3

                self.effect.enter(self.x,self.y)
    def move_update_motion(self,_dir):
        self.moving = True
        if _dir == 0:
            for i in self.stage.box_house:
                if self.y == i.y:
                    if self.x > i.x:
                        if self.min < i.x:
                            self.min = i.x
            self.count = (self.x  - self.min ) / 60
            self.count -= 1
            print(self.count)
           # self.x = self.min + 60
        elif _dir == 1:
            for i in self.stage.box_house:
                if self.y == i.y:
                    if self.x < i.x:
                        if self.min > i.x:
                            self.min = i.x
            self.count = (self.min - self.x) / 60
            self.count -= 1
            print(self.count)
            #self.x = self.min -60
        elif _dir == 2:
            for i in self.stage.box_house:
                if self.x == i.x:
                    if self.y < i.y:
                        if self.min > i.y:
                            self.min = i.y
            #self.y = self.min -60
            self.count = (self.min - self.y) / 60
            self.count -= 1
            print(self.count)
        elif _dir == 3:
            for i in self.stage.box_house:
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
            for i in self.stage.box_house:
                tempX = i.x + ( 60 * self.count)
                i.move_dir(0,tempX)
            for i in self.stage.unbox_house:
                tempX = i.x + (60 * self.count)
                i.move_dir(0, tempX)
        if _dir == 1:
            for i in self.stage.box_house:
                tempX = i.x - (60 * self.count)
                i.move_dir(1, tempX)
            for i in self.stage.unbox_house:
                tempX = i.x - (60 * self.count)
                i.move_dir(1, tempX)
        if _dir == 2:
            for i in self.stage.box_house:
                tempY = i.y - (60 * self.count)
                i.move_dir(2, tempY)
            for i in self.stage.unbox_house:
                tempY = i.y - (60 * self.count)
                i.move_dir(2, tempY)
        if _dir == 3:
            for i in self.stage.box_house:
                tempY = i.y + (60 * self.count)
                i.move_dir(3, tempY)
            for i in self.stage.unbox_house:
                tempY = i.y + (60 * self.count)
                i.move_dir(3, tempY)
        self.count = 0





