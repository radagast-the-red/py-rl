import entities


class ZoneHandler:
    """
    This class keeps information about the current zone and helps draw it
    """
    zoneArray = []

    def __init__(self, h, w, default_terrain):
        self.h = h
        self.w = w
        for y in range(0, h):
            level = []
            for x in range(0, w):
                # TODO: add entity type loader using JSON
                level.append(entities.Terrain(x, y, 100, default_terrain, 'T'))
            self.zoneArray.append(level)

    def get(self, x, y):
        return self.zoneArray[x][y]

    def set(self, x, y, entity):
        self.zoneArray[x][y] = entity
        # as a backup, update the entity's new location
        entity.x = x
        entity.y = y

    def draw_zone(self, screen):
        x = self.w
        y = self.h
        # going row by row
        for i in range(0, y - 1):
            # draw a row
            for j in range(0, x - 1):
                obj = self.get(j, i)
                screen.print_at(obj.char, j, i)
        screen.refresh()
