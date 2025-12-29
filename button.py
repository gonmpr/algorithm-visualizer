import pygame
from constants import Color


class Button:
    def __init__(self, window, pos_x, pos_y, width, height, text, func = None):
        self.window = window
        self.func = func
        self.last_clicked = False
        self.color = Color.GREEN
        self.button = pygame.Rect(pos_x, pos_y, width, height)
        
        self.font = pygame.font.SysFont('Arial', 30) 

        self.text = self.font.render(text, True, Color.BLACK)

        self.text_pos = (pos_x + (self.button.width - self.text.get_width())/2, 
                         pos_y + (self.button.height - self.text.get_height())/2) 

    def draw(self):
        #when mouse is over but is not clicked
        if self.mouse_on_button() and not self.last_clicked:
            self.color = Color.GREY

        pygame.draw.rect(self.window, self.color, self.button, border_radius=20)
        self.window.blit(self.text, self.text_pos) 

        #when the button was clicked set this color
        if self.last_clicked:
            self.color = Color.RED
            return

        self.color = Color.GREEN

    def mouse_on_button(self):
        return self.button.collidepoint(pygame.mouse.get_pos())


    def use(self, *args):
        if not self.func:
            raise Exception("Button class Error: function must be setted before use")
        self.func(*args)
        return 1
