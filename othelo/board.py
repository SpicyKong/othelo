class Board:
    side = None
    board = None
    
    
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
    
    """
    설명:
        게임 말을 (x, y)에 위치 시킨다.
    """
    def put_a_piece(self, x, y, piece):
        self.board[y][x] = piece
        
    """
    설명:
        uesr가 게임 말을 둘 수 있는 위치들을 알려준다.
    """
    def get_place(self, color):
        pass