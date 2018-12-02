from pico2d import *
import game_world
class Box:
    def __init__(self,_x,_y):
        self.image = load_image('image\\black.png')
        self.x = _x
        self.y = _y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.velocity = game_world.GRASS_SPEED_PPS
        self.dest = 0
    def draw(self):
        self.image.draw(self.x ,self.y)
    def update(self):
        if self.left:
            self.x += self.velocity * game_world.frame_time
            if self.x > self.dest:
                self.left = False
                self.x = self.dest
                self.dest = 0
        elif self.right:
            self.x -= self.velocity * game_world.frame_time
            if self.x < self.dest:
                self.right = False
                self.x = self.dest
                self.dest = 0
        elif self.up:
            self.y -= self.velocity * game_world.frame_time
            if self.y < self.dest:
                self.up = False
                self.y = self.dest
                self.dest = 0
        elif self.down:
            self.y += self.velocity * game_world.frame_time
            if self.y > self.dest:
                self.down = False
                self.y = self.dest
                self.dest = 0
    def move_dir(self,_dir,_dest):
        if _dir == 0:
            self.left = True

        elif _dir == 1:
            self.right = True
        elif _dir == 2:
            self.up = True
        elif _dir == 3:
            self.down = True
        self.dest = _dest

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x+60, self.y + 60