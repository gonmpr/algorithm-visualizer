import pygame
from constants import Color


class Button:
    def __init__(self, window, pos_x, pos_y, width, height, text, func = lambda:None):
        self.window = window
        self.func = func
        self.clicked = False # TODO: implementar alternancia
        self.color = Color.GREEN
        self.button = pygame.Rect(pos_x, pos_y, width, height)
        
        self.font = pygame.font.SysFont('Terminus', 30) 

        self.text = self.font.render(text, True, Color.BLACK)

        self.text_pos = (pos_x + (self.button.width - self.text.get_width())/2, 
                         pos_y + (self.button.height - self.text.get_height())/2) 

    def draw(self, sorting=False):
        if self.mouse_on_button() and not self.clicked and not sorting:
            self.color = Color.GREY

        pygame.draw.rect(self.window, self.color, self.button, border_radius=10)
        self.window.blit(self.text, self.text_pos) 

        if self.clicked and not sorting:
            self.color = Color.RED
            return

        self.color = Color.GREEN

    def mouse_on_button(self):
        return self.button.collidepoint(pygame.mouse.get_pos())


    def call(self) :
        if self.mouse_on_button():
            if not self.func:
                raise Exception("Button class Error: function must be setted before use")
            return self.func()
