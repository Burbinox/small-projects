def init_board(board_size):
    """
    :param board_size: the board size
    :return: board - the matrix with the walls of the board
    """
    frame_board_size = board_size + 2
    board = [[0 for x in range(frame_board_size)] for y in range(frame_board_size)]
    for i in range(frame_board_size):
        board[i][0] = 1
    for i in range(frame_board_size):
        board[frame_board_size-1][i] = 1
    for i in range(frame_board_size):
        board[i][frame_board_size-1] = 1
    return board
