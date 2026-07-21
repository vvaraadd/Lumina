class Screen:
    """
    Base class for every Lumina screen.
    """

    def __init__(self):
        self.widgets = []

    def update(self):
        for widget in self.widgets:
            if widget.visible:
                widget.update()

    def draw(self, framebuffer):
        framebuffer.clear()

        for widget in self.widgets:
            if widget.visible:
                widget.draw(framebuffer)

    def is_finished(self):
        return False

    def next_screen(self):
        return None