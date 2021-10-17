class User:
    username = None
    color = None
    game = None
    
    def __init__(self, username, game):
        self.username = username
        self.game = game
    
    def set_turn(self, color):
        self.color = color
    
    """
    Piece 객체 하나를 (x, y) 칸에 둔다.
    put_a_piece(self, x, y, color):
    """
    def put_a_piece(self, x, y):
        self.game.put_a_piece(x, y, self.color)
    
    """
    내 턴을 진행한다
    
    내 턴 >
    둘 수 있는 위치를 물어봄 >
    둘 수 있는 위치 중 하나를 선택 함 >
    그 위치에 돌을 둠 >
    턴 종료 >
    를 무한 반복.
    
    Where can i place
    """
    def my_turn(self, wcip):
        pass
    
    """
    (x, y) 위치에 게임 말을 둔다.
    """
    def put_a_piece(self, x, y):
        game.put_a_piece(x, y, color)
    
    """
    내 말의 색을 반환한다.
    """
    def get_color(self):
        return color
    
    def turn_end(self):
        game.next_turn()