import pygame
from constants import Color, ScreenProperties
from data import Data
from button import Button
from bubble_sort import bubble_sort
    
def main():
    run = True
    sorting = False
    clock = pygame.time.Clock()
    pygame.init()

    window = pygame.display.set_mode((ScreenProperties.WIDTH, ScreenProperties.HEIGHT))
    
    unordered_data = Data(window)
    data_parameters = {'n':10, 'min_val':1, 'max_val':15} #n, min_val, max_val
    unordered_data.generate_list(**data_parameters) 

    #buttons
    randomize_button = Button(window, 20, 20, 100, 40, 'RESET', lambda: unordered_data.generate_list(**data_parameters))
    run_button = Button(window, 200, 20, 100, 40, 'RUN')
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and not sorting:
                
                if run_button.mouse_on_button():
                    sorting = not sorting

                randomize_button.call()


        if sorting:
            sorting = unordered_data.order(bubble_sort) 
#           pygame.time.wait(25)

        window.fill(Color.BACKGROUNDCOLOR)

        unordered_data.draw()

        randomize_button.draw(sorting)
        run_button.draw(sorting)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
