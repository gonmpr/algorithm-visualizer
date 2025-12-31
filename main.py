import pygame
from utils.constants import Color, ScreenProperties 
from utils.data import Data
from utils.button import Button
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort


    
def main():
    run = True
    sorting = False
    clock = pygame.time.Clock()
    pygame.init()

    screen = pygame.display.set_mode((ScreenProperties.WIDTH, ScreenProperties.HEIGHT))
    
    unordered_data = Data(screen)
    data_parameters = {'n':20, 'min_val':1, 'max_val':30}
    unordered_data.generate_list(**data_parameters) 

    #buttons
    ref_y = ScreenProperties.HEIGHT / 70
    pad = ScreenProperties.WIDTH * 0.007 

    bubble_sort_buttton = Button(screen, 200, 40, pad , ref_y, 'BUBBLE SORT',lambda: bubble_sort)
    merge_sort_button = Button(screen, 200, 40, 2*pad + 200, ref_y, 'MERGE SORT', lambda:merge_sort )
    insertion_sort_button = Button(screen, 200, 40, 3*pad + 400, ref_y, 'INSERTION SORT', lambda:None)
    quick_sort_button = Button(screen, 200, 40, 4*pad + 600, ref_y, 'QUICK SORT', lambda:None)
    selection_sort_button = Button(screen, 200, 40, 5*pad + 800, ref_y, 'SELECTION SORT', lambda:None)

    reset_button = Button(screen, 100, 40, ScreenProperties.WIDTH - 100 - pad , ref_y + 40 + pad, 
                              'RESET', lambda: unordered_data.generate_list(**data_parameters))

    run_button = Button(screen, 100, 40, ScreenProperties.WIDTH - 100 - pad, ref_y, 'RUN')


    #groups
    buttons_call = [bubble_sort_buttton, merge_sort_button, insertion_sort_button,
                    quick_sort_button, selection_sort_button]

    buttons_draw = [reset_button,run_button, bubble_sort_buttton, merge_sort_button,
                    insertion_sort_button, quick_sort_button, selection_sort_button]



    last_button_clicked = None
    sorting_selected = None
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and not sorting:
                
                if run_button.mouse_on_button() and sorting_selected:
                    sorting = not sorting
                elif reset_button.mouse_on_button():
                    reset_button.call()
                    sorting = False


                for button in buttons_call:
                    if button.mouse_on_button() and button.func is not None:
                        for btn in buttons_call:
                            btn.clicked = False
                        sorting_selected = button.call()
                        button.clicked = True
                        last_button_clicked = button
                    if button != last_button_clicked:
                        button.clicked = False


        if sorting:
            last_button_clicked.clicked = True
            sorting = unordered_data.order(sorting_selected) 
            pygame.time.wait(20)

        screen.fill(Color.BACKGROUNDCOLOR)

        unordered_data.draw()

        for button in buttons_draw:
            button.draw(sorting)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
