class Screen:
    """
    Base class for every Lumina screen.
    """

    def __init__(self):
        pass

    def update(self):
        """
        Update the screen.
        """
        pass

    def draw(self, framebuffer):
        """
        Draw the screen.
        """
        pass

    def is_finished(self):
        """
        Returns True when this screen is finished.
        """
        return False

    def next_screen(self):
        """
        Returns the next screen.
        """
        return None