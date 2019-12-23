import entities


class ZoneHandler:
    """
    This class keeps information about the current zone
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
