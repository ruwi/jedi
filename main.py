import pyglet
from pyglet.window import key


class MyWindow(pyglet.window.Window):
    def __init__(self, batch=None):
        super(MyWindow, self).__init__()
        self.batch = batch


    def on_key_press(self, symbol, modifiers):
        print "on_key_press", symbol, modifiers


    def on_draw(self):
        self.batch.draw()


class App(object):
    def __init__(self):
        self.app = pyglet.app
        self.batch = pyglet.graphics.Batch()
        self.window = MyWindow(batch=self.batch)


    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = App()
    app.run()
