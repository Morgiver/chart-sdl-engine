import ctypes
from sdl2 import *

class Component:
    """ Defining the Component Type"""
    pass

class DrawableComponent(Component):
    """ Set the entity has drawable for the RenderSystem """
    pass

class MouseStateComponent(Component):
    """ Set the state of the mouse """
    def __init__(self):
        self.mode = "cursor"
        # cursor
        # line
        # attached
        # cursor

class MouseAttachComponent(Component):
    """ Set an entity Point coordinates attached to the mouse's coordinates"""
    def __init__(self, mouse_x: float, mouse_y: float, point_name: str):
        self.x = ctypes.c_int(mouse_x)
        self.y = ctypes.c_int(mouse_y)
        self.point_name = point_name

    def update(self, x, y):
        self.x = x
        self.y = y

class DraggedComponent(Component):
    """ Set entity has dragged by the mouse """
    def __init__(self, mouse_x: float, mouse_y: float):
        self.x = mouse_x
        self.y = mouse_y

class PositionComponent(Component):
    """ Set a position point x, y for the Entity"""
    def __init__(self, x: float, y: float):
        self.x = ctypes.c_int(x)
        self.y = ctypes.c_int(y)

class VectorComponent(Component):
    """ Set a list of coordinates point for the entity """
    def __init__(self, coordinates: list[tuple[float, float]]):
        self.coordinates = coordinates

class SizeComponent(Component):
    """ Set a width and height size for the entity """
    def __init__(self, width: float, height: float):
        self.width = ctypes.c_int(width)
        self.height = ctypes.c_int(height)

class FillRectComponent(Component):
    """ Draw a Rectangle filled with color """
    def __init__(self, r: int = 255, g: int = 255, b: int = 255, a: int = 255) -> None:
        """
        Initialization

        Parameters:
            r (int): Red Color
            g (int): Green Color
            b (int): Blue Color
            a (int): Alpha Value

        Returns:
            None
        """
        self.r = ctypes.c_ubyte(r)
        self.g = ctypes.c_ubyte(g)
        self.b = ctypes.c_ubyte(b)
        self.a = ctypes.c_ubyte(a)

class ShapeComponent(Component):
    """ Define the shape of the entity"""
    def __init__(self, shape_name: str):
        self.name = shape_name

class ColorComponent(Component):
    """
    Handling rgba int data and converter them into ctype.c_ubytes
    """
    def __init__(self, r: int = 255, g: int = 255, b: int = 255, a: int = 255) -> None:
        """
        Initialization

        Parameters:
            r (int): Red Color
            g (int): Green Color
            b (int): Blue Color
            a (int): Alpha Value

        Returns:
            None
        """
        self.r = ctypes.c_ubyte(r)
        self.g = ctypes.c_ubyte(g)
        self.b = ctypes.c_ubyte(b)
        self.a = ctypes.c_ubyte(a)

class HoverableComponent(Component):
    """ Set the entity has hoverable """
    pass
