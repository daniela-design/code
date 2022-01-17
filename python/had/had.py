from pathlib import Path
import pyglet
import random

TILE_SIZE = 64
TILES_DIRECTORY = Path('snake-tiles')

class State:
    def __init__(self):
        self.snake = [(0, 0), (1, 0)]
        self.snake_direction = 0, 1
        self.width = 10
        self.height = 10
        self.food = []
        self.add_food()
        self.add_food()
        self.snake_alive = True
        self.queued_directions = []

    def move(self):
        if self.queued_directions:
            new_direction = self.queued_directions[0]
            del self.queued_directions[0]
            # self.snake_direction = new_direction
            old_x, old_y = self.snake_direction
            new_x, new_y = new_direction
            if (old_x, old_y) != (-new_x, -new_y):
                self.snake_direction = new_direction
        
        if not self.snake_alive:
            return

        old_x, old_y = self.snake[-1]
        dir_x, dir_y = self.snake_direction
        new_x = old_x + dir_x
        new_y = old_y + dir_y
        
        if new_x < 0:
            self.snake_alive = False
        if new_y < 0:
            self.snake_alive = False
        if new_x >= self.width:
            self.snake_alive = False
        if new_y >= self.height:
            self.snake_alive = False
        
        new_head = new_x, new_y

        if new_head in self.snake:
            self.snake_alive = False

        self.snake.append(new_head)
        if new_head in self.food:
            self.food.remove(new_head)
            self.add_food()
        else:
            del self.snake[0]

        
    def add_food(self):
        for try_number in range(100):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            position = x, y
            if (position not in self.snake) and (position not in self.food):
                self.food.append(position)
                return

red_image = pyglet.image.load("apple.png")

snake_tiles = {}
for path in TILES_DIRECTORY.glob('*.png'):
    snake_tiles[path.stem] = pyglet.image.load(path)


window = pyglet.window.Window()

state = State()
state.width = window.width // TILE_SIZE
state.height = window.height // TILE_SIZE

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
    # for x, y in state.snake:
    #     source = "end"
    #     dest = "end"
    #     if dest == 'end' and not state.snake_alive:
    #         dest = 'dead'
    #     snake_tiles[source + "-" + dest].blit(x*TILE_SIZE, y*TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)
    
    for i in range(len(state.snake)):
        x = state.snake[i][0]
        y = state.snake[i][1]

        vysl = x - state.snake[i-1][0]
        if i != len(state.snake)-1:
            vysl2 = y - state.snake[i+1][1]

        if i == 0:
            source = "end"
        else:
            if vysl == 1:
                source = "left"
            elif vysl == -1:
                source = "right"
            elif vysl == 0:
                source = "bottom"
            else:
                source = "top"
        
        if i == len(state.snake)-1: 
            dest = "end"
        else:
            if vysl2 == -1:
                dest = "top"
            elif vysl2 == 1:
                dest = "bottom"
            elif vysl2 == 0:
                dest = "right"
            else:
                dest = "left"
        snake_tiles[source + "-" + dest].blit(x*TILE_SIZE, y*TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)

    for x, y in state.food:
        red_image.blit(x*TILE_SIZE, y*TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)

@window.event
def on_key_press(key_code, modifier):
    if key_code == pyglet.window.key.LEFT:
        new_direction = -1, 0
    if key_code == pyglet.window.key.RIGHT:
        new_direction = 1, 0
    if key_code == pyglet.window.key.DOWN:
        new_direction = 0, -1
    if key_code == pyglet.window.key.UP:
        new_direction = 0, 1
    state.queued_directions.append(new_direction)

def move(dt):
    state.move()

pyglet.clock.schedule_interval(move, 1/6)

pyglet.app.run()