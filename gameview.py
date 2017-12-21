import pygame
pygame.init()

class GameView:
    """Describes the game's display window"""

    #TODO: Designate width and height in terms of unispace font
    def __init__(self, width=320, height=240):
        """Width and height specified at initialization"""
        self.size = width, height

    def openWindow(self):
        """Opens window of designated size; returns window object"""
        return pygame.display.set_mode(self.size)

    def draw(self, env):
        pass