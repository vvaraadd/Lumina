try:
    import pygame
except Exception:  # pragma: no cover - fallback for environments without pygame
    class _Clock:
        def tick(self, fps=0):
            return None

    class _EventModule:
        @staticmethod
        def get():
            return []

    class _TimeModule:
        @staticmethod
        def Clock():
            return _Clock()

    class _PygameStub:
        time = _TimeModule()
        event = _EventModule()
        QUIT = 256

    pygame = _PygameStub()

from core.display import Display
from core.framebuffer import FrameBuffer
from core.screen_manager import ScreenManager

import config


class App:

    def __init__(self):

        self.display = Display()
        self.framebuffer = FrameBuffer()
        self.screen_manager = ScreenManager()

        self.running = True

        self.clock = pygame.time.Clock()

    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            # Update the current screen
            self.screen_manager.update()

            # Draw the current screen
            self.screen_manager.draw(self.framebuffer)

            # Render the framebuffer
            self.display.render(self.framebuffer)

            # Limit FPS
            self.clock.tick(config.FPS)

        self.display.close()