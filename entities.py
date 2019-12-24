import json


class Entity:
    """
    Basic entity class
    """

    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp


class Terrain(Entity):
    """
    Terrain entity
    """

    def __init__(self, x, y, hp, name, char):
        super().__init__(x, y, hp)
        self.name = name
        self.char = char


class Floor(Entity):
    """
    Floor entity
    """

    def __init__(self, x, y, hp, name, char):
        super().__init__(x, y, hp)
        self.name = name
        self.char = char


class Mob(Entity):
    """
    Mobile entity
    """

    def __init__(self, x, y, hp, name, char):
        super().__init__(x, y, hp)
        self.name = name
        self.char = char


class EntityLoader:
    """
    Used to load entity information from json
    """

    def __init__(self):
        # perform initialization, read from file
        with open("entities.json", "r") as entDataFile:
            self.entData = json.load(entDataFile)

    def load_entity(self, tag, o_type):
        obj = self.entData[o_type][tag]
        # different objects require different data
        if o_type == "mob":
            return Mob(0, 0, obj["stats"]["hp"], tag, obj["graphics"]["char"])
        if o_type == "terrain":
            return Terrain(0, 0, obj["stats"]["hp"], tag, obj["graphics"]["char"])
        if o_type == "floor":
            return Floor(0, 0, obj["stats"]["hp"], tag, obj["graphics"]["char"])
