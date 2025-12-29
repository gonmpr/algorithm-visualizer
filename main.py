import pygame
from constants import Color, ScreenProperties
from data import Data
    
def main():
    run = True
    clock = pygame.time.Clock()
    pygame.init()

    window = pygame.display.set_mode((ScreenProperties.WIDTH, ScreenProperties.HEIGHT))
    
    unordered_data = Data(window)
    unordered_data.generate_list(300, 1, 50) #value, min_val, max_val

    
    while run:

        window.fill(Color.BACKGROUNDCOLOR)
        unordered_data.draw_list()
        pygame.display.update()






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        clock.tick(60)

if __name__ == '__main__':
    main()
