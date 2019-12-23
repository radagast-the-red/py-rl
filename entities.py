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


class Mob(Entity):
    """
    Mobile entity
    """

    def __init__(self, x, y, hp, name, char):
        super().__init__(x, y, hp)
        self.name = name
        self.char = char
