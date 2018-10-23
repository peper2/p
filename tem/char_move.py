from pico2d import *
open_canvas()

class Char:
    def __init__(self):
        self.x = 100
        self.y = 100      #처음 캐릭터 위치 설정
        self.image = load_image("char_s.png")
        self.frame = 0      #첫번째 사진의 인덱스를 초기화
    def draw(self):
        self.image.clip_draw(self.frame*60,0,60,57,self.x,self.y)  #연속된 모션 사진을 출력하기 위한 커팅작업
    def update(self):
        self.frame = (self.frame + 1)%4     #사진이 3장이므로 3으로 나눔
    def move_x(self,_x):
        self.x += _x
    def move_y(self,_y):
        self.y += _y

class BackG:
    def __init__(self):
        self.image = load_image('back.png')
        print(self.image)
        self.frame = 0
        self.bgm = load_music('back.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(400,300)

class Goal:
    def __init__(self):
        self.image = load_image('goal.png')
        print(self.image)
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 60, 0, 60, 60, 102, 280)
    def update(self):
        self.frame = (self.frame + 1) % 2


char = Char()
grass = BackG()
goal = Goal()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            close_canvas()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                char.move_x(300)
            elif event.key == SDLK_LEFT:
                char.move_x(-300)
            elif event.key == SDLK_UP:
                char.move_y(180)
            elif event.key == SDLK_DOWN:
                char.move_y(-180)


running = True



while running:
    clear_canvas()
    handle_events()

    char.update()
    goal.update()
    grass.draw()
    goal.draw()
    char.draw()


    update_canvas()
    delay(0.15)