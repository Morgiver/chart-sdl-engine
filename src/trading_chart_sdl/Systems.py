import uuid
import ctypes
from sdl2 import *
from src.trading_chart_sdl.Manager import EntityManager
from src.trading_chart_sdl.Components import *

class System:
    """ Defining the System Type """
    pass

class RenderSystem(System):
    """
    Render System is used to render every entity if they are Drawable
    """
    @staticmethod
    def clear(renderer: render.SDL_Renderer) -> None:
        """
        Clearing the global renderer with a background color

        Paramerters:
            renderer (SDL_Renderer): The Renderer to clear
        """
        SDL_RenderPresent(renderer)
        SDL_SetRenderDrawColor(
            renderer,
            0, #self.bg_color.r,
            0, #self.bg_color.g,
            0, #self.bg_color.b,
            255, #self.bg_color.a
        )
        SDL_RenderClear(renderer)

    @staticmethod
    def update(em: EntityManager, renderer: render.SDL_Renderer, e_id: uuid.UUID) -> None:
        """
        Update the rendering surface

        Parameters:
            em      (EntityManager): The entity manager
            renderer (SDL_Renderer): The rendering surface
            e_id             (UUID): The unique id of entity
        """
        if em.has_component(e_id, "drawable"):
            if em.has_component(e_id, "shape"):
                RenderSystem.line(em, renderer, e_id)
            if em.has_component(e_id, "shape"):
                RenderSystem.rect(em, renderer, e_id)

    @staticmethod
    def line(em: EntityManager, renderer: render.SDL_Renderer, e_id: uuid.UUID) -> None:
        """
        Draw a Line

        Parameters:
            em      (EntityManager): The entity manager
            renderer (SDL_Renderer): The rendering surface
            e_id             (UUID): The unique id of entity
        """
        vector_component = em.get_component(e_id, "vector")
        color_component = em.get_component(e_id, "color")

        if not vector_component or not color_component or len(vector_component.coordinates) != 2:
            return

        a = PositionComponent(*vector_component.coordinates[0])
        b = PositionComponent(*vector_component.coordinates[1])
        c = color_component

        SDL_SetRenderDrawColor(renderer, c.r, c.g, c.b, c.a)
        SDL_RenderDrawLine(renderer, a.x, a.y, b.x, b.y)

    @staticmethod
    def rect(em: EntityManager, renderer: render.SDL_Renderer, e_id: uuid.UUID) -> None:
        """
        Draw a Rectangle

        Parameters:
            em      (EntityManager): The entity manager
            renderer (SDL_Renderer): The rendering surface
            e_id             (UUID): The unique id of entity
        """
        size_component = em.get_component(e_id, "size")
        color_component = em.get_component(e_id, "color")
        position_component = em.get_component(e_id, "position")

        if not size_component or not color_component or not position_component:
            return

        SDL_SetRenderDrawColor(renderer,
            color_component.r,
            color_component.g,
            color_component.b,
            color_component.a
        )

        SDL_RenderDrawRect(renderer, SDL_Rect(
            position_component.x,
            position_component.y,
            size_component.width,
            size_component.height
        ))
