import gametools
import gameview
import pygame
pygame.init()

def init_world():
    sample_boy = gametools.Character("Thadd")
    world = gametools.Encounter([10,10], {}, {}, {})
    world.add_character(sample_boy, [5,5], "boy", "@")
    return world

def move(env, mover_name, direction):
    if direction == "u":
        env.move_character(mover_name, [env.atlas[mover_name][0], env.atlas[mover_name][1]-1])
    elif direction == "d":
        env.move_character(mover_name, [env.atlas[mover_name][0], env.atlas[mover_name][1]+1])
    elif direction == "l":
        env.move_character(mover_name, [env.atlas[mover_name][0] - 1, env.atlas[mover_name][1]])
    elif direction == "r":
        env.move_character(mover_name, [env.atlas[mover_name][0] + 1, env.atlas[mover_name][1]])


if __name__ == '__main__':
    test_window = gameview.GameView(1024, 768)
    pygame.event.set_blocked(pygame.ACTIVEEVENT)
    pygame.event.set_blocked(pygame.VIDEORESIZE)
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    world = init_world()

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    test_window.draw("Space bar pressed down.")
                elif event.key == pygame.K_z:
                    test_window.draw("Z key pressed down.")
                elif event.key == pygame.K_q:
                    test_window.drawScreen(world.make_drawable())
                elif event.key == pygame.K_UP:
                    move(world,"boy","u")
                    test_window.drawScreen(world.make_drawable())
                elif event.key == pygame.K_LEFT:
                    move(world, "boy", "l")
                    test_window.drawScreen(world.make_drawable())
                elif event.key == pygame.K_RIGHT:
                    move(world, "boy", "r")
                    test_window.drawScreen(world.make_drawable())
                elif event.key == pygame.K_DOWN:
                    move(world, "boy", "d")
                    test_window.drawScreen(world.make_drawable())
                elif event.key == pygame.K_ESCAPE:
                    game_over = True



