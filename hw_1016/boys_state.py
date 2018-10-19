from pico2d import *
import game_framework
import random
from enum import Enum
class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)

class Boy_Image:
    def __init__(self):
        self.image = load_image('../res/animation_sheet.png')
        self.wp = load_image('../res/wp.png')

class Boy:
    #class State(Enum):
    #    s1=1
    #    s2=2
    #    s3=3
    #    s4=4
    def __init__(self):
        print("Creating..")
        # self.state = self.State.s1
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(1.0, 3.0)
        self.frame = random.randint(0, 7)
        self.waypoints = []
        self.name = ''
        # self.image = load_image('../res/animation_sheet.png')
        #self.wp = load_image('../res/wp.png')
        self.state = 0
        self.rot = 0
        self.stop = False
    def draw(self, boy_image):
        for wp in self.waypoints:
            boy_image.wp.draw(wp[0], wp[1])
        if self.state == 2:
            self.rot = 100
        elif self.state == 3:
            self.rot = 0
        elif self.state== 0:
            self.rot = 200
        elif self.state==1:
            self.rot = 300
        boy_image.image.clip_draw(self.frame * 100, self.rot, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        if len(self.waypoints) > 0:
            self.stop = True
            tx, ty = self.waypoints[0]
            dx, dy = tx - self.x, ty - self.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dx > 0:
                self.state = 2
            elif dx < 0:
                self.state = 3
            if dist > 0:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist

                if dx < 0 and self.x < tx: self.x = tx
                if dx > 0 and self.x > tx: self.x = tx
                if dy < 0 and self.y < ty: self.y = ty
                if dy > 0 and self.y > ty: self.y = ty

                if (tx, ty) == (self.x, self.y):
                    del self.waypoints[0]
        else:
            if self.stop == True:
                self.stop = False
                if self.state == 2:
                    self.state = 1
                elif self.state == 3:
                    self.state = 0
                else : self.state = 1


span = 50
def handle_events():
    global boys
    global span
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif e.key in range(SDLK_1, SDLK_9 + 1):
                span = 20 * (e.key - SDLK_0)

        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                tx, ty = e.x, 600 - e.y
                for b in boys:
                    bx = tx + random.randint(-span, span)
                    by = ty + random.randint(-span, span)
                    b.waypoints += [ (bx, by) ]
            else:
                for b in boys:
                    b.waypoints = []
import json
def create_team():
    global boy_data
    boy_data_file = open('boys_data.json','r')
    boy_data = json.load(boy_data_file)
    boy_data_file.close()

def enter():
    create_team()
    global grass , boys_image,boys
    global boy_data
    boys = []

    temp = boy_data['boys']
    for i in temp:
        boy = Boy()
        boy.name = i['name']
        boy.x = i['x']
        boy.y = i['y']
        boy.speed = i['speed']
        boys.append(boy)
    grass = Grass()
    boys_image = Boy_Image()


# def main():
#     global running
#     enter()
#     while running:
#         handle_events()
#         print(running)
#         update()
#         draw()
#     exit()

def draw():
    global grass, boys,boys_image
    clear_canvas()
    grass.draw()
    for b in boys:
        b.draw(boys_image)
    update_canvas()

def update():
    global boys
    for b in boys:
        b.update()
    delay(0.01)

# fill here

def exit():
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
