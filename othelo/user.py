class User:
    username = None
    color = None
    game = None
    
    def __init__(self, username):
        self.username = username
    
    def set_game(self, game):
        self.game = game
    
    
    def set_turn(self, color):
        self.color = color
    
    """
    Piece 객체 하나를 (x, y) 칸에 둔다.
    put_a_piece(self, x, y, color):
    """
    def put_a_piece(self, x, y):
        self.game.put_a_piece(x, y, self.color)=
        
    """
    (x, y) 위치에 게임 말을 둔다.
    """
    def put_a_piece(self, x, y):
        game.put_a_piece(x, y, color)
    
    """
    내 말의 색을 반환한다.
    """
    def get_color(self):
        return self.color
        
    def put_a_piece_by_input(self):
        x, y = -1, -1
        while not self.game.put_a_piece(x, y, self.color):
            x, y, = map(int, input().split())
        