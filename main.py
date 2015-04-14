import pyglet
from pyglet.window import key

class GameLogic(object):
    def __init__(self):
        self.pos = [20, 20]
        self.vel = [0, 0]
        self.dt = 10

    def head_up(self):
        print "head_up"
        self.vel[1] = 1

    def tick(self):
        for i in (0, 1):
            self.pos[i] += self.vel[i] * self.dt

    def stop_moving(self):
        for i in (0, 1):
            self.vel[i] = 0


class MyWindow(pyglet.window.Window):
    """Main Window class"""

    def __init__(self, batch=None):
        super(MyWindow, self).__init__()
        self.batch = batch
        self.game_logic = GameLogic()
        self.fps = 60

        image = pyglet.image.load("circle.png")
        self.sprites = [pyglet.sprite.Sprite(image, batch=self.batch)]

        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        pyglet.clock.schedule_interval(self.on_tick, 1./self.fps)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.game_logic.head_up()

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.game_logic.stop_moving()

    def on_tick(self, dt):
        self.game_logic.tick()

    def on_draw(self):
        self.sprites[0].x, self.sprites[0].y = self.game_logic.pos

        pyglet.gl.glClearColor(1., 1., 1., 1.)
        self.clear()
        self.batch.draw()


class App(object):
    """Main application class"""

    def __init__(self):
        self.app = pyglet.app
        self.batch = pyglet.graphics.Batch()
        self.window = MyWindow(batch=self.batch)

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = App()
    app.run()
