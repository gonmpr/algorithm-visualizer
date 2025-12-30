import pygame, random
from constants import ScreenProperties, Color

class Data:

    def __init__(self, window):
        self.window = window
        self.lst = []
        self.min_val = 0
        self.max_val = 0
        self.sort_gen = None  # Añadir esto
        self.color_positions = {}  # Añadir esto

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



    def order(self, algorithm_func):
        if not self.sort_gen:
            self.sort_gen = algorithm_func(self.lst.copy())
            self.color_positions = {}
        
        try:
            # Obtener siguiente paso
            lst_state, idx1, idx2, action = next(self.sort_gen)
            
            # Actualizar lista
            self.lst = lst_state
            
            # Guardar índices para colorear (VERDE y ROJO como en el ejemplo)
            self.color_positions = {}
            if idx1 >= 0:
                self.color_positions[idx1] = Color.GREEN  # Primera barra verde
            if idx2 >= 0:
                self.color_positions[idx2] = Color.RED  # Segunda barra roja
            
            if action == "done":
                self.sort_gen = None
                self.color_positions = {}
                return False  
            
            return True
            
        except StopIteration:
            self.sort_gen = None
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
