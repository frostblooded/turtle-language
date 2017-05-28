class PenHandler:
    def __init__(self):
        self.pens = {}
        self.pen_current = None
        self.pen_active = False

    def draw(self, distance, radians):
        if not self.pen_active:
            return

        # other stuff
