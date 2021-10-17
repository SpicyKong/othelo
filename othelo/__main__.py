from othelo.board import Board
from othelo.game import Game
from othelo.piece import Piece
from othelo.rule import Rule
from othelo.user import User

if __name__ == '__main__':
    """
    Game(User('user1'), User('user2'), Board(8))
    print(Game)
    print(Piece)
    print(Rule)
    print(Board)
    print(User)"""
    board = Board(8)
    for y in range(8):
        for x in range(8):
            print(board.can_place(x, y, 0), end=" ")
        print()
            