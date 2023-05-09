from chart_sdl_engine.Managers.Entity import *

class Scene:
    def __init__(self, pos_x = 0, pos_y = 0, parent = None):
        self.parent = parent
        self.screen_origin = {'x': pos_x, 'y': pos_y}
        self.entities = {}
        self.layer_level = 0

    def attach(self, e_id: uuid.UUID) -> None:
        """
        Attaching an entity into the Scene

        Parameters:
            e_id (UUID): The Entity Unique ID
        """
        if e_id not in self.entities:
            self.entities[e_id] = {}

    def detach(self, e_id: uuid.UUID) -> None:
        if e_id in self.entities:
            del self.entities[e_id]

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.entities_indexer = {}

    def add_scene(self, name: str, scene: Scene) -> None:
        """
        Adding a Scene to the manager

        Parameters:
            name    (str): Name of the Scene
            scene (Scene): The scene
        """
        if name not in self.scenes:
            self.scenes[name] = scene

    def attach_to(self, name: str, e_id: uuid.UUID) -> None:
        """
        Attaching an Entity to a named Scene

        Parameters:
            name    (str): Name of the Scene
            scene (Scene): The scene

        Raising:
            1. Scene is not listed
            2. Entity is already attached in other Scene
        """
        if name not in self.scenes:
            raise Exception(f"Scene {name} is not listed")

        for scene in self.scenes:
            if scene != name and e_id in self.scenes[name].entities:
                raise Exception("Entity is already attached in other Scene")

        self.scenes[name].attach(e_id)
        self.entities_indexer[e_id] = name

    def detach_from(self, e_id: uuid.UUID) -> None:
        """
        Detach an Entity from a Scene

        Parameters:
            e_id (UUID): The Entity Unique ID
        """
        if e_id in self.entities_indexer:
            self.scenes[self.entities_indexer[e_id]].detach(e_id)

    def delete_scene(self, name: str) -> None:
        """
        Deleting a scene from the manager

        Parameters:
            name (str): Name of the Scene
        """
        if name in self.scenes:
            # Deleting every reference in indexer
            for e_id in self.scenes[name].entities:
                del self.entities_indexer[e_id]

            del self.scenes[name]
