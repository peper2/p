from pico2d import *
import random

cnt = 0


class Grass:
    def __init__(self):
        self.image = load_image('E:\\과제\\게임공학\\2018-2\\2D게임프로그래밍\\grass.png')
        print(self.image)

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        global cnt
        print("Creating..")
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(1.0, 3.0)
        self.frame = random.randint(0, 7)
        self.image = load_image('E:\\과제\\게임공학\\2018-2\\2D게임프로그래밍\\run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8



waypoints = []
KPU_WIDTH, KPU_HEIGHT = 800, 600
dx, dy = 0,0
def handle_events():
    global running
    global px, py
    global dx, dy
    global dest
    global waypoints
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
       # elif e.type == SDL_MOUSEMOTION:
        #    px, py = e.x, KPU_HEIGHT - 1 - e.y
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == 1:
                px, py = e.x, KPU_HEIGHT - 1 - e.y
                waypoints += [(px, py)]
            else:
                waypoints = []
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH,KPU_HEIGHT)
wp = load_image('E:\\과제\\게임공학\\2018-2\\2D게임프로그래밍\\wp.png')
g = Grass()
b = Boy()
b2 = Boy()
# b2.y = 200
waypoints = []
boys = [Boy() for i in range(20)]
# boys = []
# for i in range(20):
#    boys += [ Boy() ]


# for b in boys:
#   b.y = random.randint(90, 550)

running = True
px,py =400,300


while running:
    handle_events()


    if len(waypoints) > 0:
        (px, py) = waypoints[0]
        for b in boys:
            dx, dy = px - b.x, py - b.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist > 0:
                b.x += b.speed * dx / dist
                b.y += b.speed * dy / dist

                if dx < 0 and b.x < px: b.x = px
                if dx > 0 and b.x > px: b.x = px
                if dy < 0 and b.y < py: b.y = py
                if dy > 0 and b.y > py: b.y = py

            if (b.x, b.y) == (px, py):
                cnt += 1
    for b in boys:
        b.update()
    # b.update()
    # b2.update()
    if cnt == 20:
        cnt = 0
        del waypoints[0]
    cnt = 0
    clear_canvas()
    g.draw()
    for b in boys:
        b.draw()
    for loc in waypoints:
        wp.draw(loc[0], loc[1])

    update_canvas()

    delay(0.03)
