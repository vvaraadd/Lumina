import pygame

import config


class PygameRenderer:
    """
    Draws the framebuffer onto a pygame window.
    """

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode(
            (
                config.GRID_WIDTH * config.PIXEL_SIZE,
                config.GRID_HEIGHT * config.PIXEL_SIZE,
            )
        )

        pygame.display.set_caption(config.WINDOW_TITLE)

    def render(self, framebuffer):

        self.screen.fill(config.BACKGROUND_COLOR)

        for y in range(config.GRID_HEIGHT):
            for x in range(config.GRID_WIDTH):

                color = framebuffer.get_pixel(x, y)

                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        x * config.PIXEL_SIZE,
                        y * config.PIXEL_SIZE,
                        config.PIXEL_SIZE - 1,
                        config.PIXEL_SIZE - 1,
                    ),
                )

        pygame.display.flip()

    def close(self):

        pygame.quit()