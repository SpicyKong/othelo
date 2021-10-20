from othelo.piece import Piece
import time as tm
class Game:
    user1 = None
    user2 = None
    board = None
    time = None
    finished = None
    
    def __init__(self, user1, user2, board):
        self.user1 = user1
        self.user2 = user2
        self.board = board
        self.finished = False
        user1.set_turn(0)
        user2.set_turn(1)
        user1.set_game(self)
        user2.set_game(self)
        self.time = 0
    
    """
    게임 진행을 시작한다.
    우선 임시로 직접 입력을 받아 말을 위치시킨다.
    """
    def play(self):
        while not self.is_done():
            if self.time%2:
                user = self.user2
            else:
                user = self.user1
            self.time += 1
            print("score : ", self.get_score(self.user1), " : ", self.get_score(self.user2))
            print("now turn's color -", user.get_color())
            self.board.show()
        
            user.put_a_piece_by_input()
        self.board.show()
        
    """
    (x, y)위치에 color 색의 게임말을 둔다.
    """
    def put_a_piece(self, x, y, color):
        
        if not self.board.can_place(x, y, color):
            return False
        
        p = Piece(color)
        
        self.board.put_a_piece(x, y, p)
        
        return True
    
    def get_color_place(self, color):
        return self.board.get_color_place(color)
    
    """
    게임이 끝났다면 True 아니라면 False
    """
    def is_done(self):
        if self.board.get_color_place(0) or self.board.get_color_place(1):
            return False
        return True
    
    def get_score(self, user):
        color = user.get_color()
        size = self.board.get_size()
        ret = 0
        for y in range(size):
            for x in range(size):
                piece = self.board.get_piece(x, y)
                if piece is None:
                    continue
                if piece.get_color() == color:
                    ret += 1
        return ret