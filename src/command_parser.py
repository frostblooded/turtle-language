from turtle import Turtle

from src.command import Command


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

        self.current_turtle = None
        self.current_turtle_active = False
        self.turtles = {}

    def pen_choose(self, *args):
        new_pen = args[0]

        if self.turtles.get(new_pen) is None:
            self.turtles[new_pen] = Turtle()

        self.current_turtle = self.turtles[new_pen]

    def pen_down(self, *args):
        self.current_turtle_active = True

    def pen_up(self, *args):
        self.current_turtle_active = False

    def draw_west(self, *args):
        pass

    def draw_north(self, *args):
        pass

    def draw_east(self, *args):
        pass

    def draw_south(self, *args):
        pass

    def handle_command(self, command, arg):
        self.commands[command](arg)
