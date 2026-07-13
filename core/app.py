import pygame

from core.display import Display
from core.framebuffer import FrameBuffer
from core.colors import RED

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

            self.framebuffer.set_pixel(15, 15, RED)

            # -------------------------

            self.display.render(self.framebuffer)

            self.clock.tick(config.FPS)

        self.display.close()