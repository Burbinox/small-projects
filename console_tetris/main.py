import random
from copy import deepcopy
import setup
import validators as vl
import moves

BOARD_SIZE = 20

# Extra two are for the walls, playing area will have size as BOARD_SIZE
EFF_BOARD_SIZE = BOARD_SIZE + 2

PIECES = [

    [[1], [1], [1], [1]],

    [[1, 0],
     [1, 0],
     [1, 1]],

    [[0, 1],
     [0, 1],
     [1, 1]],

    [[0, 1],
     [1, 1],
     [1, 0]],

    [[1, 1],
     [1, 1]]

]

# Constants for user input
MOVE_LEFT = 'a'
MOVE_RIGHT = 'd'
ROTATE_ANTICLOCKWISE = 'w'
ROTATE_CLOCKWISE = 's'


def print_board(board, curr_piece, piece_pos, error_message=''):
    """

    :param board: matrix of the size of the board
    :param curr_piece: matrix for the piece active in the game
    :param piece_pos: [x,y] co-ordinates of the top-left cell in the piece matrix
                        w.r.t. the board
    :param error_message:
    :return:
    """
    board_copy = deepcopy(board)
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            board_copy[piece_pos[0]+i][piece_pos[1]+j] = curr_piece[i][j] | board[piece_pos[0]+i][piece_pos[1]+j]

    # Print the board to STDOUT
    for i in range(EFF_BOARD_SIZE):
        for j in range(EFF_BOARD_SIZE):
            if board_copy[i][j] == 1:
                print("*", end='')
            else:
                print(" ", end='')
        print("")

    print(" - a (return): move piece left")
    print(" - d (return): move piece right")
    print(" - w (return): rotate piece counter clockwise")
    print(" - s (return): rotate piece clockwise")

    if error_message:
        print(error_message)
    print("Your move: ", end="")


def get_random_piece():
    idx = random.randrange(len(PIECES))
    return PIECES[idx]


def get_random_position(curr_piece):
    """

    :param curr_piece: piece which is alive in the game at the moment
    :return: a randomly (along x-axis) chosen position for this piece
    """
    curr_piece_size = len(curr_piece)

    # This x refers to rows, rows go along y-axis
    x = 0
    # This y refers to columns, columns go along x-axis
    y = random.randrange(1, EFF_BOARD_SIZE-curr_piece_size)
    return [x, y]


def merge_board_and_piece(board, curr_piece, piece_pos):
    """
    Fixes the position of the passed piece at piece_pos in the board
    This means that the new piece will now come into the board
    also remove any filled up rows from the board to continue the game

    :param board: matrix of the size of the board
    :param curr_piece: matrix for the piece active in the game
    :param piece_pos: [x,y] co-ordinates of the top-left cell in the piece matrix
                        w.r.t. the board
    """
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            board[piece_pos[0]+i][piece_pos[1]+j] = curr_piece[i][j] | board[piece_pos[0]+i][piece_pos[1]+j]

    # After merging the board and piece
    # If there are rows which are completely filled then remove those rows

    # Declare empty row to add later
    empty_row = [0]*EFF_BOARD_SIZE
    empty_row[0] = 1
    empty_row[EFF_BOARD_SIZE-1] = 1

    # Declare a constant row that is completely filled
    filled_row = [1]*EFF_BOARD_SIZE

    # Count the total filled rows in the board
    filled_rows = 0
    for row in board:
        if row == filled_row:
            filled_rows += 1

    # The last row is always a filled row because it is the boundary
    # So decrease the count for that one
    filled_rows -= 1

    for i in range(filled_rows):
        board.remove(filled_row)

    # Add extra empty rows on the top of the board to compensate for deleted rows
    for i in range(filled_rows):
        board.insert(0, empty_row)


def play_game():
    """
    - Initializes the game
    - Reads player move from console
    - Checks for the move validity
    - Continues the game if valid move, else prints out error msg
    - Fixes the piece position on board if it cannot be moved
    - Pops in new piece on top of the board
    - Quits if no valid moves and possible for a new piece
    """

    # Initialize the game board, piece and piece position
    board = setup.init_board(BOARD_SIZE)
    curr_piece = get_random_piece()
    piece_pos = get_random_position(curr_piece)
    print_board(board, curr_piece, piece_pos)

    player_move = input()
    while not vl.is_game_over(board, curr_piece, piece_pos):
        error_message = ""
        do_move_down = False
        if player_move == MOVE_LEFT:
            if vl.can_move_left(board, curr_piece, piece_pos):
                piece_pos = moves.get_left_move(piece_pos)
                do_move_down = True
            else:
                error_message = "Cannot move left!"
        elif player_move == MOVE_RIGHT:
            if vl.can_move_right(board, curr_piece, piece_pos):
                piece_pos = moves.get_right_move(piece_pos)
                do_move_down = True
            else:
                error_message = "Cannot move right!"
        elif player_move == ROTATE_ANTICLOCKWISE:
            if vl.can_rotate_anticlockwise(board, curr_piece, piece_pos):
                curr_piece = moves.rotate_anticlockwise(curr_piece)
                do_move_down = True
            else:
                error_message = "Cannot rotate anti-clockwise !"
        elif player_move == ROTATE_CLOCKWISE:
            if vl.can_rotate_clockwise(board, curr_piece, piece_pos):
                curr_piece = moves.rotate_clockwise(curr_piece)
                do_move_down = True
            else:
                error_message = "Cannot rotate clockwise!"
        else:
            error_message = "That is not a valid move!"

        if do_move_down and vl.can_move_down(board, curr_piece, piece_pos):
            piece_pos = moves.get_down_move(piece_pos)

        # This means the current piece in the game cannot be moved
        # We have to fix this piece in the board and generate a new piece
        if not vl.can_move_down(board, curr_piece, piece_pos):
            merge_board_and_piece(board, curr_piece, piece_pos)
            curr_piece = get_random_piece()
            piece_pos = get_random_position(curr_piece)

        # Redraw board
        print_board(board, curr_piece, piece_pos, error_message=error_message)
        player_move = input()

    print("GAME OVER!")


if __name__ == "__main__":
    play_game()
