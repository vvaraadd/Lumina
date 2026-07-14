from screens.splash import SplashScreen


class ScreenManager:
    """
    Controls which screen is active.
    """

    def __init__(self):

        self.current_screen = SplashScreen()

    def set_screen(self, screen):

        self.current_screen = screen

    def update(self):

        self.current_screen.update()

        if self.current_screen.is_finished():

            next_screen = self.current_screen.next_screen()

            if next_screen is not None:

                self.set_screen(next_screen)

    def draw(self, framebuffer):

        self.current_screen.draw(framebuffer)