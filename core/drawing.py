class DrawingMixin:
    """
    Drawing functions for the framebuffer.
    """

    def draw_line(self, x1, y1, x2, y2, color):

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        err = dx - dy

        while True:

            self.set_pixel(x1, y1, color)

            if x1 == x2 and y1 == y2:
                break

            e2 = 2 * err

            if e2 > -dy:
                err -= dy
                x1 += sx

            if e2 < dx:
                err += dx
                y1 += sy

    def draw_rectangle(self, x, y, width, height, color):

        self.draw_line(x, y, x + width - 1, y, color)

        self.draw_line(
            x,
            y + height - 1,
            x + width - 1,
            y + height - 1,
            color,
        )

        self.draw_line(x, y, x, y + height - 1, color)

        self.draw_line(
            x + width - 1,
            y,
            x + width - 1,
            y + height - 1,
            color,
        )

    def fill_rectangle(self, x, y, width, height, color):

        for row in range(y, y + height):

            self.draw_line(
                x,
                row,
                x + width - 1,
                row,
                color,
            )
