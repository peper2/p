from pico2d import *

speed = 10

def handle_events():
    global running
    global x, y
    global k
    global xp,yp
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEMOTION:
            xp= e.x
            yp = 600- e.y
open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

x, y = 800 // 2, 90
xp,yp = 800//2, 90
k=0
frame = 0
running = True
while running:
    
    grass.draw(400, 30)
    
    if(x <= xp and y <= yp):
        if(x != xp):
            x = x +10
        if(y != yp):
            y = y +10
    elif(x <= xp and y >= yp):
        if(x != xp):
            x = x +10
        if(y != yp):
            y = y -10
    elif(x >= xp and y <= yp):
        if(x != xp):
            x = x -10
        if(y != yp):
            y = y +10
    elif(x >= xp and y >= yp):
        if(x != xp):
            x = x -10
        if(y != yp):
            y = y -10
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    clear_canvas()
    frame = (frame + 1) % 8
    delay(0.001)
    
close_canvas()
