try:
    import pygame
except Exception:
    class _Clock:
        def tick(self, fps=0):
            return None

    class _EventModule:
        @staticmethod
        def get():
            return []

    class _PygameStub:
        time = _Clock()
        event = _EventModule()
        QUIT = 256

    pygame = _PygameStub()

from core.display import Display
from core.framebuffer import FrameBuffer
from core.colors import RED, GREEN, BLUE, WHITE

import config


class App:

    def __init__(self):

        self.display = Display()
        self.framebuffer = FrameBuffer()

        self.running = True

        self.clock = pygame.time.Clock()

    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            # -------------------------
            # Demo
            # -------------------------

            self.framebuffer.clear()

            self.framebuffer.draw_rectangle(
                2,
                2,
                28,
                28,
                RED,
            )

            self.framebuffer.fill_rectangle(
                10,
                10,
                8,
                8,
                GREEN,
            )

            self.framebuffer.draw_line(
                0,
                0,
                31,
                31,
                BLUE,
            )

            self.framebuffer.draw_line(
                31,
                0,
                0,
                31,
                WHITE,
            )

            # -------------------------

            self.display.render(self.framebuffer)

            self.clock.tick(config.FPS)

        self.display.close()