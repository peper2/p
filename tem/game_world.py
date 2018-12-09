from pico2d import *

objects = [[],[],[]]
layer_bg = 0
layer_player = 1
layer_obstacle = 2

PIXEL_PER_METER = (10.0/ 0.3)
GRASS_SPEED = 400.0
GRASS_SPEED_MPM = (GRASS_SPEED * 1000.0 / 60.0)
GRASS_SPEED_MPS = (GRASS_SPEED_MPM / 60.0)
GRASS_SPEED_PPS = (GRASS_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/ TIME_PER_ACTION
frame_time = 0.0

def add_object(o, layer):
	objects[layer].append(o)

def remove_object(o):
	for i in range(len(objects)):
		if o in objects[i]:
			print('deleting', o)
			objects[i].remove(o)
			del o
def clear():
	for o in all_objects():
		del o
	objects.clear()
def all_objects():
	for i in range(len(objects)):
		for o in objects[i]:
			yield o
def objects_at_layer(layer):
	for o in objects[layer]:
		yield o
def update():
	for o in all_objects():
		o.update()
def draw():
	for o in all_objects():
		o.draw()

background = load_image("image\\back2.png")
def blank_draw():
    global background
    background.draw(400,300)
