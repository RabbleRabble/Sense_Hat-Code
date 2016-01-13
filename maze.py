from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

r=(255,0,0)
b=(0,0,0)
w=(255,255,255)
g=(0,255,0)

x=1
y=1


maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,r,r,b,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,b,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,r,b,r,r,r],
        [g,b,b,b,b,b,b,r]]

game_over=False

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch < 179 and x != 0:
        new_x -= 1
    elif 359 > pitch > 181 and x != 7:
        new_x += 1
    if 1 < roll < 179 and y != 7:
        new_y += 1
    elif 359 > roll > 181 and y != 0:
        new_y -= 1
    x,y=check_wall(x,y,new_x,new_y)
    return x,y

def check_wall(x,y,new_x,new_y):
    if maze[new_y][new_x] != r:
        return new_x, new_y
    elif maze[new_y][x] != r:
        return x, new_y
    elif maze[y][new_x] != r:
        return new_x, y
    return x,y

def check_win(x,y):
    global game_over
    if maze[y][x]==g:
        game_over=True
        sense.show_message('You Win', text_colour=[255,0,255])

def check_win2(x,y):
    global game_over
    if maze[y][x]==g:
        game_over=False
        sense.show_message('You Win Again!', text_colour=[255,0,255])

while not game_over:
    pitch=sense.get_orientation()['pitch']
    roll=sense.get_orientation()['roll']
    x,y = move_marble(pitch, roll, x, y)
    check_win(x,y)
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.05)
    maze[y][x] = b

sense.clear()

maze=[[b,b,b,b,b,b,b,b],
      [b,b,b,b,b,b,b,b],
      [b,b,b,b,b,b,b,b],
      [b,b,b,g,b,b,b,b],
      [b,b,b,b,b,b,b,b],
      [b,b,b,b,b,b,b,b],
      [b,b,b,b,b,b,b,b],
      [b,b,b,b,b,b,b,b]]

while game_over:
    pitch=sense.get_orientation()['pitch']
    roll=sense.get_orientation()['roll']
    x,y = move_marble(pitch, roll, x, y)
    check_win2(x,y)
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.05)
    maze[y][x] = b

sense.clear()
    
