from pico2d import *

class Box:
    def __init__(self,_x,_y):
        self.image = load_image('image\\black.png')
        self.x = _x
        self.y = _y
        self.move = False
    def draw(self):
        self.image.draw(self.x ,self.y)
    def update(self):
        if self.move:
            #self.x
         pass


    def get_bb(self):
        return self.x - 60, self.y - 60, self.x+60, self.y + 60