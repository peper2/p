from pico2d import *
import box
stage01_design =  [[ 1,1,1,1,1,1,1,1,1,1],        #!
         [ 1,0,0,0,0,1,1,1,1,1],        #2
         [ 1,1,1,1,0,1,1,1,1,1],        #3
         [ 1,1,1,1,0,1,1,1,1,1],        #4
         [ 1,0,0,0,0,0,0,0,1,1],        #5
         [ 1,0,1,1,0,0,0,0,1,1],        #6
         [ 1,0,1,1,0,0,0,0,1,1],        #7
         [ 1,0,0,1,1,1,1,1,1,1],        #8
         [ 1,1,0,1,1,1,1,1,1,1],        #9
         [ 1,0,0,0,0,0,0,0,1,1],        #10
         [ 1,0,0,0,1,1,1,0,0,1],        #11
         [ 1,0,0,0,1,1,1,1,0,1],        #12
         [ 1,1,1,1,1,1,1,1,0,1]]

class Stage01:
    def __init__(self):
        self.box_house = []
    def enter(self):
        for i in range(13):
            for j in range(10):
                if stage01_design[i][j] == 1:
                    self.box_house.append(box.Box(40 + (i * 60), 0 + (j * 60)))
    def draw(self):
        for i in self.box_house:
            i.draw()

    def update(self):
        for i in self.box_house:
            i.update()

    def get_box_group(self):
        for o in self.box_house:
            yield o

stage1 = Stage01()
