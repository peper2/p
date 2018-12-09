from pico2d import *
import box
import game_world
stage01_design =  \
        [[ 1,1,1,1,1,1,1,1,1,1,1,1,1],        #!            #동서남북 모든끝은 1권장
         [ 1,0,0,0,0,0,0,0,0,0,0,0,2],        #2
         [ 1,0,0,0,0,0,0,0,0,0,0,0,1],        #3
         [ 1,0,0,0,0,0,0,0,0,0,0,0,1],        #4
         [ 1,0,0,0,0,0,0,0,0,0,0,0,1],        #5
         [ 1,0,0,0,0,0,0,0,0,0,0,0,1],        #6
         [ 1,0,0,0,0,0,0,0,0,0,0,0,1],        #7
         [ 1,0,0,0,1,1,0,0,1,0,1,1,1],        #8
         [ 1,1,0,0,0,0,0,0,1,0,1,1,1],        #9
         [ 1,0,0,0,0,0,0,0,1,0,1,1,1],        #10
         [ 1,0,0,0,0,0,0,0,0,0,1,1,1],        #11
         [ 1,0,0,0,0,0,0,0,0,1,1,1,1],        #12
         [ 1,1,1,1,1,1,1,1,1,1,1,1,1]]
            #뒤집기상관없이 이상태로 맵상태변경가능
class Stage:
    def __init__(self):
        self.box_house = []
        self.unbox_house = []
        self.reverseY = 13
    def enter(self,stage_design):
        for i in range(len(stage_design)):
            self.reverseY -=1
            for j in range(len(stage_design)):
                if stage_design[i][j] == 1:
                    self.box_house.append(box.Box(40 + (j * 60), 0 + (self.reverseY * 60), 1))      #검정
                else :
                    if stage_design[i][j] == 2:
                        temp = box.Box(40 + (j * 60), 0 + (self.reverseY * 60), 0)
                        temp.color = 2
                        self.unbox_house.append(temp)
                        continue
                    self.unbox_house.append(box.Box(40 + (j * 60), 0 + (self.reverseY * 60), 0))  # 흰색


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


stage1 = Stage()
stage2 = Stage()
stage02_design =  \
        [[ 1,1,1,1,1,1,1,1,1,1,1,1,1],        #!            #동서남북 모든끝은 1권장
         [ 1,0,1,0,0,0,0,0,0,0,0,0,2],        #2
         [ 1,0,1,0,0,0,0,0,0,0,0,0,1],        #3
         [ 1,0,1,0,0,0,0,0,0,0,0,0,1],        #4
         [ 1,0,1,0,0,0,0,0,0,0,0,0,1],        #5
         [ 1,0,1,0,0,0,0,0,0,0,0,0,1],        #6
         [ 1,0,1,0,0,0,0,0,0,0,0,0,1],        #7
         [ 1,0,1,0,1,1,0,0,1,0,1,1,1],        #8
         [ 1,1,0,0,0,0,0,0,1,0,1,1,1],        #9
         [ 1,0,0,0,0,0,0,0,1,0,1,1,1],        #10
         [ 1,0,0,0,0,0,0,0,0,0,1,1,1],        #11
         [ 1,0,0,0,0,0,0,0,0,1,1,1,1],        #12
         [ 1,1,1,1,1,1,1,1,1,1,1,1,1]]
            #뒤집기상관없이 이상태로 맵상태변경가능