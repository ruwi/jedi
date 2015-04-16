# -*- coding: utf-8 -*-

from collections import namedtuple
import numbers

import pyglet
from pyglet.window import key


class Vec2(namedtuple('Vec2', ('x', 'y'))):
    """A 2D vector"""

    def __add__(self, other):
        if not isinstance(other, Vec2):
            return NotImplemented

        return Vec2(
            x = self.x + other.x, y = self.y + other.y,
        )

    def __mul__(self, other):
        if not isinstance(other, numbers.Number):
            return NotImplemented

        return Vec2(
            x = self.x * other, y = self.y * other,
        )

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self + (-1) * other



class GameLogic(object):
    def __init__(self):
        self.pos = Vec2(20, 20)
        self.vel = Vec2(0, 0)
        # 0 is right, 90 is up, as in polar coordinates.
        self.orientation = 90
        self.rot_speed = 0
        self.dt = 10

    def head_up(self):
        self.vel += Vec2(0, 1)

    def head_down(self):
        self.vel += Vec2(0, -1)

    def head_right(self):
        self.vel += Vec2(1, 0)

    def head_left(self):
        self.vel += Vec2(-1, 0)

    def rotate_left(self):
        self.rot_speed -= 1

    def rotate_right(self):
        self.rot_speed += 1

    def tick(self):
        self.pos += self.vel * self.dt

    def stop_moving(self):
        self.vel = Vec2(0, 0)


class MyWindow(pyglet.window.Window):
    """Main Window class"""

    def __init__(self, batch=None):
        super(MyWindow, self).__init__()
        self.batch = batch
        self.game_logic = GameLogic()
        self.fps = 60

        image = pyglet.image.load("jedi.png")
        self.sprites = [pyglet.sprite.Sprite(image, batch=self.batch)]

        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        pyglet.clock.schedule_interval(self.on_tick, 1./self.fps)

        self.key_down_actions = {
            key.UP: self.game_logic.head_up,
            key.DOWN: self.game_logic.head_down,
            key.RIGHT: self.game_logic.head_right,
            key.LEFT: self.game_logic.head_left,
        }
        self.key_up_actions = {
            key.UP: self.game_logic.head_down,
            key.DOWN: self.game_logic.head_up,
            key.RIGHT: self.game_logic.head_left,
            key.LEFT: self.game_logic.head_right,
        }

    def on_key_press(self, symbol, modifiers):
        self.key_down_actions.get(symbol, lambda:None)() 

    def on_key_release(self, symbol, modifiers):
        self.key_up_actions.get(symbol, lambda:None)() 

    def on_tick(self, dt):
        self.game_logic.tick()

    def on_draw(self):
        self.sprites[0].position = self.game_logic.pos
        # Pyglet uses clockwise rotations.
        self.sprites[0].rotation = -self.game_logic.orientation

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
