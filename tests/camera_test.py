import unittest

from src.trading_chart_sdl import *

class TestCamera(unittest.TestCase):
    def TestSimpleWindow(self):
        c = SDLChart()

        my_line = Line(
            Point(random.randrange(0, 250), random.randrange(0, 250)),
            Point(random.randrange(0, 250), random.randrange(0, 250)),
            Color(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), 255)
        )

        c.initialize()
        c.entities.append(my_line)

        is_running = True
        while is_running:
            if not c.run():
                break
