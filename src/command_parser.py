from turtle import Turtle

from src.command import Command
from src.pen_handler import PenHandler


class CommandParser:
    def __init__(self):
        self.commands = {
            Command.PEN_CHOOSE: self.pen_choose,
            Command.PEN_DOWN: self.pen_down,
            Command.PEN_UP: self.pen_up,
            Command.DRAW_WEST: self.draw_west,
            Command.DRAW_NORTH: self.draw_north,
            Command.DRAW_EAST: self.draw_east,
            Command.DRAW_SOUTH: self.draw_south
        }

        self.pen_handler = PenHandler()

    def pen_choose(self, *args):
        new_pen = args[0]

        if self.pen_handler.pens.get(new_pen) is None:
            self.pen_handler.pens[new_pen] = Turtle()

        self.pen_handler.pen_current = self.pen_handler.pens[new_pen]

    def pen_down(self, *args):
        self.pen_handler.pen_active = True

    def pen_up(self, *args):
        self.pen_handler.pen_active = False

    def draw_west(self, *args):
        self.pen_handler.draw(args[0], PenHandler.WEST_DEGREES)

    def draw_north(self, *args):
        self.pen_handler.draw(args[0], PenHandler.NORTH_DEGREES)

    def draw_east(self, *args):
        self.pen_handler.draw(args[0], PenHandler.EAST_DEGREES)

    def draw_south(self, *args):
        self.pen_handler.draw(args[0], PenHandler.SOUTH_DEGREES)

    def handle_command(self, command, arg):
        if arg is not None:
            arg = int(arg)

        self.commands[command](arg)
