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
    게임 진행을 시작한다. finshed랑 finish_token 리펙토링 하기
    """
    def play(self):
        finish_token = 2
        while finish_token:
            if self.time%2:
                user = self.user2
            else:
                user = self.user1
            self.time += 1
            places = self.board.get_color_place(user.get_color())
            if not places:
                finish_token -= 1
                continue
            finish_token = 2
            
            print("now turn's color -", user.get_color())
            print("you can put on these sites:", places)
            self.board.show()
            #tm.sleep(0.5)
            x, y = places.pop()
            self.put_a_piece(x, y, user.get_color())
        
            #user.put_a_piece_by_input()
        print()
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
    플레이어가 턴이 끝났을때 끝났다고 보고
    """
    def next_turn(self):
        self.time += 1
    
    """
    게임 종료
    """
    def game_end(self):
        pass