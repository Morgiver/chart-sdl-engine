import uuid
import ctypes
from sdl2 import *
from src.trading_chart_sdl.Manager import EntityManager
from src.trading_chart_sdl.Components import *

class System:
    """ Defining the System Type """
    @staticmethod
    def update(em: EntityManager, renderer: render.SDL_Renderer, e_id: uuid.UUID) -> None:
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
        a = em.get_component(e_id, "point_a")
        b = em.get_component(e_id, "point_b")
        c = em.get_component(e_id, "color")

        if not a or not b or not c:
            return

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
        fillrect_component = em.get_component(e_id, "fillrect")

        if not size_component or not color_component or not position_component:
            return

        rect = SDL_Rect(
            position_component.x,
            position_component.y,
            size_component.width,
            size_component.height
        )

        if not fillrect_component:
            SDL_SetRenderDrawColor(renderer,
                color_component.r,
                color_component.g,
                color_component.b,
                color_component.a
            )
            SDL_RenderDrawRect(renderer, rect)
        else:
            SDL_SetRenderDrawColor(renderer,
                fillrect_component.r,
                fillrect_component.g,
                fillrect_component.b,
                fillrect_component.a
            )
            SDL_RenderFillRect(renderer, rect)

class MouseSystem(System):
    @staticmethod
    def update(em: EntityManager, renderer: render.SDL_Renderer, e_id: uuid.UUID) -> None:
        """
        Update the Mouse State and process Mouse actions

        Parameters:
            em      (EntityManager): The entity manager
            renderer (SDL_Renderer): The rendering surface
            e_id             (UUID): The unique id of entity
        """
        if em.has_special("mouse"):
            if em.has_component(e_id, "mouse-attach"):
                mouse = em.get_special("mouse")
                pos = em.get_component(mouse, "position")
                attach = em.get_component(e_id, "mouse-attach")
                attach.update(pos.x, pos.y)
                point = em.get_component(e_id, attach.point_name)
                point.x = attach.x
                point.y = attach.y

    @staticmethod
    def on_motion(em: EntityManager, event) -> None:
        e_id = em.get_special("mouse")

        if e_id is not None:
            pos = em.get_component(e_id, "position")
            pos.x = ctypes.c_int(event.x)
            pos.y = ctypes.c_int(event.y)

            print(f"X : {event.x} | Y: {event.y} | relative X : {event.xrel} | relative Y : {event.yrel}")

    @staticmethod
    def on_button_down(em: EntityManager, event) -> None:
        e_id = em.get_special("mouse")

        if e_id is not None:
            if event.button == SDL_BUTTON_LEFT:
                print(f"Button Down : {SDL_BUTTON_LEFT}")

            if event.button == SDL_BUTTON_RIGHT:
                print(f"Button Down : {SDL_BUTTON_RIGHT}")

            if event.button == SDL_BUTTON_MIDDLE:
                print(f"Button Down : {SDL_BUTTON_MIDDLE}")

    @staticmethod
    def on_button_up(em: EntityManager, event) -> None:
        e_id = em.get_special("mouse")

        if e_id is not None:
            if event.button == SDL_BUTTON_LEFT:
                print(f"Button Up : {SDL_BUTTON_LEFT}")

            if event.button == SDL_BUTTON_RIGHT:
                print(f"Button Up : {SDL_BUTTON_RIGHT}")

            if event.button == SDL_BUTTON_MIDDLE:
                print(f"Button Up : {SDL_BUTTON_MIDDLE}")

    @staticmethod
    def on_wheel(em: EntityManager) -> None:
        print("Wheeling")

class EventSystem(System):
    @staticmethod
    def update(em: EntityManager, renderer: render.SDL_Renderer, e_id: uuid.UUID):
        pass
