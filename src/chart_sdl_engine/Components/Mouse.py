from chart_sdl_engine.Components.Base import *

class MouseStateComponent(Component):
    """ Set the state of the mouse """
    def __init__(self, e_id = None, mode = "cursor"):
        self.entity = e_id
        self.mode = mode

class OnLeftButtonUpEvent(Component):
    def __init__(self, callback):
        self.callback = callback

class OnRightButtonUpEvent(Component):
    def __init__(self, callback):
        self.callback = callback

class MouseAttachComponent(Component):
    """ Set an entity Point coordinates attached to the mouse's coordinates"""
    def __init__(self, mouse_x: float, mouse_y: float, point_name: str):
        self.x = ctypes.c_int(mouse_x)
        self.y = ctypes.c_int(mouse_y)
        self.point_name = point_name

    def update(self, x, y):
        self.x = x
        self.y = y

class SelectableComponent(Component):
    def __init__(self):
        pass

class DraggedComponent(Component):
    """ Set entity has dragged by the mouse """
    def __init__(self, mouse_x: float, mouse_y: float):
        self.x = mouse_x
        self.y = mouse_y

class HoverableComponent(Component):
    """ Set the entity has hoverable """
    pass
