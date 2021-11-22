import math
import pygame
from pygame.color import THECOLORS


class Window():
    def __init__(self):
        self.height = 600
        self.width = 600
        self.grid = 3
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.size = math.ceil((self.width * 0.02) / ((self.grid) / 2))
        self.loc = None
        self.loc1start = None
        self.loc1end = None
        self.loc2start = None
        self.loc2end = None

    def location1(self, event, i, j):
        if (
            (i - 1) / self.grid * self.width < event.pos[0] < i / self.grid * self.width and 
            (j - 1) / self.grid * self.height < event.pos[1] < j / self.grid * self.height
        ):
            start_line_x = (i - 1)/ self.grid * self.width + 2 / 30 * (1 / self.grid * self.width)
            end_line_x = start_line_x + 26 / 30 * (1 / self.grid *self.width)
            start_line_y = (j - 1)/ self.grid * self.height + 2 / 30 * (1 / self.grid * self.height)
            end_line_y = start_line_y + 26 / 30 * (1 / self.grid * self.height)
            loc1start = (start_line_x, start_line_y) 
            loc1end = (end_line_x, end_line_y) 
            loc2start = (end_line_x, start_line_y) 
            loc2end = (start_line_x, end_line_y) 
            
            loc = (
                (i - 1)/ self.grid * self.width + 1 / 2 * (1 / self.grid * self.width), 
                (j - 1)/ self.grid * self.height + 1 / 2 * (1 / self.grid * self.height)
            )                       
            
            return loc, loc1start, loc1end, loc2start, loc2end


    def figure_1(self, loc):
        pygame.draw.circle(self.screen, THECOLORS["black"], loc, round(1 / (2.5 * self.grid) * min(self.height, self.width)),  self.size)
        
    def figure_2(self, loc1start, loc1end, loc2start, loc2end):
        pygame.draw.line(self.screen, THECOLORS["black"], loc1start, loc1end, self.size)
        pygame.draw.line(self.screen, THECOLORS["black"], loc2start, loc2end, self.size)
    
    def field(self):
        self.screen.fill(THECOLORS['white'])
        for i in range(1, self.grid):
            pygame.draw.line(self.screen, THECOLORS['black'], ((i / self.grid * self.width, 0)),((i / self.grid * self.width, self.height)), self.size)  
            pygame.draw.line(self.screen, THECOLORS['black'], ((0, i / self.grid * self.height)),((self.width, i / self.grid * self.height)), self.size)     


# screen_arg = Window()

