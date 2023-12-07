"""
CSSE1001 Assignment 1
Semester 2, 2022
"""
import a1_support
from a1_support import *


# Fill these in with your details
__author__ = "Ruobing Wang"
__email__ = "s4723675@student.uq.edu.au"
__date__ = "3/08/2022"


# Write your functions here

board_one = a1_support.load_board('boards/board_one.txt')
board_two = a1_support.load_board('boards/board_two.txt')
board_three = a1_support.load_board('boards/board_three.txt')
empty_board = a1_support.load_board('boards/empty_board.txt')
board_one_winnable = a1_support.load_board('boards/board_one_winnable.txt')


def num_hours() -> float:
    """
    the main purpose verify that  understanding how to submit to Gradescope and estimate time-consuming in this assignment.

    Returns: function  return the number of hours that estimate spent in this assignment as a float variable.


    """
    hours = 100.5
    return hours


def is_empty(position: tuple[int, int], board: Board) -> bool:
    """ Check tuple position is None or empty in Board that  convert to  Boolean values.
    if this position we checked is empty or None that will return True otherwise it will return False.

     Parameters:
     position (tuple[int,int]): the cell (row,column) position we check is empty or not.

     board (list[list[Optional[int]]]): the list of list the board we focused on.

     Return:

     bool: return True if there is empty or None cell in board ,or filled with a value return and not a valid board to false.

     Preconditions: all position should on 9x9 board.

    Examples:
    ->>>is_empty((3, 5), board_three)
    False
    ->>>is_empty((8, 8), board_three)
    True
    ->>>is_empty((10, 8), board_three)
    False
    ->>> is_empty((8, 10), board_three)
    False

"""

    board_cols = len(board[0])
    (row, column) = position
    if board[row][column] == 0 or None:
        return True
    if 0 <= row < len(board) and 0 <= column < board_cols:
        return board[row][column] is None
    return False  # Error provided is not on this board'


def update_board(position: tuple[int, int], value: Optional[int], board: Board) -> None:
    """
    Updates the board at the provided (row, column) position with the provided value.

    Args:
        position (tuple[int,int]):the position( row,column) should be updated.

        value (Optional [int]):the value should be in that position.

        board (Board:list[list[Optional[int]]]): the board we use to implement this function.

    Preconditions: all position should on 9x9 board and the given position must not correspond to a filled
    cell in the original board.

    Returns:None ,since we only perform actions and board can be altered given as a parameter in this function.


    Examples:
    ->>update_board((8, 8), 5, board_three)
    ->>> board_three
    [[6, 8, 5, 1, 3, 2, 9, 4, 7], [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3], [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2], [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1], [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, 5]]

    """

    (row, column) = position
    if is_empty(position, board) or board[row][column] != value:
        board[row][column] = value


def clear_position(position: tuple[int, int], board: Board) -> None:
    """
    Updates the board to clear the cell at the provided (row, column) position.
    Args:
        position (tuple[int,int]):the position( row,column) should be cleared.

        board (Board->:list[list[Optional[int]]]):Board:list[list[Optional[int]]]):
        the board we use to implement this function.

    precondition:the given position must not correspond to a filled cell in the original board.

    Assumption:the given position exists on the board.

    Returns:None

    Examples:
        ->>> update_board((8, 8), 5, board_three)
    ->>> board_three
    [[6, 8, 5, 1, 3, 2, 9, 4, 7], [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3], [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2], [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1], [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, 5]]
    ->>> clear_position((8,8), board_three)
    ->>> board_three
    [[6, 8, 5, 1, 3, 2, 9, 4, 7], [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3], [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2], [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1], [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, None]]

    """
    (row, column) = position
    if is_empty(position, board) is False:
        board[row][column] = None


def read_board(raw_board: str) -> Board:
    """
    Converts the raw board from a string of characters into a list of 9 lists.
    Args:
        raw_board (str):string will only ever contain integers and/or space characters.

    Assumption: the string will only ever contain integers and/or space characters.

    Returns(Board:list[list[Optional[int]]]) :revert into a list contain 9 lists.
    Examples:

    ->>> read_board(board_one)
    [[6, 8, 5, 1, 3, 2, 9, 4, 7], [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3], [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2], [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1], [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, None]]
    ->>> read_board(board_two)
    [[6, 8, 5, 1, 3, None, None, 4, 7],
    [7, None, None, None, None, None, None, 1, None],
    [None, 1, None, 7, 6, 4, None, 5, None],
    [9, None, None, None, 7, None, 5, None, 4],
    [8, None, 1, None, None, 9, None, 7, 2],
    [4, None, 3, None, None, 6, None, None, None],
    [None, None, None, 4, 2, 7, 3, 9, None],
    [None, 4, None, 9, None, None, None, 6, 8],
    [1, None, 7, None, None, None, 4, None, None]]




    """
    new_list = [value for value in raw_board]  # make string convert to one list
    result = []   # create an empty list to add more string list
    # we change all strings in original list to an integer list
    for num in new_list:
        try:
            e = int(num)
            result.append(e)
        except:
            # if list contain empty string("") we convert it to integer(0) add in list(result) ,then convert 0 to None
            if num == "":
                result.append(0)
            else:
                result.append(None)
    new_list1 = [result[j:j + 9] for j in range(0, len(new_list), 9)]  # make 9 individual lists in one list to 2d list

    return new_list1


def print_board(board: Board) -> None:
    """
    Displays the puzzle in a user-friendly format with column number and row number.

    Args:
        board (Board:list[list[Optional[int]]]):the list contain 9 lists.

    Returns:None.

    Examples:
->>> print_board(board_three)
    685|132|947 0
    734|598|216 1
    219|764|853 2
    -----------
    926|871|534 3
    851|349|672 4
    473|256|189 5
    -----------
    568|427|391 6
    342|915|768 7
    197|683|42  8
    012 345 678


    """
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:  # set signal for every 3 rows not start first row
            print(HORIZONTAL_WALL * 11)

        for column in range(len(board[0])):
            if board[row][column] is None or board[row][column] == 0:  # set None element in column with whitespace
                board[row][column] = " "

            if column % 3 == 0 and column != 0:  # set column with end of every 3 column
                print(VERTICAL_WALL, end="")

            if column == (len(board)-1):           # at the index 8 we set numbers of columns next to this
                print(board[row][column], row)

            else:

                print(str(board[row][column]), end="")
    print("\n012 345 678")  # this is the row number with next line


def row_check(board: Board) -> bool:
    """
    Check each row is duplication and valid in sudoku.

    Args:
        board(Board:list[list[Optional[int]]]): The board user plays.

    Returns (bool):boolean value,
    if each value in row that duplicate , not fulled in correct values or with no correct value input return False,
    otherwise return True.

    Examples:
    ->>>update_board((8, 8), 5, board_three)
    ->>> board_three
    [[6, 8, 5, 1, 3, 2, 9, 4, 7], [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3], [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2], [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1], [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, 5]]
    ->>> row_check(board_three)
    True

    """
    for row in range(len(board)):
        lst = []
        for j in range(len(board)):
            if board[row][j] is None:  # if there is None in row that means row list not full
                return False
            if board[row][j] in lst:   # check if update value is already exist in row list
                return False
            else:
                lst.append(board[row][j])  # if there is no duplicate value in row and all cells be filled
    return True


def col_check(board: Board) -> bool:
    """

    Check each column is duplication and valid in sudoku.

    Args:
        board(Board:list[list[Optional[int]]]): The board user plays.

    Returns (bool):boolean value,
    if each value in column that duplicate , not fulled in correct values or not correct value input return False ,
    otherwise return True.

    Examples:
   ->>>update_board((8, 8), 5, board_three)
    ->>> board_three
    [[6, 8, 5, 1, 3, 2, 9, 4, 7], [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3], [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2], [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1], [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, 5]]
    ->>> col_check(board_three)
    True
    """
    for col in range(len(board)):
        lst = []
        # example :lst[]-->board_three
        # [6, 7, 2, 9, 8, 4, 5, 3, 1]
        # [8, 3, 1, 2, 5, 7, 6, 4, 9]
        # [5, 4, 9, 6, 1, 3, 8, 2, 7]
        # [1, 5, 7, 8, 3, 2, 4, 9, 6]
        # [3, 9, 6, 7, 4, 5, 2, 1, 8]
        # [2, 8, 4, 1, 9, 6, 7, 5, 3]
        # [9, 2, 8, 5, 6, 1, 3, 7, 4]
        # [4, 1, 5, 3, 7, 8, 9, 6, 2]
        # [7, 6, 3, 4, 2, 9, 1, 8, 5]

        for i in range(len(board)):
            if board[i][col] is None:  # if there is value not be filled in column list
                return False
            if board[i][col] in lst:   # if update value already exist in original column list
                return False
            else:
                lst.append(board[i][col])  # if there is no duplicate value in column and all cells be filled
    return True


def grid_check(board: Board) -> bool:
    """
    Check each 3x3 grid duplication and valid in sudoku board since we have 9 small grids.
    Args:
        board (Board:list[list[Optional[int]]]): the board user plays.

    Returns(bool):boolean values
    if each value in grid that duplicate , not fulled in correct values or not correct value input return False ,
    otherwise return True.

    Examples:
   ->>>update_board((8, 8), 5, board_three)
    ->>> board_three
    [[6, 8, 5, 1, 3, 2, 9, 4, 7],
     [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3],
     [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2],
    [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1],
     [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, 5]]
    ->>> col_check(board_three)
    True

    """
    grid_set = int((len(board) ** 0.5))  # since this is 3x3 grid

    for row_start in range(0, len(board), grid_set):  # row divided into 3
        row_end = row_start + grid_set
        for column_start in range(0, len(board), grid_set):  # column divided into 3 in each row
            column_end = column_start + grid_set
            lst = []

            # example:board_three

            # |391|
            # |768|
            # |425|
            #  to below check
            # [3]
            # [3, 9]
            # [3, 9, 1]
            # [3, 9, 1, 7]
            # [3, 9, 1, 7, 6]
            # [3, 9, 1, 7, 6, 8]
            # [3, 9, 1, 7, 6, 8, 4]
            # [3, 9, 1, 7, 6, 8, 4, 2]
            # [3, 9, 1, 7, 6, 8, 4, 2, 5]

            for i in range(row_start, row_end):
                for j in range(column_start, column_end):
                    if board[i][j] in lst:
                        return False
                    else:
                        lst.append(board[i][j])
    return True


def has_won(board: Board) -> bool:
    """
  Check every cell is filled and all rows, columns and grids on the board contain exactly one of each digit from 1 to 9.
  The game is won if the goal has been achieved.

    Args:
        board (Board:list[list[Optional[int]]]): the board user plays.

    Returns (bool):
    Returns True if the game is won, False otherwise.Every cell is filled and all rows, columns and squares on the board
     contain exactly one of each digit from 1 to 9.

    Examples:
    ->>> has_won(board_three)
    False
   ->>>update_board((8, 8), 5, board_three)
    ->>> board_three
    [[6, 8, 5, 1, 3, 2, 9, 4, 7],
     [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3],
     [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2],
    [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1],
     [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, 5]]
    ->>> has_won(board_three)
    True

    """
    if row_check(board) is False:
        return False
    if col_check(board) is False:
        return False
    if grid_check(board) is False:
        return False
    return True


def main():
    """
    The main function would be called when the file is run, and coordinates the overall gameplay.
    Returns:
    1.prompt user board filename .
    2.Load and convert to readable format .
    3.(1) Print the user-friendly format.
      (2) Prompt player for an action ( Clear,Quit ,Help).
    4.Notification of game has won via  message .
    5.Promotion to the user whether they'd like to play again or not .
    
    """
    renew = True  # assign variable to let user play again
    # set up
    while renew is True:
        filename = load_board(input(START_GAME_PROMPT))  # Prompt user for board filename.
        read_pre = read_board(filename)  # Original File
        read_twice = read_board(filename)  # Copy to determine which value is given in oder to process following steps
    # Move
        while has_won(read_pre) is not True:
            print_board(read_pre)
            user_input = input(INPUT_PROMPT).split()  # when user input variable to move
            if len(user_input) == 1 and (user_input[0] == 'H' or user_input[0] == 'h'):
                print(HELP_MESSAGE)
                print()
            elif len(user_input) == 1 and (user_input[0] == 'Q' or user_input[0] == 'q'):  # when user want to quit game
                return
            # Before make change cell check if there are any values in cell
            elif len(user_input) == 3 and is_empty([int(user_input[0]),int(user_input[1])] ,read_twice) is True:
                if user_input[2] == CLEAR:  # implement clear function when user want to clear just update value
                    clear_position([int(user_input[0]),int(user_input[1])] ,read_pre)
                else:
                    update_board([int(user_input[0]), int(user_input[1])], int(user_input[2]), read_pre)
            else:
                print(INVALID_MOVE_MESSAGE)

        else:
            print_board(read_pre)
            print(WIN_MESSAGE)
            response = input(NEW_GAME_PROMPT)  # Prompt user for whether they'd like to play again or not
            if response == 'Y' or response == 'y':
                renew = True
            else:
                break


if __name__ == "__main__":
    main()
