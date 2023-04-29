# ITERATION 0
#### Objectives for this iterations :
1. Be capable to show different zones on the screen : Graphics zone, scale x and y zones.
2. Be capable to change the time and price scale with scales zones.
3. Be capable to show a simple price line with simple price data.
4. Be capable to create simple lines and manage them in the graphics zone.

## TODO List :
0. Make Unit Test for all code producted (try to do it with SDL2)
1. ~~Define RenderSystem class~~
2. ~~Define EntityManager class~~
3. ~~Update SDLChart class~~
4. ~~Define Components Position, Size, Shape, Drawable, Vector, Color~~
5. ~~Create a viewable test in test.py drawing two line and a rectangle~~
6. ~~Commenting code from previous TODO~~
7. ~~Define different Component to be able to set different mouse state on the entity~~
8. ~~Define MouseSystem class to handle actions with the mouse~~
9. Define Scene class to be able to create multiple scene on the screen
10. Define EventSystem to handle all events

## Note about iteration 0:
The iteration 0 brought a research and development time. I started with the idea that all objectives were reachable, but this was a mistake.
Nevertheless, I learned a lot and now I have a stable start, I will surely need to modify lot of things but I now better what I want and why.

I already work on a little ECS in the past, but in this work I was discovering many way to do it better.

#### What was the real objectives of this iteration ?
1. Build an Entity Manager to manage Entities and there Components.
2. Build multiple Components to increase Systems possibilities (shape, color, size, position, etc.).
3. Build a Render System to draw all shapes that I need (e.g. : include a ShapeComponent to know what I want to draw).
4. Build a Mouse System to handle Mouse motion and button events.
5. Build the SDLEngine around that to structure and manage all Systems and Entities.

#### What's next ?
There's many challenge :

1. Events handling is more complex than I already do. I need to build an EventSystem to handle all events modularly. In this part I have to know when to use the SDL Events and when to use the "update" method from the system.
2. Build a Collision detection system, first to now if the mouse is over an entity or not, after to be able to handle the detection between entities.
3. Build a WorldManager and a WorldSystem to place entities and now every time where they are.
4. Increase performance in Collision Detection with building a Quad Tree pattern and using the Culling optimization.
