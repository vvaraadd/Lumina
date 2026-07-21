from screens.base import Screen
from widgets.clock import ClockWidget
from core.colors import WHITE


class DemoScreen(Screen):

    def __init__(self):
        super().__init__()

        self.widgets.append(
            ClockWidget(1, 10, WHITE)
        )