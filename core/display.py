from renderers.pygame_renderer import PygameRenderer


class Display:

    def __init__(self):

        self.renderer = PygameRenderer()

    def render(self, framebuffer):

        self.renderer.render(framebuffer)

    def close(self):

        self.renderer.close()