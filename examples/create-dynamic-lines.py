import sys
import random
import time

sys.path.append('./src')

from trading_chart_sdl import *

if __name__ == "__main__":
    e = SDLEngine()

    lines = []

    e.add_system(MouseSystem)
    e.add_system(EventSystem)
    e.add_system(RenderSystem)

    def on_click(em, mouse, mouse_x, mouse_y):
        state = em.get_component(mouse, "mouse-state")

        if state.mode == "cursor":
            entity = em.create_entity()
            em.add_component(entity, "drawable", DrawableComponent())
            em.add_component(entity, "shape", ShapeComponent("line"))
            em.add_component(entity, "point_a", PositionComponent(mouse_x, mouse_y))
            em.add_component(entity, "point_b", PositionComponent(0,0))
            em.add_component(entity, "mouse-attach", MouseAttachComponent(0, 0, "point_b"))
            em.add_component(entity, "color", ColorComponent(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                255
            ))

            em.add_component(mouse, "mouse-state", MouseStateComponent(e_id=entity, mode="line-creation"))
            return None

        if state.mode == "line-creation":
            em.remove_component(state.entity, "mouse-attach")
            em.add_component(mouse, "mouse-state", MouseStateComponent())

            return None

    mouse = e.create_entity()
    e.register_special(mouse, "mouse")
    e.add_component(mouse, "position", PositionComponent(0, 0))
    e.add_component(mouse, "mouse-state", MouseStateComponent())
    e.add_component(mouse, "OnLeftButtonUpEvent", OnLeftButtonUpEvent(on_click))

    e.initialize()

    while e.step():
        pass
