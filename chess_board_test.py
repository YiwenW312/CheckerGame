from chess_board import ChessBoard


def test_constructor():
    board = ChessBoard(120, 8, "crown")
    assert board.cell_size == 120
    assert len(board.checkers_red) == 12


def test_move_checker():
    board = ChessBoard(120, 8, "crown")
    checker = board.checkers_red[11]
    board.move_checker(checker, 0, 0)
    assert checker.x == 0
    assert checker.y == 0


def test_jumpable():
    board = ChessBoard(120, 8, "crown")
    checker = board.checkers_red[11]
    jump_list = board.jumpable(checker)
    assert len(jump_list) == 0


def test_achievable():
    board = ChessBoard(120, 8, "crown")
    checker = board.checkers_red[11]
    achieve_list = board.achievable(checker)
    assert len(achieve_list) == 1


def test_delete_checker():
    board = ChessBoard(120, 8, "crown")
    checker = board.checkers_red[11]
    board.delete_checker(checker)
    assert len(board.checkers_red) == 11


def test_king():
    board = ChessBoard(120, 8, "crown")
    checker = board.checkers_red[11]
    board.king(checker)
    assert not checker.is_king
