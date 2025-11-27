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
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False # Stops the main loop
            screen.fill("light green")
            b.draw()
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


    
    