from pico2d import *
import mygame
import game_world
import math
import box
class Effect:
    def __init__(self):
        self.images = [load_image("image\\runing2.png"), load_image("image\\runing3.png")]
        self.view_y2 = 0
        self.view_y = 0
        self.x = 0
        self.y = 0
        self.velocity = game_world.GRASS_SPEED_PPS
        self.moving = False
        self.start = False
        self.dir = 3.141592 *2
        self.term_y = 0
        self.term_x = 0
        self.last_start = 0
    def draw(self):
        #self.images[1].clip_draw(0,0, self.view_x, self.view_y, self.x, self.y)
        self.images[1].clip_composite_draw(0, 0, 18, int(self.view_y), self.dir, '', self.x, self.y,
                                          18, int(self.view_y))
        self.images[0].clip_composite_draw(0, 0, 50, int(self.view_y2)-30, self.dir, '', self.x+self.term_x, self.y + self.term_y,
                                           50, int(self.view_y2)-30)
    def reverse_smooth_time(self):
        return self.velocity * game_world.frame_time /4
    def smooth_time(self):
        if get_time() - mygame.key_pree_time < 0.1:
            return self.velocity * game_world.frame_time / 4
        elif get_time() - mygame.key_pree_time < 0.05:
            return self.velocity * game_world.frame_time / 5
        else: return self.velocity * game_world.frame_time / 3
    def update(self,player):
        self.smooth_time()
        if self.moving :
            if self.start :
                if player.go_dir == 2:
                    self.dir = 3.141592 *2
                    if self.view_y < 360:
                        self.view_y += self.smooth_time()
                        self.y = player.y - (self.view_y /2)
                    else :
                        self.view_y = 360
                        self.y = player.y - 180

                    if self.view_y2 < 300:
                        self.view_y2 += self.smooth_time()
                        self.term_y = 40
                        self.term_x = 0
                    else :
                        self.view_y2 = 300

                if player.go_dir == 3:
                    self.dir = 3.141592 *2
                    if self.view_y <  360:
                        self.view_y += self.smooth_time()
                        self.y = player.y + (self.view_y / 2)
                    else:
                        self.view_y = 360
                        self.y = player.y + 180
                    if self.view_y2 < 300:
                        self.view_y2 += self.smooth_time()
                        self.term_y = -40
                        self.term_x = 0
                    else:
                        self.view_y2 = 300
                if player.go_dir == 0:
                    self.dir = - 3.141592 / 2
                    if self.view_y < 360:
                        self.view_y += self.smooth_time()
                        self.x = player.x + (self.view_y / 2)
                    else:
                        self.view_y = 360
                        self.x = player.x + 180
                    if self.view_y2 < 300:
                        self.view_y2 += self.smooth_time()
                        self.term_y = 0
                        self.term_x =  -40
                    else:
                        self.view_y2 = 300
                if player.go_dir == 1:
                    self.dir = - 3.141592 / 2
                    if self.view_y < 360:
                        self.view_y += self.smooth_time()
                        self.x = player.x - (self.view_y / 2)
                    else:
                        self.view_y = 360
                        self.x = player.x - 180
                    if self.view_y2 < 300:
                        self.view_y2 += self.smooth_time()
                        self.term_y = 0
                        self.term_x = 40
                    else:
                        self.view_y2 = 300
            elif self.start== False:        #단축
                if player.go_dir == 2:
                    if self.view_y > 0:
                        if box.end_time:
                            self.view_y -= self.reverse_smooth_time()
                        else : self.view_y -= self.smooth_time() *2
                        self.y = player.y - (self.view_y /2)
                    elif self.view_y <= 0 :
                        self.exit()
                    if self.view_y2 >0:
                        if box.end_time:
                            self.view_y2 -= self.reverse_smooth_time()
                        else : self.view_y2 -= self.smooth_time()*2
                    elif self.view_y2 <= 0:
                        self.view_y2 = 0
                if player.go_dir == 3:
                    if self.view_y > 0:
                        if box.end_time:
                            self.view_y -= self.reverse_smooth_time()
                        else :self.view_y -= self.smooth_time()*2
                        self.y = player.y + (self.view_y / 2)
                    elif self.view_y <= 0:
                        self.exit()
                    if self.view_y2 >0:
                        if box.end_time:
                            self.view_y2 -= self.reverse_smooth_time()
                        else :self.view_y2 -= self.smooth_time()*2
                    elif self.view_y2 <= 0:
                        self.view_y2 = 0
                if player.go_dir == 0:
                    if self.view_y > 0:
                        if box.end_time:
                            self.view_y -= self.reverse_smooth_time()
                        else : self.view_y -= self.smooth_time()*2
                        self.x = player.x + (self.view_y / 2)
                    elif self.view_y <= 0:

                        self.exit()
                    if self.view_y2 > 0:
                        if box.end_time:
                            self.view_y2 -= self.reverse_smooth_time()
                        else :self.view_y2 -= self.smooth_time()*2
                    elif self.view_y2 <= 0:
                        self.view_y2 = 0
                if player.go_dir == 1:
                    if self.view_y > 0:
                        if box.end_time:
                            self.view_y -= self.reverse_smooth_time()
                        else : self.view_y -= self.smooth_time()*2
                        self.x = player.x - (self.view_y / 2)
                    elif self.view_y <= 0:
                        self.exit()
                    if self.view_y2 > 0:
                        if box.end_time:
                            self.view_y2 -= self.reverse_smooth_time()
                        else : self.view_y2 -= self.smooth_time()*2
                    elif self.view_y2 <= 0:
                        self.view_y2 = 0
    def exit(self):
        self.term_x = 0
        self.term_y = 0
        self.moving = False
        self.view_y = 0
    def enter(self,player_x,player_y):
        self.moving = True
        self.start = True
        self.x = player_x
        self.y = player_y
        #self.y = player_y - self.view_y
