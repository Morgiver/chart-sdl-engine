# Trading Chart SDL

This package will provide an API to render trading charts and give some graphics tools to do technical analysis using the SDL2 (Simple DirectMedia Layer).
It will provide access to tools created to collect data for training artificial intelligence as well.

## Actual State : Iteration 0 [IN DEV] (see [historic for past iterations](https://github.com/Morgiver/trading-chart-sdl/blob/main/iterations.md))

#### Objectives for this iterations :
1. Be capable to show different zones on the screen : Graphics zone, scale x and y zones.
2. Be capable to change the time and price scale with scales zones.
3. Be capable to show a simple price line with simple price data.
4. Be capable to create simple lines and manage them in the graphics zone.

# TODO List :
0. Make Unit Test for all code producted (try to do it with SDL2)
1. ~~Define RenderSystem class~~
2. ~~Define EntityManager class~~
3. ~~Update SDLChart class~~
4. ~~Define Components Position, Size, Shape, Drawable, Vector, Color~~
5. ~~Create a viewable test in test.py drawing two line and a rectangle~~
6. ~~Commenting code from previous TODO~~
7. Define different Component to be able to set different mouse state on the entity
8. ~~Define MouseSystem class to handle actions with the mouse~~
9. Define Scene class to be able to create multiple scene on the screen
10. Define EventSystem to handle all events

# Note about iteration 0:
Many many things to handle, working with SDL2 need more work than a thought.
I have created an ECS from scratch to be more free to move in the future, I prefere to fully control the tech.
The objectives were one step too far I think. The real objective was to build a basic ECS.
