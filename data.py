import pygame, random
from constants import ScreenProperties, Color

class Data:

    def __init__(self, window):
        self.window = window
        self.lst = []
        self.min_val = 0
        self.max_val = 0
        self.sort_generator = None 
        self.color_positions = {}

    def set_list(self):
        if not self.lst:
            raise Exception("Data class error: lst not defined")

        self.min_val = min(self.lst)
        self.max_val = max(self.lst)

        self.bar_width = round((ScreenProperties.WIDTH - ScreenProperties.SIDEPAD) / len(self.lst))
        self.bar_height = round((ScreenProperties.HEIGHT - ScreenProperties.TOPPAD) / (self.max_val - self.min_val))
        self.start_draw = ScreenProperties.SIDEPAD // 2



    def generate_list(self, n, min_val, max_val):
        self.lst = []
        for _ in range(n):
            val = random.randint(min_val, max_val)
            self.lst.append(val)
        self.set_list()



    def order(self, func):
        if not self.sort_generator:
            self.sort_generator = func(self.lst.copy())
        
        try:
             
            lst_state, index1, index2, action = next(self.sort_generator)
            self.lst = lst_state
            
            self.color_positions = {}
            if index1 >= 0:
                self.color_positions[index1] = Color.ESPECIALBARCOLOR[0]  
            if index2 >= 0:
                self.color_positions[index2] = Color.ESPECIALBARCOLOR[1] 
            
            if not action:
                self.sort_generator = None
                return False  
            
            return True
            
        except StopIteration:
            self.sort_generator = None
            self.color_positions = {}
            return False
            
    def draw(self):
        
        for i, val in enumerate(self.lst):

            x = self.start_draw + i * self.bar_width
            y = ScreenProperties.HEIGHT - (val - self.min_val + 1 ) * self.bar_height
            width = self.bar_width
            height = (val - self.min_val + 1) * self.bar_height
            color = Color.BARCOLORS[i%3]

            if i in self.color_positions:
                color = self.color_positions[i]

            pygame.draw.rect(self.window, color, (x, y, width, height))
