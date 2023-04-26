import random
import time
from src.trading_chart_sdl import *

if __name__ == "__main__":
    c = SDLChart()

    c.add_system(RenderSystem)

    line_entity = c.create_entity()
    c.add_component(line_entity, "drawable", DrawableComponent())
    c.add_component(line_entity, "shape", ShapeComponent("line"))
    c.add_component(line_entity, "vector", VectorComponent(
        [
            (random.randint(100, 400), random.randint(100, 400)),
            (random.randint(100, 400), random.randint(100, 400))
        ]
    ))
    c.add_component(line_entity, "color", ColorComponent(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        255
    ))

    line_entity_two = c.create_entity()
    c.add_component(line_entity_two, "drawable", DrawableComponent())
    c.add_component(line_entity_two, "shape", ShapeComponent("line"))
    c.add_component(line_entity_two, "vector", VectorComponent(
        [
            (random.randint(100, 400), random.randint(100, 400)),
            (random.randint(100, 400), random.randint(100, 400))
        ]
    ))
    c.add_component(line_entity_two, "color", ColorComponent(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        255
    ))

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

    c.initialize()

    while c.step():
        pass
