import moves


def is_game_over(board, curr_piece, piece_pos):
    """

    :param board: matrix of the size of the board
    :param curr_piece: matrix for the piece active in the game
    :param piece_pos: [x,y] co-ordinates of the top-left cell in the piece matrix
                        w.r.t. the board
    :return:
            True - if game is over
            False - if game is live and player can still move
    """
    # If the piece cannot move down and the position is still the first row
    # of the board then the game has ended
    if not can_move_down(board, curr_piece, piece_pos) and piece_pos[0] == 0:
        return True
    return False


def overlap_check(board, curr_piece, piece_pos):
    """

    :param board: matrix of the size of the board
    :param curr_piece: matrix for the piece active in the game
    :param piece_pos: [x,y] co-ordinates of the top-left cell in the piece matrix
                        w.r.t. the board
    :return:
            True - if piece do not overlap with any other piece or walls
            False - if piece overlaps with any other piece or board walls
    """
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            if board[piece_pos[0]+i][piece_pos[1]+j] == 1 and curr_piece[i][j] == 1:
                return False
    return True


def can_move_left(board, curr_piece, piece_pos):
    """

    :param board: matrix of the size of the board
    :param curr_piece: matrix for the piece active in the game
    :param piece_pos: [x,y] co-ordinates of the top-left cell in the piece matrix
                        w.r.t. the board
    :return:
            True - if we can move the piece left
            False - if we cannot move the piece to the left
    """
    piece_pos = moves.get_left_move(piece_pos)
    return overlap_check(board, curr_piece, piece_pos)


def can_move_right(board, curr_piece, piece_pos):
    """

    :param board: matrix of the size of the board
    :param curr_piece: matrix for the piece active in the game
    :param piece_pos: [x,y] co-ordinates of the top-left cell in the piece matrix
                        w.r.t. the board
    :return:
            True - if we can move the piece right
            False - if we cannot move the piece to the right
    """
    piece_pos = moves.get_right_move(piece_pos)
    return overlap_check(board, curr_piece, piece_pos)


def can_move_down(board, curr_piece, piece_pos):
    """

    :param board: matrix of the size of the board
    :param curr_piece: matrix for the piece active in the game
    :param piece_pos: [x,y] co-ordinates of the top-left cell in the piece matrix
                        w.r.t. the board
    :return:
            True - if we can move the piece down
            False - if we cannot move the piece down
    """
    piece_pos = moves.get_down_move(piece_pos)
    return overlap_check(board, curr_piece, piece_pos)


def can_rotate_anticlockwise(board, curr_piece, piece_pos):
    """

    :param board: matrix of the size of the board
    :param curr_piece: matrix for the piece active in the game
    :param piece_pos: [x,y] co-ordinates of the top-left cell in the piece matrix
                        w.r.t. the board
    :return:
            True - if we can move the piece anti-clockwise
            False - if we cannot move the piece anti-clockwise
    """
    curr_piece = moves.rotate_anticlockwise(curr_piece)
    return overlap_check(board, curr_piece, piece_pos)


def can_rotate_clockwise(board, curr_piece, piece_pos):
    """

    :param board: matrix of the size of the board
    :param curr_piece: matrix for the piece active in the game
    :param piece_pos: [x,y] co-ordinates of the top-left cell in the piece matrix
                        w.r.t. the board
    :return:
            True - if we can move the piece clockwise
            False - if we cannot move the piece clockwise
    """
    curr_piece = moves.rotate_clockwise(curr_piece)
    return overlap_check(board, curr_piece, piece_pos)
