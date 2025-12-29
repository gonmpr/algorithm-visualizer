import pygame
from constants import Color


class Button:
    def __init__(self, window, pos_x, pos_y, width, height, text):
        self.window = window

        self.button = pygame.Rect(pos_x, pos_y, width, height)
        
        self.font = pygame.font.SysFont('Arial', 30) 

        self.text = self.font.render(text, True, Color.BLACK)
        self.text_pos = (pos_x + (self.button.width - self.text.get_width())/2, 
                         pos_y + (self.button.height - self.text.get_height())/2) 

    def draw(self):
        if self.mouse_on_button():
            pygame.draw.rect(self.window, Color.RED, self.button)
        else:
            pygame.draw.rect(self.window, Color.GREEN, self.button)
        self.window.blit(self.text, self.text_pos) 

    def mouse_on_button(self):
        return self.button.collidepoint(pygame.mouse.get_pos())
