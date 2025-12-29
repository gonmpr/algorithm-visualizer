import pygame, random
from constants import ScreenProperties, Color

class Data:

    def __init__(self, window):
        self.window = window

    def set_list(self):
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
            
    def draw_list(self):
        
        for i, val in enumerate(self.lst):

            x = self.start_draw + i * self.bar_width
            y = ScreenProperties.HEIGHT - (val - self.min_val) * self.bar_height
            width = self.bar_width
            height = (val - self.min_val) * self.bar_height

            color = Color.BARCOLORS[i%3]

            pygame.draw.rect(self.window, color, (x, y, width, height))
