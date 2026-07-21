from datetime import datetime

from widgets.base import Widget


class ClockWidget(Widget):

    def __init__(self, x, y, color):
        super().__init__()

        self.x = x
        self.y = y
        self.color = color

        self.time = ""

    def update(self):
        self.time = datetime.now().strftime("%H:%M")

    def draw(self, framebuffer):
        framebuffer.draw_text(
            self.x,
            self.y,
            self.time,
            self.color,
        )