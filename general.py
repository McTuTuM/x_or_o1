import pygame
import sys
from pygame.color import THECOLORS
import math
from x_or_o import Ui_MainWindow
from PyQt5 import QtWidgets


pygame.init
class ini(Ui_MainWindow, QtWidgets.QMainWindow):
    x = True
    def __init__(self):
        self.loc = None
        self.loc1start = None
        self.loc1end = None
        self.loc2start = None
        self.loc2end = None
        self.incorrect = False
        self.memory = 0 

    def x_or_o(self, loc, loc1start, loc1end, loc2start, loc2end):
        ini.x = not ini.x
        if ini.x:
            self.figure_1(loc)
            self.memory = 1
        else:
            self.figure_2(loc1start, loc1end, loc2start, loc2end)
            self.memory = 2
            

    def chek(self, loc, loc1start, loc1end, loc2start, loc2end):
        if not self.incorrect:
            self.x_or_o(loc, loc1start, loc1end, loc2start, loc2end)
            self.incorrect = True
        else:
            print("---")

    @staticmethod
    def figure_1(loc):
        pygame.draw.circle(window.screen, THECOLORS["black"], loc, round(1 / (2.5 * window.grid) * min(window.height, window.width)),  window.size)

    @staticmethod
    def figure_2(loc1start, loc1end, loc2start, loc2end):
        pygame.draw.line(window.screen, THECOLORS["black"], loc1start, loc1end,  window.size)
        pygame.draw.line(window.screen, THECOLORS["black"], loc2start, loc2end,  window.size)
    

class window:

    height = 600
    width = 1200
    game_over = False
    grid = 3
    size = math.ceil((width * 0.02) / ((grid) / 2))
    @staticmethod
    def location1(event, i, j):
        if (
            (i - 1) / window.grid * window.width < event.pos[0] < i / window.grid * window.width and 
            (j - 1) / window.grid * window.height < event.pos[1] < j / window.grid * window.height
        ):
            start_line_x = (i - 1)/ window.grid * window.width + 2 / 30 * (1 / window.grid * window.width)
            end_line_x = start_line_x + 26 / 30 * (1 / window.grid *window.width)
            start_line_y = (j - 1)/ window.grid * window.height + 2 / 30 * (1 / window.grid * window.height)
            end_line_y = start_line_y + 26 / 30 * (1 / window.grid * window.height)
            loc1start = (start_line_x, start_line_y) 
            loc1end = (end_line_x, end_line_y) 
            loc2start = (end_line_x, start_line_y) 
            loc2end = (start_line_x, end_line_y) 

            loc = (
                (i - 1)/ window.grid * window.width + 1 / 2 * (1 / window.grid * window.width), 
                (j - 1)/ window.grid * window.height + 1 / 2 * (1 / window.grid * window.height)
            )                       
            
            return loc, loc1start, loc1end, loc2start, loc2end
    
    
    @staticmethod
    def start():
        window.field()
        window.game_over = False
        arr = []
        ini.x = True
        for i in range(window.grid):
            arr2 = []
            for j in range(window.grid):
                arr2.append(ini())
            arr.append(arr2)
        
        while not window.game_over:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(window.grid):
                        for j in range(window.grid):
                            data = window.location1(event, i + 1, j + 1)
                            if data is not None:
                                arr[i][j].chek(*data)
                    window.win_or_lose(arr)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.flip()

        window.start()
    
    screen1 = pygame.display.set_mode((300,150))
    #menu()
    screen = pygame.display.set_mode((width, height))
    def win_or_lose(arr):
        s = 0
        for i in arr:
            if all(tuple(j.memory == 1 for j in i )):
                print('win o') 
                window.game_over = True      
            elif all(tuple(j.memory == 2 for j in i )):
                print('win x') 
                window.game_over = True
        for j in range(window.grid):
            for i in range(window.grid):
                if all(tuple(arr[i] [j].memory == 1 for i in range(window.grid))):
                    print('win o') 
                    window.game_over = True      
                elif all(tuple(arr[i] [j].memory == 2 for i in range(window.grid))):
                    print('win x') 
                    window.game_over = True

        if all(arr[j][j].memory == 1 for j in range(window.grid)):
                print('o win')
                window.game_over = True 
        elif all(arr[j][j].memory == 2 for j in range(window.grid)):
                print('x win')    
                window.game_over = True
        if all(arr[j][window.grid - 1 - j].memory == 1 for j in range(window.grid)):
                print('o win')
                window.game_over = True
        elif all(arr[j][window.grid - 1 - j].memory == 2 for j in range(window.grid)):
                print('x win')
                window.game_over = True
        for i in range(window.grid):
            for j in range(window.grid):
                if arr[i] [j].memory > 0 :
                    s += 1
                    if s == window.grid ** 2:
                        print("nothink")
    
                        window.game_over = True

    # def menu(self):

    #     menu_start = True
    #     self.menu_start = menu_start
    #     while menu_start == True:

    #         screen1.fill(THECOLORS['white'])
    #         pygame.draw.rect(screen1,THECOLORS['black'], (10, 25, 130, 125), 5)
    #         pygame.draw.rect(screen1,THECOLORS['black'], (170, 25, 290, 125), 5)
    #         pygame.draw.rect(screen1,THECOLORS['black'], (0, 10, 300, 155), 5)
    #         input()
    #         menu_start = False
    #     return menu_start

    @staticmethod
    def field():
        window.screen.fill(THECOLORS['white'])
        for i in range(1, window.grid):
            pygame.draw.line(window.screen, THECOLORS['black'], ((i / window.grid * window.width, 0)),((i / window.grid * window.width, window.height)), window.size)  
            pygame.draw.line(window.screen, THECOLORS['black'], ((0, i / window.grid * window.height)),((window.width, i / window.grid * window.height)), window.size)     
        
if __name__ == "__main__":
    window.start()
