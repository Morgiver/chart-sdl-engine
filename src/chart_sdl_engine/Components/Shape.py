from chart_sdl_engine.Components.Base import *

class SizeComponent(Component):
    """ Set a width and height size for the entity """
    def __init__(self, width: float, height: float):
        self.width = ctypes.c_int(width)
        self.height = ctypes.c_int(height)

class ShapeComponent(Component):
    """ Define the shape of the entity"""
    def __init__(self, shape_name: str):
        self.name = shape_name
