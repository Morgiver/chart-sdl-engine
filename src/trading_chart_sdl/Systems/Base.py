import uuid
import ctypes
from sdl2 import *
from trading_chart_sdl.Managers import *
from trading_chart_sdl.Components import *

class System:
    """ Defining the System Type """
    @staticmethod
    def update(em: EntityManager, renderer: render.SDL_Renderer, e_id: uuid.UUID) -> None:
        pass
