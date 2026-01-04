import pygame
from utils.constants import Color, ScreenProperties, Value 
from utils.data import Data
from utils.button import Button
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.quick_sort import quick_sort
from algorithms.selection_sort import selection_sort
from algorithms.bogo_sort import bogo_sort


    
def main():
    run = True
    sorting = False
    clock = pygame.time.Clock()
    pygame.init()
    font = pygame.font.SysFont('Terminus', 28) 

    screen = pygame.display.set_mode((ScreenProperties.WIDTH, 
                                      ScreenProperties.HEIGHT))
    
    unordered_data = Data(screen)
    
    unordered_data.generate_list(Value.SIZE, 1, Value.SIZE) 

    #buttons
    ref_y = ScreenProperties.HEIGHT / 70
    pad = ScreenProperties.WIDTH * 0.003 

    bubble_sort_buttton = Button(screen, 200, 40, pad , ref_y, 
                                    'BUBBLE SORT',lambda: bubble_sort)

    selection_sort_button = Button(screen, 200, 40, 2*pad + 200, ref_y,
                                   'SELECTION SORT', lambda:selection_sort)

    insertion_sort_button = Button(screen, 200, 40, 3*pad + 400, ref_y,
                                    'INSERTION SORT', lambda:insertion_sort)

    quick_sort_button = Button(screen, 200, 40, 4*pad + 600, ref_y,
                               'QUICK SORT', lambda:quick_sort)

    merge_sort_button = Button(screen, 200, 40, 5*pad + 800, ref_y,
                               'MERGE SORT', lambda:merge_sort )

    bogo_sort_button = Button(screen, 200, 40, pad , ref_y + 40 + pad, 'BOGO SORT', lambda:bogo_sort)



    run_button = Button(screen, 100, 40, ScreenProperties.WIDTH - 200 - 2*pad, ref_y, 'RUN')

    reset_button = Button(screen, 100, 40, ScreenProperties.WIDTH - 100 - pad, ref_y + 40 + pad, 
                              'RESET', lambda: unordered_data.generate_list(Value.SIZE, 1, Value.SIZE))

    stop_button = Button(screen, 100, 40, ScreenProperties.WIDTH - 100 - pad , ref_y , 'STOP')


    step_button = Button(screen, 100, 40, ScreenProperties.WIDTH - 200 - 2*pad, ref_y + 40 + pad, 'STEP')

    #groups
    buttons_call = [bubble_sort_buttton, merge_sort_button, insertion_sort_button,
                    quick_sort_button, selection_sort_button, bogo_sort_button]

    buttons_draw = [reset_button,run_button,step_button, bubble_sort_buttton, merge_sort_button,
                    insertion_sort_button, quick_sort_button, selection_sort_button,
                    bogo_sort_button]



    last_button_clicked = None
    sorting_selected = None

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and sorting:
                if stop_button.mouse_on_button():
                    sorting = False
                    unordered_data.stop()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and not sorting:
                
                if run_button.mouse_on_button() and sorting_selected:
                    sorting = True 
                if reset_button.mouse_on_button():
                    reset_button.call()
                    sorting = False
                if step_button.mouse_on_button() and sorting_selected:
                    unordered_data.order(sorting_selected) 

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
#           pygame.time.wait(20)

        screen.fill(Color.BACKGROUNDCOLOR)

        unordered_data.draw()

        for button in buttons_draw:
            button.draw(sorting)
        stop_button.draw(not sorting)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
