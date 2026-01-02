import pygame, random
from utils.constants import ScreenProperties, Color
from collections.abc import Iterable
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
        value_diference = self.max_val - self.min_val if  self.max_val - self.min_val > 0 else 1
        self.bar_height = round((ScreenProperties.HEIGHT - ScreenProperties.TOPPAD) / value_diference)
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
            self.color_positions = {} 

            lst_state, indexs, index2, action = next(self.sort_generator)
            
            self.lst = lst_state
            
            if isinstance(indexs, Iterable):
                c = 1
                for i in indexs:
                    if i >= 0:
                        self.color_positions[i] = Color.ESPECIALBARCOLOR[c]  
                        c = 0
            else:
                if indexs >= 0:
                    self.color_positions[indexs] = Color.ESPECIALBARCOLOR[1]  

            if index2 >= 0:
                self.color_positions[index2] = Color.ESPECIALBARCOLOR[2] 
            
            if not action:
                self.sort_generator = None
                return False  
            
            return True
            
        except StopIteration:
            self.sort_generator = None
            return False
    def draw(self):
        
        for i, val in enumerate(self.lst):

            x = self.start_draw + i * self.bar_width
            y = ScreenProperties.HEIGHT - (val - self.min_val) * self.bar_height
            width = self.bar_width

            height = (val - self.min_val) * self.bar_height
            if height == 0:
                height = self.bar_height * 0.5  
                y = ScreenProperties.HEIGHT - height

            color = Color.BARCOLORS[i%3]

            if i in self.color_positions:
                color = self.color_positions[i]


            font = pygame.font.SysFont('Terminus',width) 
            text = font.render(str(val), True, color)


            pygame.draw.rect(self.window, color, (x, y, width, height))
            self.window.blit(text, (x + (width - text.get_width())/2, y - width/1.5 )) 








