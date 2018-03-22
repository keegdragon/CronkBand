import pygame
pygame.init()

class GameView:
    """Describes the game's display window"""

    #TODO: Designate width and height in terms of unispace font
    def __init__(self, width=320, height=240):
        """Width and height specified at initialization
        Setting mode opens window"""
        self.size = width, height
        self.displaySurface = pygame.display.set_mode(self.size)
        self.font = pygame.font.Font(None, 60)

    def openWindow(self):
        """Opens window of designated size; returns window object"""
        return self.displaySurface

    def draw(self, env):
        ren = self.font.render(env, 0, (0,0,255), (0,0,0))
        self.displaySurface.fill(pygame.Color(0,0,0))
        self.displaySurface.blit(ren, (10, 10))
        pygame.display.flip()


if __name__ == '__main__':
    testWindow = GameView(1024, 768)
    #testWindow.openWindow()
    game_over = False
    pygame.event.set_blocked(pygame.ACTIVEEVENT)
    pygame.event.set_blocked(pygame.VIDEORESIZE)
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    testWindow.draw("Space bar pressed down.")
                elif event.key == pygame.K_z:
                    testWindow.draw("Z key pressed down.")
                elif event.key == pygame.K_q:
                    testWindow.draw("")
                    my_rect = pygame.draw.rect(testWindow.displaySurface, pygame.Color(0,0,255), (10,10,10,10))
                    pygame.display.flip()
                elif event.key == pygame.K_UP:
                    testWindow.draw("")
                    my_rect = pygame.draw.rect(testWindow.displaySurface, pygame.Color(0, 0, 255), my_rect.move(0,-5))
                    pygame.display.flip()
                elif event.key == pygame.K_LEFT:
                    testWindow.draw("")
                    my_rect = pygame.draw.rect(testWindow.displaySurface, pygame.Color(0, 0, 255), my_rect.move(-5,0))
                    pygame.display.flip()
                elif event.key == pygame.K_RIGHT:
                    testWindow.draw("")
                    my_rect = pygame.draw.rect(testWindow.displaySurface, pygame.Color(0, 0, 255), my_rect.move(5, 0))
                    pygame.display.flip()
                elif event.key == pygame.K_DOWN:
                    testWindow.draw("")
                    my_rect = pygame.draw.rect(testWindow.displaySurface, pygame.Color(0, 0, 255), my_rect.move(0, 5))
                    pygame.display.flip()
                elif event.key == pygame.K_ESCAPE:
                    game_over = True