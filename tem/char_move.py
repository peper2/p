from pico2d import *
import game_world
open_canvas()

bb = []
import stage01
stage1 = None
class Background:
    def __init__(self):
        self.image = load_image('image\\futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.width = self.image.w
        self.height = self.image.h
        self.x, self.y = 0, 0
        self.target = None
    def draw(self):
        self.image.clip_draw_to_origin(self.x, self.y, self.cw, self.ch, 0, 0)
    def update(self):
        if self.target == None:
            return
        self.x = clamp(0, int(self.target.x - self.cw // 2), self.width - self.cw)
        self.y = clamp(0, int(self.target.y - self.ch // 2), self.height - self.ch)



class Char:
    def __init__(self):
        self.x = 90
        self.y = 90    #처음 캐릭터 위치 설정
        self.image = load_image("image\\char_s.png")
        self.xb= 0
        self.yb = 0
        self.frame = 0      #첫번째 사진의 인덱스를 초기화
        self.move = False
        self.up = True
        self.down = True
        self.left = True
        self.right  = True
    def draw(self):
        self.image.clip_draw(self.frame*60,0,60,57,self.x,self.y)  #연속된 모션 사진을 출력하기 위한 커팅작업
    def update(self,box):
        self.frame = (self.frame + 1) % 4 #사진이 3장이므로 3으로 나눔

        # self.y += self.yb
        # self.x += self.xb
        # self.yb = 0
        # self.xb = 0

    def pos(self):
        return self.x - self.bg.x, self.y - self.bg.y

    def move_x(self,_x):
        self.x += _x
    def move_y(self,_y):
        self.y += _y
    def coll(self,box):
        if box.x   >= self.x + 60 and box.y  >= self.y + 60 : return        #사분면
        if box.x  >= self.x  + 60 and box.y <= self.y - 60  : return
        if box.x <= self.x - 60 and box.y >= self.y + 60 : return
        if box.x <= self.x - 60 and box.y <= self.y - 60 : return

        if box.y == self.y and self.x + 60 < box.x : return             #2칸이상떨어져있는
        if box.y == self.y and self.x - 60 > box.x: return
        if box.x == self.x and self.y + 60 < box.y: return
        if box.x == self.x and self.y - 60 > box.y: return

        if box.x-60  == self.x and box.y  == self.y:
            self.right = False

        if box.x + 60 == self.x and box.y == self.y:
            self.left = False

        if box.y + 60 == self.y and box.x == self.x:
            self.down = False
        if box.y - 60 == self.y and box.x == self.x:
            self.up = False
    def reset(self):
        self.down = True
        self.up = True
        self.right = True
        self.left = True
        #if box.y - self.y < 60:
         #   self.up = False
         #   self.yb = 0
        #else:
         #   self.up = True


        #if self.y - box.y < 60:
         #   self.down = False
         #   self.yb = 0
      #  else:
         #   self.down = True
    def stop(self):
        pass



class BackG:
    def __init__(self):
        self.image = load_image('image\\white.png')
        #self.frame = 0
        self.bgm = load_music('image\\back.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(400,300)




class Logo:
    def __init__(self):
        self.image = load_image('image\\logo.png')
        #print(self.image)
        self.frame = 0
        self.timer = 20
        self.onoff = True

    def draw(self):
        if self.onoff == True:
            self.image.clip_draw(self.frame * 800, 0, 800, 600, 400, 300)

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.timer -= 1
        if self.timer < 0:
            self.onoff = False

class Goal:
    def __init__(self):
        self.image = load_image('image\\goal.png')
        print(self.image)
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 60, 0, 60, 60, 750, 510)
    def update(self):
        self.frame = (self.frame + 1) % 2

char = Char()
back = BackG()
goal = Goal()
#box = Box()
# boxs1 = [Box(100 +(i*60),520) for i in range(15)]
# boxs2 = [Box(40 +(i*60),40) for i in range(13)]
# box3 = Box(460,460)
# box4 = [Box(40,40+(i*60)) for i in range(13)]

logo = Logo()

#Edit = [[1],[2],[3],[4],[5],[6],[7],[8],[],[]]

edit =  [[ 1,1,1,1,1,1,1,1,1,1],        #!
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
         [ 1,1,1,1,1,1,1,1,0,1]]        #13

#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

# for i in range(10):
#     for j in range(10):
#         box.draw(edit[i],[j])
import player
playerchar = None

running = True


current_time = get_time()
def update():
    global current_time,stage1


    game_world.frame_time = get_time() - current_time

    current_time += game_world.frame_time



def main():
    global current_time
    current_time = get_time()
    playerchar = player.Player()
    stage01.stage1.enter()
    while running:

        clear_canvas()
        playerchar.update()
        stage01.stage1.update()
        playerchar.draw()
        stage01.stage1.draw()
        update()
        playerchar.handle_events()
        update_canvas()

        continue
        #handle_events()
        char.reset()
        # for i in range(13):
        #     #boxs1[i].draw()


        #box3.draw()
        back.draw()
        BB.draw()
        #char.update()
        #logo.update()
        char.draw()
        #logo.draw()
        goal.draw()
        goal.update()
        BB.update()
        #for i in boxs1:
            #char.coll(i)

        # bb = []
        #
        # for i in range(13):
        #     for j in range(10):
        #         if edit[i][j] == 1:
        #             tempBox = Box(30+(i*60),30+(j*60))
        #             bb.append(tempBox)
        # for k in bb:
        #     char.coll(k)

        # for i in bb:
        #     i.draw()

        handle_events()
        update_canvas()

if __name__ == '__main__':
    main()

def move_update(obj):
    pass

