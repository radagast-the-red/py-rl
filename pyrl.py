from asciimatics.screen import Screen
import entities
import gen
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
    # init everything

    el = entities.EntityLoader()
    hg = gen.HiveGenerate("stone_wall", "stone_floor")
    zh = hg.gen(30, 51, 51, 8, 4, 8, 4)

    player = el.load_entity("player", "mob")
    zh.set(2, 2, player)

    zh.draw_zone(screen)
    time.sleep(700)


Screen.wrapper(main_loop)
