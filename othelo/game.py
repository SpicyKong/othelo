class Game:
    user1 = None
    user2 = None
    board = None
    time = None
    
    def __init__(self, user1, user2, board):
        self.user1 = user1
        self.user2 = user2
        self.board = board
        user1.set_turn(0)
        user2.set_turn(1)
        time = 0
    
    """
    게임 진행을 시작한다.
    """
    def play(self):
        pass
    
    """
    (x, y)위치에 color 색의 게임말을 둔다.
    """
    def put_a_piece(self, x, y, color):
        pass
    
    def get_color_place(self, color):
        return board.get_color_place(color)
    
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