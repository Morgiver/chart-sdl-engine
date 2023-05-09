from chart_sdl_engine.Managers.Entity import *

class GridManager:
    """
    Grid Manager manage Entities position in a grid, this
    """
    def __init__(self):
        self.grid = {}
        self.position_indexer = {}

    def update_position(self, em: EntityManager, e_id: uuid.UUID) -> None:
        """
        Updating the position of an Entity

        Parameters:
            em (EntityManager): Entity Manager
            e_id        (UUID): Unique ID of the Entity
        """

        x, y = em.get_component(e_id, "position")
        width, height = em.get_component(e_id, "space-size")

        """ Creating position value in the grid if needed to """
        if y not in self.grid:
            self.grid[y] = {}

        if x not in self.grid[y]:
            self.grid[y][x] = {}

        if y + height not in self.grid:
            self.grid[y + height] = {}

        if x + width not in self.grid[y]:
            self.grid[y][x + width] = {}

        if x not in self.grid[y + height]:
            self.grid[y + height][x] = {}

        if x + width not in self.grid[y + height]:
            self.grid[y + height][x + width] = {}

        """
        Checking if the Entity is already registred and verifying
        if the origin point position has changed or not.
        If the position has changed, deleting the actual position.
        """
        if e_id in self.position_indexer and (self.position_indexer[e_id]['o']['x'] != x or self.position_indexer[e_id]['o']['y'] != y):
            # e_id is already registred, deleting actual position
            self.remove_position(e_id)

        """ Updating the position of Entity """
        # Origin point : Upper Left Corner
        self.grid[y][x][e_id] = {}
        # Upper Right Corner
        self.grid[y][x + width][e_id] = {}
        # Lower Left Corner
        self.grid[y + height][x][e_id] = {}
        # Lower Right Corner
        self.grid[y + height][x + width][e_id] = {}


        """ Updating the indexer """
        self.position_indexer[e_id] = {
            'o': {'x': x, 'y': y},
            'ur': {'x': x + width, 'y': y},
            'll': {'x': x, 'y': y + height},
            'lr': {'x': x + width, 'y': y + height}
        }

    def remove_position(self, e_id: uuid.UUID) -> None:
        """
        Removing the entity position from the grid

        Parameters:
            e_id (UUID): Unique ID of the Entity
        """
        ent = self.position_indexer[e_id]

        del self.grid[ent['o']['y']][ent['o']['x']][e_id]
        del self.grid[ent['ur']['y']][ent['ur']['x']][e_id]
        del self.grid[ent['ll']['y']][ent['ll']['x']][e_id]
        del self.grid[ent['lr']['y']][ent['lr']['x']][e_id]

        # Removing Origin Corner X Position
        if len(self.grid[ent['o']['y']][ent['o']['x']]) < 1:
            del self.grid[ent['o']['y']][ent['o']['x']]

        # Removing Upper Right Corner X Position
        if len(self.grid[ent['ur']['y']][ent['ur']['x']]) < 1:
            del self.grid[ent['ur']['y']][ent['ur']['x']]

        # Removing Lower Left Corner X Position
        if len(self.grid[ent['ll']['y']][ent['ll']['x']]) < 1:
            del self.grid[ent['ll']['y']][ent['ll']['x']]

        # Removing Lower Right Corner X Position
        if len(self.grid[ent['lr']['y']][ent['lr']['x']]) < 1:
            del self.grid[ent['lr']['y']][ent['lr']['x']]

        # Removing Origin Y Position
        if len(self.grid[ent['o']['y']]) < 1:
            del self.grid[ent['o']['y']]

        # Removing Lower Left Corner Y Position
        if len(self.grid[ent['ll']['y']]) < 1:
            del self.grid[ent['ll']['y']]
