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
        self.font = pygame.font.Font(pygame.font.match_font("couriernew"), int(height / 40))

    def openWindow(self):
        """Opens window of designated size; returns window object"""
        return self.displaySurface

    def draw(self, env):
        ren = self.font.render(env, 0, (0,0,255), (0,0,0))
        self.displaySurface.blit(ren, (0, 0))
        pygame.display.flip()

    def drawScreen(self, env):
        self.displaySurface.fill(pygame.Color(0, 0, 0))
        yToRender = 0
        for line in env:
            ren = self.font.render(line, 0, (230,230,230), (0,0,0))
            self.displaySurface.blit(ren, (0, yToRender))
            pygame.display.flip()
            yToRender += int(self.size[1] / 40)