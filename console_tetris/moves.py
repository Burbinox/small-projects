from copy import deepcopy


def get_left_move(piece_pos):
    """
    :param piece_pos: position of piece on the board
    :return: new_piece_pos: new position of the piece shifted to the left
    """

    new_piece_pos = [piece_pos[0], piece_pos[1] - 1]
    return new_piece_pos


def get_right_move(piece_pos):
    """
    :param piece_pos: position of piece on the board
    :return: new_piece_pos: new position of the piece shifted to the left
    """
    # Shift the piece right by 1 unit
    new_piece_pos = [piece_pos[0], piece_pos[1] + 1]
    return new_piece_pos


def get_down_move(piece_pos):
    """
    :param piece_pos: position of piece on the board
    :return: new_piece_pos: new position of the piece shifted to the left
    """
    new_piece_pos = [piece_pos[0] + 1, piece_pos[1]]
    return new_piece_pos


def rotate_clockwise(piece):
    """
    :param piece: matrix of the piece to rotate
    :return: Clockwise rotated piece
    """
    piece_copy = deepcopy(piece)
    reverse_piece = piece_copy[::-1]
    return list(list(elem) for elem in zip(*reverse_piece))


def rotate_anticlockwise(piece):
    """
    :param piece: matrix of the piece to rotate
    :return: counter clockwise rotated piece
    """
    piece_copy = deepcopy(piece)
    # Rotating clockwise three times will be same as rotating counter clockwise
    piece_1 = rotate_clockwise(piece_copy)
    piece_2 = rotate_clockwise(piece_1)
    return rotate_clockwise(piece_2)
