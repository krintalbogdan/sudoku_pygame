from board import Board
import pygame

if __name__ == '__main__':
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        #wide, tall
        screen = pygame.display.set_mode((720, 720))
        
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

            screen.fill("light green")
            b.draw()

            if selected_row is not None and selected_col is not None:
                b.select(selected_col, selected_row)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


    
    