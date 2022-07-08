# sudoku solver 
from pprint import pprint
def find_next_empty(puzzle):
    # find empty spot in puzzle 
    # if no empty spot return (None,None) 
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1: # -1 represents the empty spot in puzzle
                return r,c
    
    return None,None
    
def is_valid(puzzle, guess, row, col):
    # check Row
    if guess in puzzle[row]:
        return False

    # Check column 
    col_value = [puzzle[i][col] for i in range(9)] 
    if guess in col_value:
        return False

    # check matrix 
    row_start = (row//3)*3
    col_start = (col//3)*3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    

    return True 

def solve_sudoku(puzzle):
    """
    solve sudoku using back-tracking 
    """
    # step 1: Choose empty box 
    row, col = find_next_empty(puzzle)

    # step 1.1: if there is number left, then we're done because we only allowed valid inputs 

    if row is None:
        return True
    
    # step 2: making guess
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            # place guess at that row and colum
            puzzle[row][col] = guess

            # recursively call to solve more
            if solve_sudoku(puzzle):
                return True
            
        puzzle[row][col] = -1 

    return False


if __name__ == "__main__":
    puzzle  = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    puzzle  = [
        [-1, 2, 6,   -1, -1, -1,   8, 1, -1],
        [3, -1, -1,   7, -1, 8,   -1, -1, 6],
        [4, -1, -1,   -1, 5, -1,   -1, -1, 7],

        [-1, 5, -1,   1, -1, 7,   -1, 9, -1],
        [-1, -1, 3,   9, -1, 5,   1, -1, -1],
        [-1, 4, -1,   3, -1, 2,   -1, 5, -1],

        [1, -1, -1,   -1, 3, -1,   -1, -1, 2],
        [5, -1, -1,   2, -1, 4,   -1, -1, 9],
        [-1, 3, 8,   -1, -1, -1,   4, 6, -1]
    ]

    print(solve_sudoku(puzzle))
    pprint(puzzle)
