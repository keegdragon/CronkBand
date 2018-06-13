import gametools
import gameview
import pygame
from random import *
pygame.init()

event_dir_dict = {pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1),
                  pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0)}


def pile_game(encounter):
    for actor in encounter.people:
        if type(actor) is gametools.Pile:
            return
    sample_stuff = gametools.Pile(gametools.Item("Coin", 0.1,
                                                 "A gold coin", 1))
    encounter.add_character(sample_stuff, [randint(0, 9), randint(0, 9)])
    return


def pc_actions(encounter, event_kind, event):
    encounter.player_to_front("Rupert")
    player = encounter.people[0]
    if event_kind == "movement":
        move_to_x = (encounter.atlas[player.name][0]
                     + event_dir_dict[event.key][0])
        move_to_y = (encounter.atlas[player.name][1]
                     + event_dir_dict[event.key][1])
        if (move_to_x < len(encounter.game_board)
                and move_to_y < len(encounter.game_board[0])):
            neighbor = encounter.game_board[move_to_x][move_to_y]
            if neighbor is None:
                move(encounter, player, event)
            else:
                if not neighbor.bump(player):
                    encounter.remove_character(neighbor)
                    move(encounter, player, event)
        else:
            print('(' + str(move_to_x) + ', ' + str(move_to_y)
                  + ') is outside the game board.')


def npc_actions(encounter):
    pile_game(encounter)


def move(encounter, mover, event):
    encounter.move_character(mover,
                             [encounter.atlas[mover.name][0]
                              + event_dir_dict[event.key][0],
                              encounter.atlas[mover.name][1]
                              + event_dir_dict[event.key][1]])


def init_encounter():
    sample_boy = gametools.Character("Rupert", '@')
    sample_stuff = gametools.Pile(gametools.Item("Coin", 0.1, "A gold coin", 2))
    encounter = gametools.Encounter([10, 10])
    encounter.add_character(sample_boy, [5, 5])
    encounter.add_character(sample_stuff, [7, 7])
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
                elif (event.key == pygame.K_UP
                      or event.key == pygame.K_DOWN
                      or event.key == pygame.K_LEFT
                      or event.key == pygame.K_RIGHT):
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
