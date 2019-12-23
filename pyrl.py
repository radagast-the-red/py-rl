from asciimatics.screen import Screen
import entities
import zonehandler
import time

"""

v0.1

initializing
- create the player mob



game loop
IF THE PLAYER IS DOING SOMETHING
- Simulate all entities
- Count down player action time
IF THE PLAYER IS DONE WITH AN ACT
- reflect the player's action
- draw stuff
- prompt for a new act


"""


def main_loop(screen):

    el = entities.EntityLoader()
    zh = zonehandler.ZoneHandler(20, 20, "Gorgo")

    player = el.load_entity("player", "mob")
    zh.set(1, 0, player)

    zh.draw_zone(screen)
    time.sleep(700)

Screen.wrapper(main_loop)
