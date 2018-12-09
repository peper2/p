from pico2d import *
import game_world
import mygame
goal_image = load_image("image\\goal.png")
end_time = False
class Box:
    def __init__(self,_x,_y,_color):
        self.image = load_image('image\\black.png')
        self.unimage = load_image("image\\white.png")

        self.x = _x
        self.y = _y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.velocity = game_world.GRASS_SPEED_PPS
        self.dest = 0
        self.color = _color
    def draw(self):
        if self.color == 0:
            self.unimage.draw(self.x,self.y)
        elif self.color == 1:
            self.image.draw(self.x ,self.y)
        elif self.color == 2:
            self.unimage.draw(self.x, self.y)
            self.goal_draw()
    def reverse_smooth_time(self):
        return self.velocity * game_world.frame_time / 8

    def smooth_time(self):
        if get_time() - mygame.key_pree_time < 0.1:
            return self.velocity * game_world.frame_time / 2
        elif get_time() - mygame.key_pree_time < 0.05:
            return self.velocity * game_world.frame_time / 3
        else: return self.velocity * game_world.frame_time
    def update(self):
        global end_time
        self.smooth_time()
        if self.left:
            if self.dest - self.x < 45:
                self.x += self.reverse_smooth_time()
                end_time = True
            else : self.x += self.smooth_time()

            if self.x > self.dest:
                self.left = False
                self.x = self.dest
                self.exit()
        elif self.right:
            if self.x - self.dest < 45:
                self.x -= self.reverse_smooth_time()
                end_time = True
            else : self.x -= self.smooth_time()
            if self.x < self.dest:
                self.right = False
                self.x = self.dest
                self.exit()
        elif self.up:
            if self.y - self.dest < 45:
                self.y -= self.reverse_smooth_time()
                end_time = True
            else : self.y -= self.smooth_time()
            if self.y < self.dest:
                self.up = False
                self.y = self.dest
                self.exit()

        elif self.down:
            if self.dest - self.y < 45:
                self.y += self.reverse_smooth_time()
                end_time = True
            else :self.y += self.smooth_time()
            if self.y > self.dest:
                self.down = False
                self.y = self.dest
                self.exit()
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
    def goal_draw(self):
        global goal_image,goal_frame
        goal_frame = (goal_frame + 2 * game_world.ACTION_PER_TIME * game_world.frame_time) % 2
        goal_image.clip_draw(int(goal_frame) * 60, 0, 60, 60, self.x, self.y)
    def exit(self):
        global end_time
        self.dest = 0
        end_time = False
goal_frame = 0
