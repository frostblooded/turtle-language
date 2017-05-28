from enum import Enum


class Command(Enum):
    PEN_CHOOSE = 'P'
    PEN_DOWN = 'D'
    PEN_UP = 'U'
    DRAW_WEST = 'W'
    DRAW_NORTH = 'N'
    DRAW_EAST = 'E'
    DRAW_SOUTH = 'S'
