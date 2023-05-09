from chart_sdl_engine.Components.Base import *

class PositionComponent(Component):
    """ Set a position point x, y for the Entity"""
    def __init__(self, x: float, y: float):
        self.x = ctypes.c_int(x)
        self.y = ctypes.c_int(y)

class VectorComponent(Component):
    """ Set a list of coordinates point for the entity """
    def __init__(self, coordinates: list[tuple[float, float]]):
        self.coordinates = coordinates
