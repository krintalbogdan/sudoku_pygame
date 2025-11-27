import sudoku_generator
import pygame

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        if difficulty == 'easy':
            self.difficulty = 30
        elif difficulty == 'medium':
            self.difficulty = 40
        elif difficulty == 'hard':
            self.difficulty = 50

        self.board = sudoku_generator.generate_sudoku(width, self.difficulty)
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy medium, or hard.

    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
        size = pygame.display.get_window_size()
        length = int(size[0]/9)
        width = int(size[1]/9)
        for col in range(length, size[0], length):
            if col%3==0:
                pygame.draw.line(self.screen, "black", (col,0), (col,size[1]), width=3)
            else:
                pygame.draw.line(self.screen, "black", (col,0), (col,size[1]))
        for row in range(width, size[1], width):
            if row%3==0:
                pygame.draw.line(self.screen, "black", (0,row), (size[0],row), width=3)
            else:
                pygame.draw.line(self.screen, "black", (0,row), (size[0],row))

    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        size = pygame.display.get_window_size()
        x = size[0] / 9
        y = size[1] / 9
        r = pygame.Rect(x*row, y*col, x, y)
        pygame.draw.rect(surface = self.screen, rect=r)

    def click(self, x, y):
        # If a tuple of (x,y) coordinates is within the displayed board, 
        # this function returns a tuple of the (row, col) of the cell which was clicked. 
        # Otherwise, this function returns None.
        pass

    def clear(self):
        # Clears the value cell. 
        # Note that the user can only remove the cell values and 
        # sketched values that are filled by themselves.
        pass

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to the user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        pass

    def place_number(self, value):
        # Sets the value of the current selected cell equal to the user entered value. 
        # Called when the user presses the Enter key.
        pass

    def reset_to_original(self):
        # Resets all cells in the board to their original values 
        # (0 if cleared, otherwise the corresponding digit).
        pass

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        pass

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        pass

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x,y).
        pass

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        pass
