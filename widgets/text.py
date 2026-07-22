from core import framebuffer
from widgets.base import Widget

from core.alignment import LEFT, CENTER, RIGHT


class TextWidget(Widget):
    """
    Displays text on the screen.
    """

    def __init__(
        self,
        x,
        y,
        text,
        color,
        alignment=LEFT,
    ):
        super().__init__()

        self.x = x
        self.start_x = x
        self.y = y

        self.text = text
        self.color = color

        self.alignment = alignment

    def update(self):
        if not self.scroll:
            return

        self.scroll_timer += 1

        if self.scroll_timer >= self.scroll_delay:
            self.scroll_offset += self.scroll_speed
            self.scroll_timer = 0

    def draw(self, framebuffer):

        if len(self.text) == 0:
            return

        text_width = framebuffer.get_text_width(self.text)

        draw_x = self.x - self.scroll_offset

        if self.alignment == CENTER:
            draw_x -= text_width // 2

        elif self.alignment == RIGHT:
            draw_x -= text_width

        if self.scroll and draw_x + text_width < 0:
            self.scroll_offset = 0

        framebuffer.draw_text(
            draw_x,
            self.y,
            self.text,
            self.color,
        )

        if self.scroll and draw_x + text_width < 0:
            self.scroll_offset = -framebuffer.width

    def __init__(
    self,
    x,
    y,
    text,
    color,
    alignment=LEFT,
    scroll=False,
):
        super().__init__()

        self.x = x
        self.y = y

        self.text = text
        self.color = color

        self.alignment = alignment

        self.scroll = scroll
        self.scroll_offset = 0
        self.scroll_speed = 1
        self.scroll_delay = 2
        self.scroll_timer = 0