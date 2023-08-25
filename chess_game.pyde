from chess_board import ChessBoard
from game_controller import GameController
CELL_SIZE = 120
BOARD_SIZE = 8


def setup():
    """setup the chess game"""
    global gc
    size(CELL_SIZE * BOARD_SIZE + 1, CELL_SIZE * BOARD_SIZE + 1)
    crown = loadImage("crown.png")
    board = ChessBoard(CELL_SIZE, BOARD_SIZE, crown)
    gc = GameController(board)


def draw():
    gc.update(mousePressed, mouseX, mouseY)


def mouseReleased():
    gc.place_checker(mouseX, mouseY)


def mousePressed():
    gc.pick_checker(mouseX, mouseY)


def draw_checker():
    """draw the checker"""
    ellipses()
    strokeWeight(STROKEWEIGHT)
    stroke()


def draw_king_checker():
    """draw the king checker"""
    image(img)
    ellipses()
    strokeWeight(STROKEWEIGHT)
    stroke()
