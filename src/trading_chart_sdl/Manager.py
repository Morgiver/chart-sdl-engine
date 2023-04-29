import uuid
from trading_chart_sdl.Components import Component

class EntityManager:
    """
    Managing all entities and components

    Able to add, return and verify components in entities
    """
    def __init__(self):
        self.entities = {}
        self.components = {}
        self.specials = {}

    def create_entity(self) -> uuid.UUID:
        """
        Create a new entity uuid

        Returns:
            e_id (UUID): The new entity UUID
        """
        e_id = uuid.uuid4()
        self.entities[e_id] = {}
        return e_id

    def register_special(self, e_id: uuid.UUID, name: str) -> None:
        """
        Register an entity to be considered "special". That means this entity
        will be accessible faster. It is used to register device like mouse or
        keyboard.

        Parameters:
            e_id (UUID): Entity UUID
            name  (str): Name of the special entity
        """
        if name not in self.specials:
            self.specials[name] = e_id

    def has_special(self, name: str) -> bool:
        """
        Check if there's a named special entity in specials dict

        Parameters:
            name (str): The name of special entity
        """
        return name in self.specials

    def get_special(self, name: str):
        """
        Get a special entity by it's name

        Parameters:
            name (str): The name of special entity

        Returns:
            entity (UUID): The entity UUID
        """
        if name in self.specials:
            return self.specials[name]

    def add_component(self, e_id: uuid.UUID, component_type: str, component: Component) -> None:
        """
        Add a Component to a specifyied Entity

        Parameters:
            e_id           (UUID): Entity UUID
            component_type  (str): Type of the component
            component (Component): The component
        """
        if component_type not in self.components:
            self.components[component_type] = {}

        self.components[component_type][e_id] = component
        self.entities[e_id][component_type] = {}

    def remove_component(self, e_id: uuid.UUID, component_type):
        """
        Removing a component from it's entity

        Parameters:
            e_id           (UUID): Entity UUID
            component_type  (str): Type of the component
        """
        if component_type not in self.components:
            self.components[component_type] = {}
            return

        del self.components[component_type][e_id]
        del self.entities[e_id][component_type]

    def get_component(self, e_id: uuid.UUID, component_type: str) -> Component:
        """
        Get a Component from an entity

        Parameters:
            e_id           (UUID): Entity UUID
            component (Component): The component

        Returns:
            component (Component): The specifyied Component
        """
        if component_type not in self.components:
            return None

        return self.components[component_type].get(e_id, None)

    def has_component(self, e_id: uuid.UUID, component_type: str) -> bool:
        """
        Verifying if the Entity has a specifyied Component

        Parameters:
            e_id           (UUID): Entity UUID
            component (Component): The component

        Returns:
            has_component (bool): has or not the specifiyed Component
        """
        return component_type in self.components and e_id in self.components[component_type]
