from screens.base import Screen
from screens.demo import DemoScreen

from core.colors import WHITE


class SplashScreen(Screen):

    def __init__(self):

        super().__init__()

        self.frames = 0

    def update(self):

        self.frames += 1

    def draw(self, framebuffer):

        framebuffer.clear()

        framebuffer.fill_rectangle(
            12,
            12,
            8,
            8,
            WHITE,
        )

    def is_finished(self):

        return self.frames >= 120

    def next_screen(self):

        return DemoScreen()