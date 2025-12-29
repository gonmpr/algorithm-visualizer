import pygame
from constants import Color, ScreenProperties
from data import Data
from button import Button

    
def main():
    run = True
    clock = pygame.time.Clock()
    pygame.init()

    window = pygame.display.set_mode((ScreenProperties.WIDTH, ScreenProperties.HEIGHT))
    
    boton_prueba = Button(window, 20, 20, 100, 40, 'hola')
    unordered_data = Data(window)
    unordered_data.generate_list(15, 1, 20) #value, min_val, max_val

    
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                boton_prueba.last_clicked = True


        window.fill(Color.BACKGROUNDCOLOR)
        unordered_data.draw()
        boton_prueba.draw()
        pygame.display.update()
        
        clock.tick(60)

if __name__ == '__main__':
    main()
