import sudoku_generator
import pygame
import cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.selected_cell = None
        if difficulty == 'easy':
            self.difficulty = 30
        elif difficulty == 'medium':
            self.difficulty = 40
        elif difficulty == 'hard':
            self.difficulty = 50
        

        self.board = sudoku_generator.generate_sudoku(width, self.difficulty)
        for ind, row in enumerate(self.board):
            for ind2, cell_obj in enumerate(row):
                self.board[ind][ind2] = cell.Cell(cell_obj, ind, ind2, self.screen)
            
        # WE NEED TO WRITE IN CELLS HERE
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy medium, or hard.

    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
        size = (720, 720)# pygame.display.get_window_size()
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
            
        
        for ind, row in enumerate(self.board):
            for ind2, cell_obj in enumerate(row):
                self.board[ind][ind2].draw()


    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        size = (720, 720) # pygame.display.get_window_size()
        self.selected_cell = [int(row), int(col)]
        x = size[0] / 9
        y = size[1] / 9

        r = pygame.Rect(x*row, y*col, x, y)
        pygame.draw.rect(surface = self.screen, rect=r, color = (255, 255, 255, 128))

    def click(self, x, y):
        # If a tuple of (x,y) coordinates is within the displayed board, 
        # this function returns a tuple of the (row, col) of the cell which was clicked. 
        # Otherwise, this function returns None.
        size = (720, 720) # pygame.display.get_window_size()
        cell_size = size[0] / 9
        col = x//cell_size
        row = y//cell_size
        return (col, row)

    def clear(self):
        # Clears the value cell. 
        # Note that the user can only remove the cell values and 
        # sketched values that are filled by themselves.
        selected_cell = self.board[self.selected_cell[0]][self.selected_cell[1]]
        if selected_cell.sketched_value != None:
            selected_cell.value = 0
            selected_cell.sketched_value = None

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to the user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        print(self.selected_cell)
        selected_cell = self.board[self.selected_cell[0]][self.selected_cell[1]]
        selected_cell.set_sketched_value(value)
        print("sketcheimpasse")

    def place_number(self, value):
        # Sets the value of the current selected cell equal to the user entered value. 
        # Called when the user presses the Enter key.
        print(self.selected_cell)
        selected_cell = self.board[self.selected_cell[0]][self.selected_cell[1]]
        selected_cell.set_value(value)
        print("sketcheimpasse")

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
