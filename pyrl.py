from asciimatics.screen import Screen
import entities
import zonehandler
import time

"""

v0.1

- generate a simple map
- put down the player
- let the player walk around
- implement proper turn handling


"""


def draw_zone(screen, zone):
    x = zone.w
    y = zone.h
    # going row by row
    for i in range(0, y-1):
        # draw a row
        for j in range(0, x-1):
            obj = zone.get(j, i)
            screen.print_at(obj.char, j, i)
    screen.refresh()


def main_loop(screen):
    draw_zone(screen, zonehandler.ZoneHandler(20, 20, "Gorgos"))
    time.sleep(10)

Screen.wrapper(main_loop)
