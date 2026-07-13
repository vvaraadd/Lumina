from core.colors import BLACK
import config


class FrameBuffer:
    """
    Stores the color of every pixel on the display.
    """

    def __init__(self):
        self.width = config.GRID_WIDTH
        self.height = config.GRID_HEIGHT

        self.clear()

    def clear(self):
        """
        Fill the entire framebuffer with black.
        """

        self.pixels = [
            [BLACK for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def set_pixel(self, x, y, color):
        """
        Set one pixel.
        """

        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color

    def get_pixel(self, x, y):
        """
        Return the color of one pixel.
        """

        if 0 <= x < self.width and 0 <= y < self.height:
            return self.pixels[y][x]

        return BLACK

    def fill(self, color):
        """
        Fill the entire framebuffer with one color.
        """

        for y in range(self.height):
            for x in range(self.width):
                self.pixels[y][x] = color