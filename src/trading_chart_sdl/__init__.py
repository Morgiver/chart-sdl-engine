import uuid
import ctypes
from types import *
from sdl2 import *

from trading_chart_sdl.Managers import *
from trading_chart_sdl.Components import *
from trading_chart_sdl.Systems import *

class SDLEngine:
    def __init__(self, w: int = 500, h: int = 500) -> None:
        """
        Initialization

        Parameters:
            w (int): The width of the Window
            h (int): The height of the Window
        """
        self.window   = None
        self.renderer = None
        self.events   = None
        self.title    = b"SDL Chart"
        self.width    = w
        self.height   = h
        self.em       = EntityManager()
        self.scene    = SceneManager()
        self.systems  = []

    def register_special(self, e_id: uuid.UUID, name: str) -> None:
        """ alias of EntityManager.register_special() """
        self.em.register_special(e_id, name)

    def get_special(self, name: str) -> uuid.UUID:
        """ alias of EntityManager.get_special() """
        return self.em.get_special(name)

    def has_special(self, name: str) -> bool:
        """ alias of EntityManager.has_special() """
        return self.em.has_special(name)

    def add_system(self, system: System):
        """ Adding a System to the SDLChart"""
        if system not in self.systems:
            self.systems.append(system)

        return self

    def create_entity(self) -> uuid.UUID:
        """ alias of EntityManager.create_entity() """
        return self.em.create_entity()

    def add_component(self, e_id: uuid.UUID, component_type: str, component: Component):
        """ alias of EntityManager.add_component() """
        self.em.add_component(e_id, component_type, component)
        return self

    def get_component(self, e_id: uuid.UUID, component_type: str) -> Component:
        """ alias of EntityManager.get_component() """
        return self.em.get_component(e_id, component_type)

    def has_component(self, e_id: uuid.UUID, component_type: str) -> bool:
        """ alias of EntityManager.has_component() """
        return self.em.has_component(e_id, component_type)

    def remove_component(self, e_id: uuid.UUID, component_type):
        """ alias of EntityManager.remove_component() """
        self.em.remove_component(e_id, component_type)
        return self

    def initialize(self, pointer: int | NoneType = None) -> None:
        """
        Initialize the window and the global renderer

        Parameters:
            pointer (int | NoneType): Pointer of an eventual existing window where we want
                           to integrate our Window
        """
        SDL_Init(SDL_INIT_VIDEO)

        if pointer:
            self.window = self.integrate_window(pointer)
        else:
            self.window = self.create_window()

        self.renderer = SDL_CreateRenderer(self.window, -1, 0)
        self.events = SDL_Event()

    def integrate_window(self, pointer: int):
        """
        Create a window from a parent window (like with Tkinter)

        Parameters:
            pointer (int | NoneType): Pointer of an eventual existing window where we want
                           to integrate our Window
        """
        return SDL_CreateWindowFrom(pointer)

    def create_window(self) -> SDL_Window:
        """
        Create a new window with the SDL2 library

        Returns:
            window (SDL_Window): The new window
        """
        return SDL_CreateWindow(
            self.title,
            SDL_WINDOWPOS_CENTERED,
            SDL_WINDOWPOS_CENTERED,
            self.width,
            self.height,
            SDL_WINDOW_SHOWN
        )

    def process_inputs(self) -> None:
        """
        Processing all SDL_Event
        """
        mouse_events = [SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP, SDL_MOUSEWHEEL]
        keyboard_events = [SDL_KEYUP, SDL_KEYDOWN]

        while SDL_PollEvent(ctypes.byref(self.events)) != 0:
            if self.events.type == SDL_QUIT:
                self.destroy()
                return False

            if self.events.type in mouse_events:
                MouseSystem.process_inputs(self.em, self.event)

        return True

    def update_logic(self):
        pass

    def collisions(self):
        pass

    def render(self):
        pass

    def cleanup(self):
        pass

    def destroy(self) -> None:
        """
        Destroying instances of renderer and window
        """
        SDL_DestroyRenderer(self.renderer)
        SDL_DestroyWindow(self.window)

    def quit_sdl(self) -> None:
        """
        Closing the SDL
        """
        SDL_Quit()

    def step(self) -> bool:
        is_running = self.process_inputs()
        self.update_logic()
        self.collisions()
        self.render()
        self.cleanup()

        return is_running
