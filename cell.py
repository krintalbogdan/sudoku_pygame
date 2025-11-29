import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = None
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        size = pygame.display.get_window_size()
        cell_size = size[0] / 9
        #rect_dimensions = pygame.rect.Rect(self.col*cell_size, self.row*cell_size, cell_size, cell_size)
        #pygame.draw.rect(self.screen, 'red', rect_dimensions)
        if self.value != 0:
            font = pygame.font.SysFont('arial', 50)
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (self.row*cell_size + 20, self.col*cell_size + 20))
        elif self.sketched_value != None:
            font = pygame.font.SysFont('arial', 50)
            text = font.render(str(self.sketched_value), True, (150, 150, 150))
            self.screen.blit(text, (self.row*cell_size + 20, self.col*cell_size + 20))

    # CELLS