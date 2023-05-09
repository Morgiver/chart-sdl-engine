import uuid
import ctypes
from sdl2 import *
from chart_sdl_engine.Managers import *
from chart_sdl_engine.Components import *

class System:
    """ Defining the System Type """
    @staticmethod
    def update(em: EntityManager, renderer: render.SDL_Renderer, e_id: uuid.UUID) -> None:
        pass
