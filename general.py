import pygame
import sys
from pygame.color import THECOLORS
import math
from x_or_o import Ui_MainWindow
from PyQt5 import QtWidgets

pygame.init

class General():
    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.loc = None
        self.loc1start = None
        self.loc1end = None
        self.loc2start = None
        self.loc2end = None
        self.button_event()
        
    game_over = False
    height = 300
    width = 300
    grid = 3
    size = math.ceil((width * 0.02) / ((grid) / 2))
    screen = pygame.display.set_mode((width, height))


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
    

    def start(self):
        General.field()
        arr = []
        General.game_over = False
        Box.x = True
        for i in range(General.grid):
            arr2 = []
            for j in range(self.grid):
                arr2.append(Box())
            arr.append(arr2)
        
        while not General.game_over:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(self.grid):
                        for j in range(self.grid):
                            data = self.location1(event, i + 1, j + 1)
                            if data is not None:
                                arr[i][j].check(*data)
                    self.win_or_lose(arr)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.flip()

        self.start()
    
    
    def win_or_lose(self, arr):
        s = 0
        for i in arr:
            if all(tuple(j.memory == 1 for j in i )):
                print('win o') 
                General.game_over = True      
            elif all(tuple(j.memory == 2 for j in i )):
                print('win x') 
                General.game_over = True
        for j in range(General.grid):
            for i in range(General.grid):
                if all(tuple(arr[i] [j].memory == 1 for i in range(General.grid))):
                    print('win o') 
                    General.game_over = True      
                elif all(tuple(arr[i] [j].memory == 2 for i in range(General.grid))):
                    print('win x') 
                    General.game_over = True

        if all(arr[j][j].memory == 1 for j in range(General.grid)):
                print('o win')
                General.game_over = True 
        elif all(arr[j][j].memory == 2 for j in range(General.grid)):
                print('x win')    
                General.game_over = True
        if all(arr[j][General.grid - 1 - j].memory == 1 for j in range(General.grid)):
                print('o win')
                General.game_over = True
        elif all(arr[j][General.grid - 1 - j].memory == 2 for j in range(General.grid)):
                print('x win')
                General.game_over = True
        for i in range(General.grid):
            for j in range(General.grid):
                if arr[i] [j].memory > 0 :
                    s += 1
                    if s == self.grid ** 2:
                        print("nothink")
    
                        General.game_over = True

    def button_event(self):
        pass 

    @staticmethod
    def field():
        General.screen.fill(THECOLORS['white'])
        for i in range(1, General.grid):
            pygame.draw.line(General.screen, THECOLORS['black'], ((i / General.grid * General.width, 0)),((i / General.grid * General.width, General.height)), General.size)  
            pygame.draw.line(General.screen, THECOLORS['black'], ((0, i / General.grid * General.height)),((General.width, i / General.grid * General.height)), General.size)     


class Box():

    def __init__(self):
        self.incorrect = False
        self.memory = 0 
    x = True

    def x_or_o(self, loc, loc1start, loc1end, loc2start, loc2end):
        Box.x = not Box.x
        if Box.x:
            self.figure_1(loc)
            self.memory = 1
        else:
            self.figure_2(loc1start, loc1end, loc2start, loc2end)
            self.memory = 2
            

    def check(self, loc, loc1start, loc1end, loc2start, loc2end):
        if not self.incorrect:
            self.x_or_o(loc, loc1start, loc1end, loc2start, loc2end)
            self.incorrect = True
        else:
            print("---")
    
    def figure_1(self, loc):
        pygame.draw.circle(General.screen, THECOLORS["black"], loc, round(1 / (2.5 * General.grid) * min(General.height, General.width)),  General.size)
        
    def figure_2(self, loc1start, loc1end, loc2start, loc2end):
        pygame.draw.line(General.screen, THECOLORS["black"], loc1start, loc1end, General.size)
        pygame.draw.line(General.screen, THECOLORS["black"], loc2start, loc2end, General.size)  
    

if __name__ == "__main__":
    start = General()
    start.start()