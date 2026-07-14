from screens.base import Screen
from core.colors import RED, GREEN, BLUE, WHITE


class DemoScreen(Screen):

    def update(self):
        pass

    def draw(self, framebuffer):

        framebuffer.clear()

        framebuffer.draw_rectangle(
            2,
            2,
            28,
            28,
            RED,
        )

        framebuffer.fill_rectangle(
            10,
            10,
            8,
            8,
            GREEN,
        )

        framebuffer.draw_line(
            0,
            0,
            31,
            31,
            BLUE,
        )

        framebuffer.draw_line(
            31,
            0,
            0,
            31,
            WHITE,
        )