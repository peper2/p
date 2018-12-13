from pico2d import *
import box
import game_world
import mygame
from stage_design import *
class Stage:
    def __init__(self):
        self.box_house = []
        self.unbox_house = []
        self.reverseY = 30
        self.now_stage = 1
        self.goal_box = None
        self.clear_image = load_image("image\\clear_pop.png")
        self.fail_image= load_image("image\\fail_pop.png")
        self.delay_stage = False
        self.next_stage_start = get_time()
        self.stage_default_x = 40
        self.stage_default_y = 0
        self.fail = False
    def enter(self,stage_design):

        for i in range(len(stage_design)):
            self.reverseY -=1
            for j in range(len(stage_design[0])):
                if stage_design[i][j] == 6:
                    temp = box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 6)
                    temp.trap_dir = 6
                    self.box_house.append(temp)
                elif stage_design[i][j] == 7:
                    temp = box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 7)
                    temp.dir = -3.141592/2
                    temp.trap_dir = 7
                    self.box_house.append(temp)
                elif stage_design[i][j] == 8:
                    temp = box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 8)
                    temp.dir = -3.141592
                    temp.trap_dir = 8
                    self.box_house.append(temp)
                    continue
                elif stage_design[i][j] == 9:
                    temp = box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 9)
                    temp.dir = 3.141592/2
                    temp.trap_dir = 9
                    self.box_house.append(temp)
                    continue
                elif stage_design[i][j] == 3:
                    if j>0:
                        if stage_design[i][j-1] == 0:
                            temp = box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60),3)
                            temp.dir = 3.141592
                            temp.trap_dir = 1
                            self.box_house.append(temp)
                            continue
                    if i> 0:
                        if stage_design[i-1][j] == 0:
                            temp = box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 3)
                            temp.dir = 3.141592/2
                            temp.trap_dir = 3
                            self.box_house.append(temp)
                            continue
                    if i < len(stage_design):
                        if stage_design[i + 1][j] == 0:
                            temp = box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60),   3)
                            temp.dir = -3.141592/2
                            temp.trap_dir = 2
                            self.box_house.append(temp)
                            continue
                    self.box_house.append( box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 3))
                elif stage_design[i][j] == 1:
                    self.box_house.append(box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 1))      #검정
                else :
                    if stage_design[i][j]== 5:
                        temp = box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 5)

                        self.unbox_house.append(temp)
                        continue
                    if stage_design[i][j] == 2:
                        temp = box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 2)
                        self.unbox_house.append(temp)
                        self.goal_box = temp
                        continue
                    self.unbox_house.append(box.Box(self.stage_default_x + (j * 60), self.stage_default_y + (self.reverseY * 60), 0))  # 흰색
    def next_stage(self):

        if self.now_stage == 1:
            self.stage_default_x = -140
            self.stage_default_y = 240
            self.now_stage = 2
            self.reverseY = 30
            self.enter(stage02_design)
        elif self.now_stage == 2:
            self.stage_default_x = 340
            self.stage_default_y = -420
            self.now_stage = 3
            self.reverseY = 17
            self.enter(stage03_design)
        elif self.now_stage == 3:
            self.stage_default_x = -140
            self.stage_default_y = -720
            self.now_stage = 4
            self.reverseY = 22
            mygame.playerchar.dir = 3.141592 *2
            self.enter(stage04_design)
        elif self.now_stage == 4:
            self.stage_default_x = 340
            self.stage_default_y = 240
            self.now_stage = 5
            self.reverseY = 45
            self.enter(stage05_design)
        elif self.now_stage == 5:
            self.stage_default_x = 40
            self.stage_default_y = 1740
            self.now_stage = 6
            self.reverseY = 22
            mygame.playerchar.dir = 3.141592 * 2
            self.enter(stage06_design)
        elif self.now_stage == 6:
            self.stage_default_x = 40
            self.stage_default_y = 1740
            self.now_stage = 7
            self.reverseY = 22
            mygame.playerchar.dir = 3.141592 * 2
            self.enter(stage06_design)
        elif self.now_stage == 7:
            self.stage_default_x = 40
            self.stage_default_y = 1740
            self.now_stage = 8
            self.reverseY = 22
            mygame.playerchar.dir = 3.141592 * 2
            self.enter(stage06_design)

    def draw(self):
        for i in self.box_house:
            i.draw()
        for i in self.unbox_house:
            i.draw()
    def update(self):
        for i in self.box_house:
            i.update()
        for i in self.unbox_house:
            i.update()
        self.fail_message()
        if mygame.playerchar.x == self.goal_box.x and mygame.playerchar.y ==self.goal_box.y:
            if self.delay_stage== False:
                self.next_stage_start = get_time()
                self.delay_stage = True
            if get_time() - self.next_stage_start > 1:
                self.delay_stage = False
                self.box_house.clear()
                self.unbox_house.clear()
                self.next_stage()
                mygame.playerchar.dir = 3.141592 * 2
                mygame.now_stage +=1
    def fail_message(self):
        if self.fail == True:
            if self.delay_stage == False:
                self.next_stage_start = get_time()
                self.delay_stage = True
            if get_time() - self.next_stage_start > 1:
                self.delay_stage = False
                self.box_house.clear()
                self.unbox_house.clear()
                self.now_stage -= 1
                self.next_stage()
                self.fail = False
                mygame.playerchar.dir = 3.141592 * 2
stage1 = Stage()