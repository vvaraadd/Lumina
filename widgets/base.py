class Widget:
    """
    Base class for every widget in Lumina.
    """

    def __init__(self):
        self.visible = True

    def update(self):
        """
        Update the widget.
        """
        pass

    def draw(self, framebuffer):
        """
        Draw the widget.
        """
        pass