import sys
import random
import time

sys.path.append('./src')

from trading_chart_sdl import *

if __name__ == "__main__":
    c = SDLEngine()

    c.add_system(MouseSystem)
    c.add_system(EventSystem)
    c.add_system(RenderSystem)

    mouse = c.create_entity()
    c.register_special(mouse, "mouse")
    c.add_component(mouse, "position", PositionComponent(0, 0))

    line_entity = c.create_entity()
    c.add_component(line_entity, "drawable", DrawableComponent())
    c.add_component(line_entity, "shape", ShapeComponent("line"))
    c.add_component(line_entity, "point_a", PositionComponent(
        random.randint(100, 400),
        random.randint(100, 400))
    )
    c.add_component(line_entity, "point_b", PositionComponent(
        random.randint(100, 400),
        random.randint(100, 400))
    )
    c.add_component(line_entity, "color", ColorComponent(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        255
    ))

    line_entity_two = c.create_entity()
    c.add_component(line_entity_two, "drawable", DrawableComponent())
    c.add_component(line_entity_two, "shape", ShapeComponent("line"))
    c.add_component(line_entity_two, "point_a", PositionComponent(
        random.randint(100, 400),
        random.randint(100, 400))
    )
    c.add_component(line_entity_two, "point_b", PositionComponent(
        random.randint(100, 400),
        random.randint(100, 400))
    )
    c.add_component(line_entity_two, "color", ColorComponent(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        255
    ))

    line_entity_three = c.create_entity()
    c.add_component(line_entity_three, "drawable", DrawableComponent())
    c.add_component(line_entity_three, "shape", ShapeComponent("line"))
    c.add_component(line_entity_three, "point_a", PositionComponent(
        random.randint(100, 400),
        random.randint(100, 400))
    )
    c.add_component(line_entity_three, "point_b", PositionComponent(
        random.randint(100, 400),
        random.randint(100, 400))
    )
    c.add_component(line_entity_three, "color", ColorComponent(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        255
    ))
    c.add_component(line_entity_three, "mouse-attach", MouseAttachComponent(0, 0, "point_b"))

    rect_entity = c.create_entity()
    c.add_component(rect_entity, "drawable", DrawableComponent())
    c.add_component(rect_entity, "shape", ShapeComponent("rect"))
    c.add_component(rect_entity, "size", SizeComponent(50, 25))
    c.add_component(rect_entity, "position", PositionComponent(random.randint(100, 400), random.randint(100, 400)))
    c.add_component(rect_entity, "color", ColorComponent(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        255
    ))

    rect_entity_two = c.create_entity()
    c.add_component(rect_entity_two, "drawable", DrawableComponent())
    c.add_component(rect_entity_two, "shape", ShapeComponent("fillrect"))
    c.add_component(rect_entity_two, "size", SizeComponent(50, 25))
    c.add_component(rect_entity_two, "position", PositionComponent(random.randint(100, 400), random.randint(100, 400)))
    c.add_component(rect_entity_two, "color", ColorComponent(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        255
    ))
    c.add_component(rect_entity_two, "fillcolor", ColorComponent(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        255
    ))

    c.initialize()

    while c.step():
        pass
