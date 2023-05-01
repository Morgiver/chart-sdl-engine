from trading_chart_sdl.Systems.Base import *

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
                shape = em.get_component(e_id, "shape").name

                if hasattr(RenderSystem, shape):
                    fn = getattr(RenderSystem, shape, None)
                    if callable(fn):
                        fn(em, renderer, e_id)

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

        if not size_component or not color_component or not position_component:
            return

        rect = SDL_Rect(
            position_component.x,
            position_component.y,
            size_component.width,
            size_component.height
        )

        SDL_SetRenderDrawColor(renderer,
            color_component.r,
            color_component.g,
            color_component.b,
            color_component.a
        )
        SDL_RenderDrawRect(renderer, rect)

    @staticmethod
    def fillrect(em: EntityManager, renderer: render.SDL_Renderer, e_id: uuid.UUID) -> None:
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

        rect = SDL_Rect(
            position_component.x,
            position_component.y,
            size_component.width,
            size_component.height
        )

        SDL_SetRenderDrawColor(renderer,
            color_component.r,
            color_component.g,
            color_component.b,
            color_component.a
        )
        SDL_RenderFillRect(renderer, rect)
