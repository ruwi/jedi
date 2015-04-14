import pyglet
from pyglet.window import key


class MyWindow(pyglet.window.Window):
    def on_key_press(self, symbol, modifiers):
        print "on_key_press", symbol, modifiers


class App(object):
    def __init__(self):
        self.app = pyglet.app
        self.batch = pyglet.graphics.Batch()
        self.window = MyWindow()

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = App()
    app.run()
