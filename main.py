from board import Board
import pygame

num_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

def main_screen(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Stops the main loop
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if b1.collidepoint((x,y)):
                    print("Returned easy")
                    return 'easy'
                elif b2.collidepoint((x,y)):
                    print("Returned m")
                    return 'medium'
                elif b3.collidepoint((x,y)):
                    print("Returned h")
                    return 'hard'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill('white')
        font = pygame.font.SysFont('arial', 50)
        title_text = font.render(str('Welcome to sudoku!'), True, (0, 0, 0))
        screen.blit(title_text, (125, 300))

        smaller_font = pygame.font.SysFont('arial', 25)
        button1 = pygame.rect.Rect(100, 550, 100, 50)
        pygame.draw.rect(screen, 'red', button1)
        title_text = smaller_font.render(str('Easy'), True, (0, 0, 0))
        b1 = screen.blit(title_text, (120, 560))

        button2 = pygame.rect.Rect(300, 550, 100, 50)
        pygame.draw.rect(screen, 'red', button2)
        title_text = smaller_font.render(str('Medium'), True, (0, 0, 0))
        b2 = screen.blit(title_text, (305, 560))

        button3 = pygame.rect.Rect(500, 550, 100, 50)
        pygame.draw.rect(screen, 'red', button3)
        title_text = smaller_font.render(str('Hard'), True, (0, 0, 0))
        b3 = screen.blit(title_text, (520, 560))



        pygame.display.flip()
        clock.tick(60)


def game_screen(screen, difficulty):
    b = Board(9, 9, screen, difficulty)

    selected_row = None
    selected_col = None
    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 'Stop'

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                selected_col, selected_row = b.click(x, y)

                

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    selected_col, selected_row = None, None
                elif event.key in num_keys:
                    selected = [ind for ind, num in enumerate(num_keys) if num == event.key][0]
                    b.sketch(selected)
                    selected_col, selected_row = None, None
                elif event.key == pygame.K_RETURN:
                    b.place_number()
                elif event.key == pygame.K_y:
                    return 'W'
                elif event.key == pygame.K_u:
                    return 'L'


        screen.fill("light green")
        b.draw()

        if selected_row is not None and selected_col is not None:
            b.select(selected_col, selected_row)

        pygame.display.flip()
        clock.tick(60)

def end_screen(screen, rez):
    titled_text = 'You lose :(' if rez == "L" else 'You win!'
    buttond_text = 'restart' if rez == "L" else 'exit'
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Stops the main loop
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if b1.collidepoint((x,y)):
                    return 'Restart' if rez == 'L' else None
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill('white')
        font = pygame.font.SysFont('arial', 50)
        title_text_r = font.render(str(titled_text), True, (0, 0, 0))
        screen.blit(title_text_r, (125, 300))

        smaller_font = pygame.font.SysFont('arial', 25)
        button1 = pygame.rect.Rect(100, 550, 100, 50)
        pygame.draw.rect(screen, 'red', button1)
        button_text_r = smaller_font.render(str(buttond_text), True, (0, 0, 0))
        b1 = screen.blit(button_text_r, (120, 560))

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        #wide, tall
        screen = pygame.display.set_mode((720, 820))
        STAGE = 0
        clock = pygame.time.Clock()
        running = True
        while running:
            if STAGE == 0:
                difficulty = main_screen(screen)
                STAGE += 1

            if STAGE == 1:
                print("se fue")

                rez = game_screen(screen, difficulty)
                if rez == 'Stop':
                    quit()
                else:
                    STAGE += 1

            if STAGE == 2:
                resp = end_screen(screen, rez)

                if resp == 'Restart':
                    STAGE -= 1
                else:
                    running = False
        

            
    finally:
        pygame.quit()



'''
if __name__ == '__main__':
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        #wide, tall
        screen = pygame.display.set_mode((720, 820))
        
        clock = pygame.time.Clock()
        running = True
        b = Board(9, 9, screen, 'easy')

        selected_row = None
        selected_col = None

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False # Stops the main loop

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    selected_col, selected_row = b.click(x, y)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        selected_col, selected_row = None, None
                    elif event.key in num_keys:
                        selected = [ind for ind, num in enumerate(num_keys) if num == event.key][0]
                        b.sketch(selected)
                        selected_col, selected_row = None, None
                    elif event.key == pygame.K_RETURN:
                        b.place_number()


            screen.fill("light green")
            b.draw()

            if selected_row is not None and selected_col is not None:
                b.select(selected_col, selected_row)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

'''