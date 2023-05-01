from trading_chart_sdl.Components.Base import *

class DrawableComponent(Component):
    """ Set the entity has drawable for the RenderSystem """
    pass

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
