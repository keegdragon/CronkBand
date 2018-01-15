import pygame
from pygame.event import Event, event_name, wait
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
        self.displaySurface.blit(ren, (10, 10))
        pygame.display.flip()


if __name__ == '__main__':
    testWindow = GameView(1024, 768)
    #testWindow.openWindow()
    testWindow.draw("hello world!")
    pygame.event.wait()
    testWindow.draw("you pressed a button!")
    pygame.event.wait()