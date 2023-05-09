from chart_sdl_engine.Systems.Base import *

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
        """
        Event on motion, when the mouse is moving

        Parameters:
            em           (EntityManager): The entity manager
            event (SDL_MouseMotionEvent): The sended event
        """
        e_id = em.get_special("mouse")

        if e_id is not None:
            pos = em.get_component(e_id, "position")
            pos.x = ctypes.c_int(event.x)
            pos.y = ctypes.c_int(event.y)

            print(f"X : {event.x} | Y: {event.y} | relative X : {event.xrel} | relative Y : {event.yrel}")

    @staticmethod
    def on_button_down(em: EntityManager, event) -> None:
        """
        On Button Down event

        Parameters:
            em           (EntityManager): The entity manager
            event (SDL_MouseButtonEvent): The sended event
        """
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
        """
        On Button Up event

        Parameters:
            em           (EntityManager): The entity manager
            event (SDL_MouseButtonEvent): The sended event
        """
        e_id = em.get_special("mouse")

        if e_id is not None:
            if event.button == SDL_BUTTON_LEFT:
                if em.has_component(e_id, "OnLeftButtonUpEvent"):
                    em.get_component(e_id, "OnLeftButtonUpEvent").callback(em, e_id, event.x, event.y)

            if event.button == SDL_BUTTON_RIGHT:
                print(f"Button Up : {SDL_BUTTON_RIGHT}")

            if event.button == SDL_BUTTON_MIDDLE:
                print(f"Button Up : {SDL_BUTTON_MIDDLE}")

    @staticmethod
    def on_wheel(em: EntityManager, event) -> None:
        """
        On Mouse Wheel event

        Parameters:
            em          (EntityManager): The entity manager
            event (SDL_MouseWheelEvent): The sended event
        """
        print("Wheeling")

    @staticmethod
    def process_inputs(em: EntityManager, event: SDL_Event) -> None:
        if event.type == SDL_MOUSEMOTION:
            MouseSystem.on_motion(em, event.motion)

        if event.type == SDL_MOUSEBUTTONDOWN:
            MouseSystem.on_button_down(em, event.button)

        if event.type == SDL_MOUSEBUTTONUP:
            MouseSystem.on_button_up(em, event.button)

        if event.type == SDL_MOUSEWHEEL:
            MouseSystem.on_wheel(em, event.wheel)
