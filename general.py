import pygame
import sys
from pygame.color import THECOLORS
import math
from x_or_o import Ui_MainWindow
from PyQt5 import QtWidgets
import Window

pygame.init
# class ini(Ui_MainWindow):

#     def __init__(self, parend):
        # Ui_MainWindow.__init__(self)
        # self.loc = None
        # self.loc1start = None
        # self.loc1end = None
        # self.loc2start = None
        # self.loc2end = None
        # self.incorrect = False
        # self.memory = 0 
        # self.button_event()
        # self.x = True

    # def button_event(self):
    #     pass 

    # def x_or_o(self, loc, loc1start, loc1end, loc2start, loc2end):
    #     self.x = not self.x
    #     if self.x:
    #         self.figure_1(loc)
    #         self.memory = 1
    #     else:
    #         self.figure_2(loc1start, loc1end, loc2start, loc2end)
    #         self.memory = 2
            

    # def chek(self, loc, loc1start, loc1end, loc2start, loc2end):
    #     if not self.incorrect:
    #         self.x_or_o(loc, loc1start, loc1end, loc2start, loc2end)
    #         self.incorrect = True
    #     else:
    #         print("---")
    
    # def figure_1(self, loc):
    #     pygame.draw.circle(lo.screen, THECOLORS["black"], loc, round(1 / (2.5 * lo.grid) * min(lo.height, lo.width)),  lo.size)
        
    # def figure_2(self, loc1start, loc1end, loc2start, loc2end):
    #     pygame.draw.line(self.parend.c, THECOLORS["black"], loc1start, loc1end,  lo.size)
    #     pygame.draw.line(lo.screen, THECOLORS["black"], loc2start, loc2end, lo.size)
    


class General():
    def __init__(self):
        # self.height = 600
        # self.width = 600
        self.game_over = False
        # self.grid = 3
        # self.size = math.ceil((self.width * 0.02) / ((self.grid) / 2))
        # self.screen = pygame.display.set_mode((self.width, self.height))
        self.game_over = False
        Ui_MainWindow.__init__(self)
        # self.loc = None
        # self.loc1start = None
        # self.loc1end = None
        # self.loc2start = None
        # self.loc2end = None
        self.incorrect = False
        self.memory = 0 
        self.button_event()
        self.x = True


    # def location1(self, event, i, j):
    #     if (
    #         (i - 1) / self.grid * self.width < event.pos[0] < i / self.grid * self.width and 
    #         (j - 1) / self.grid * self.height < event.pos[1] < j / self.grid * self.height
    #     ):
    #         start_line_x = (i - 1)/ self.grid * self.width + 2 / 30 * (1 / self.grid * self.width)
    #         end_line_x = start_line_x + 26 / 30 * (1 / self.grid *self.width)
    #         start_line_y = (j - 1)/ self.grid * self.height + 2 / 30 * (1 / self.grid * self.height)
    #         end_line_y = start_line_y + 26 / 30 * (1 / self.grid * self.height)
    #         loc1start = (start_line_x, start_line_y) 
    #         loc1end = (end_line_x, end_line_y) 
    #         loc2start = (end_line_x, start_line_y) 
    #         loc2end = (start_line_x, end_line_y) 
            
    #         loc = (
    #             (i - 1)/ self.grid * self.width + 1 / 2 * (1 / self.grid * self.width), 
    #             (j - 1)/ self.grid * self.height + 1 / 2 * (1 / self.grid * self.height)
    #         )                       
            
    #         return loc, loc1start, loc1end, loc2start, loc2end
    

    def start(self):
        Window.Window.field(self)
        arr = []
        for i in range(Window.Window.grid):
            arr2 = []
            for j in range(Window.Window.grid):
                arr2.append(Window.Window())
            arr.append(arr2)
        
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(arr2.grid):
                        for j in range(self.grid):
                            data = arr.location1(event, i + 1, j + 1)
                            if data is not None:
                                self.chek(*data)
                    self.win_or_lose(arr)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.flip()

        self.start()
    
    screen1 = pygame.display.set_mode((300,150))
    #menu()
    
    def win_or_lose(self, arr):
        s = 0
        for i in arr:
            if all(tuple(j.memory == 1 for j in i )):
                print('win o') 
                self.game_over = True      
            elif all(tuple(j.memory == 2 for j in i )):
                print('win x') 
                self.game_over = True
        for j in range(self.grid):
            for i in range(self.grid):
                if all(tuple(arr[i] [j] == 1 for i in range(self.grid))):
                    print('win o') 
                    self.game_over = True      
                elif all(tuple(arr[i] [j] == 2 for i in range(self.grid))):
                    print('win x') 
                    self.game_over = True

        if all(arr[j][j] == 1 for j in range(self.grid)):
                print('o win')
                self.game_over = True 
        elif all(arr[j][j] == 2 for j in range(self.grid)):
                print('x win')    
                self.game_over = True
        if all(arr[j][self.grid - 1 - j] == 1 for j in range(self.grid)):
                print('o win')
                self.game_over = True
        elif all(arr[j][self.grid - 1 - j] == 2 for j in range(self.grid)):
                print('x win')
                self.game_over = True
        for i in range(self.grid):
            for j in range(self.grid):
                if arr[i] [j] > 0 :
                    s += 1
                    if s == self.grid ** 2:
                        print("nothink")
    
                        self.game_over = True

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
    def button_event(self):
        pass 

    def x_or_o(self, loc, loc1start, loc1end, loc2start, loc2end):
        self.x = not self.x
        if self.x:
            Window.Window.field(loc)
            # self.figure_1(loc)
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
    
    # def figure_1(self, loc):
    #     pygame.draw.circle(lo.screen, THECOLORS["black"], loc, round(1 / (2.5 * lo.grid) * min(lo.height, lo.width)),  lo.size)
        
    # def figure_2(self, loc1start, loc1end, loc2start, loc2end):
    #     pygame.draw.line(self.screen, THECOLORS["black"], loc1start, loc1end, self.size)
    #     pygame.draw.line(self.screen, THECOLORS["black"], loc2start, loc2end, self.size)
    
    # def field(self):
    #     self.screen.fill(THECOLORS['white'])
    #     for i in range(1, self.grid):
    #         pygame.draw.line(self.screen, THECOLORS['black'], ((i / self.grid * self.width, 0)),((i / self.grid * self.width, self.height)), self.size)  
    #         pygame.draw.line(self.screen, THECOLORS['black'], ((0, i / self.grid * self.height)),((self.width, i / self.grid * self.height)), self.size)     
        
if __name__ == "__main__":
    lo = General()
    lo.start()
