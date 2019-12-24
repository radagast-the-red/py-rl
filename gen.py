import random
import entities
import zonehandler

"""
Shamelessly stolen from GeeksForGeeks.org!!
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


"""
Also stolen. Credit goes to Vivek Kumar Singh
"""


def rect_overlap(l1, r1, l2, r2):
    # If one rectangle is on left side of other
    if l1.x > r2.x or l2.x > r1.x:
        return False
    # If one rectangle is above other
    if l1.y < r2.y or l2.y < r1.y:
        return False
    return True


class HiveRoom:
    def __init__(self, x, y, h, w):
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def intersects(self, r):
        # check if this room intersects with room 'r'
        return rect_overlap(Point(self.x, self.y), Point(self.x + self.w, self.y + self.h), Point(r.x, r.y),
                            Point(r.x + r.w, r.y + r.h))


class HiveGenerate:
    """
    Generates a maze-like environment with many rooms
    Returns a newly constructed ZoneHandler
    """

    def __init__(self, wall_tag, floor_tag):
        el = entities.EntityLoader()
        self.wall = el.load_entity(wall_tag, "terrain")
        self.floor = el.load_entity(floor_tag, "floor")

    # TODO: Add more generation parameters
    def gen(self, attempts, h, w, max_rh, min_rh, max_rw, min_rw):
        # create new zone
        zh = zonehandler.ZoneHandler(h, w)
        rooms = []
        """
        # attempt to generate as many rooms as possible
        for x in range(0, attempts):
            new_room_x = random.randint(0, w)
            new_room_y = random.randint(0, h)
            new_room_h = random.randint(min_rh, max_rh)
            new_room_w = random.randint(min_rw, max_rw)
            new_room = HiveRoom(new_room_x, new_room_y, new_room_h, new_room_w)
            # check if the room intersects
            bad_room = False
            for r in rooms:
                if new_room.intersects(r):
                    # this is a bad room
                    bad_room = True
            # make sure the room is not OOB
            if (new_room_x + new_room_w) > w or (new_room_y + new_room_h) > h:
                continue
            # first room added regardless
            if x == 0:
                rooms.append(new_room)
        # writen rooms to zone
        print('test')
        """
        rooms.append(HiveRoom(5, 5, 6, 6))
        for r in rooms:
            # create floors
            for floor_y in range(r.y, r.y + r.h+1):
                for floor_x in range(r.x, r.x + r.w+1):
                    zh.set(floor_x, floor_y, self.floor)
            # create walls - this overwrites the flooring where necessary
            for wall_y in range(r.y, r.y + r.h+1):
                # top, bottom walls
                if wall_y == r.y or wall_y == r.y + r.h:
                    for wall_x in range(r.x, r.x + r.w+1):
                        zh.set(wall_x, wall_y, self.wall)
                else:
                    # other walls
                    zh.set(r.x, wall_y, self.wall)
                    zh.set(r.x + r.w, wall_y, self.wall)
        # return a zone handler for the newly generated zone
        return zh
