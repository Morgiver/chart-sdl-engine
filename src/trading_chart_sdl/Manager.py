import uuid
from src.trading_chart_sdl.Components import Component

class EntityManager:
    """
    Managing all entities and components

    Able to add, return and verify components in entities
    """
    def __init__(self):
        self.entities = {}
        self.components = {}

    def create_entity(self) -> uuid.UUID:
        """
        Create a new entity uuid

        Returns:
            e_id (UUID): The new entity UUID
        """
        e_id = uuid.uuid4()
        self.entities[e_id] = set()
        return e_id

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
        self.entities[e_id].add(component_type)

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
