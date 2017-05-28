class PenHandler:
    EAST_DEGREES = 0
    NORTH_DEGREES = 90
    WEST_DEGREES = 180
    SOUTH_DEGREES = 270

    def __init__(self):
        self.pens = {}
        self.pen_current = None
        self.pen_active = False

    def draw(self, distance, degrees):
        if not self.pen_active:
            return

        self.pen_current.setheading(degrees)
        self.pen_current.forward(distance)
