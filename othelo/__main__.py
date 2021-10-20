from othelo.board import Board
from othelo.game import Game
from othelo.piece import Piece
from othelo.user import User

if __name__ == '__main__':
    """
    Game(User('user1'), User('user2'), Board(8))
    print(Game)
    print(Piece)
    print(Rule)
    print(Board)
    print(User)
    
    board = Board(8)
    board.show()
    print()
    
    
    x, y = board.get_color_place(0).pop()
    #print(board.get_color_place(0))
    board.put_a_piece(x, y, Piece(0))
    board.update(x, y)
    for y in range(8):
        for x in range(8):
            print(board.can_place(x, y, 0), end=" ")
        print()
    board.show()"""
    g = Game(User('user1'), User('user2'), Board(8))
    g.play()