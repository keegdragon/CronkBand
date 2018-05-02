import gametools
import gameview
import pygame
pygame.init()

event_dir_dict = {pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1), pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0)}

def take_turn(encounter, event_kind, event):
    if event_kind == "movement":
        if not encounter.actor_at(encounter.atlas["player_1"][0] + event_dir_dict[event.key][0], \
                                encounter.atlas["player_1"][1] + event_dir_dict[event.key][1]):
            move(encounter, "player_1", event)
        else:
            pass # "bump" goes here

def move(encounter, mover_name, event):
    encounter.move_character(mover_name, \
        [encounter.atlas[mover_name][0] + event_dir_dict[event.key][0], \
         encounter.atlas[mover_name][1] + event_dir_dict[event.key][1]])

def init_encounter():
    sample_boy = gametools.Character("Thadd")
    encounter = gametools.Encounter([10,10], {}, {}, {})
    encounter.add_character(sample_boy, [5,5], "player_1", "@")
    return encounter

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
