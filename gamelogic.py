import gametools
import gameview
import pygame
from random import *
pygame.init()

event_dir_dict = {pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1), pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0)}

def pile_game(encounter):
    for actor in encounter.people.values():
        if type(actor) is gametools.Pile:
            return
    sample_stuff = gametools.Pile(gametools.Item("Hammer", 5, "It's a hammer", 1))
    encounter.add_character(sample_stuff, [randint(0,9), randint(0,9)], "loot_1", "$")
    return


def pc_actions(encounter, event_kind, event):
    if event_kind == "movement":
        neighbor_name = encounter.name_at(encounter.atlas["player_1"][0] + event_dir_dict[event.key][0], \
                           encounter.atlas["player_1"][1] + event_dir_dict[event.key][1])
        if not neighbor_name:
            move(encounter, "player_1", event)
        else:
            neighbor = encounter.people[neighbor_name]
            if not neighbor.bump(encounter.people["player_1"]):
                move(encounter, "player_1", event)
                encounter.remove_character(neighbor_name)

def npc_actions(encounter):
    pile_game(encounter)

def move(encounter, mover_name, event):
    encounter.move_character(mover_name, \
        [encounter.atlas[mover_name][0] + event_dir_dict[event.key][0], \
         encounter.atlas[mover_name][1] + event_dir_dict[event.key][1]])

def init_encounter():
    sample_boy = gametools.Character("Thadd")
    sample_stuff = gametools.Pile(gametools.Item("Hammer", 5, "It's a hammer", 1))
    encounter = gametools.Encounter([10,10], {}, {}, {})
    encounter.add_character(sample_boy, [5,5], "player_1", "@")
    encounter.add_character(sample_stuff, [7, 7], "loot_1", "$")
    return encounter

def take_turn(encounter, event_kind, event):
    pc_actions(encounter, event_kind, event)
    npc_actions(encounter)

# Listens for input and directs to auxiliary input processing functions
# game_loop may also prompt for additional input
def game_loop(test_window, encounter):
    test_window.drawScreen(encounter.make_drawable())

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    test_window.draw("Space bar pressed down.")
                elif event.key == pygame.K_UP or \
                    event.key == pygame.K_DOWN or \
                    event.key == pygame.K_LEFT or \
                    event.key == pygame.K_RIGHT:
                    take_turn(encounter, "movement", event)
                    test_window.drawScreen(encounter.make_drawable())
                elif event.key == pygame.K_ESCAPE:
                    game_over = True

if __name__ == '__main__':
    test_window = gameview.GameView(1024, 768)
    pygame.event.set_blocked(pygame.ACTIVEEVENT)
    pygame.event.set_blocked(pygame.VIDEORESIZE)
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    enc = init_encounter()

    game_loop(test_window, enc)
