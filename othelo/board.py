class Board:
    side = None
    board = None
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    
    """
    0 0 0
    0   0
    0 0 0
    
    백2개 흑2개 초기 중앙에 위치 시키는것도 추가 해야한다.
    """
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        
    
    """
    게임 말을 (x, y)에 위치 시킨다.
    """
    def put_a_piece(self, x, y, piece):
        self.board[y][x] = piece
        
    """
    color 색의 게임 말을 둘 수 있는 위치들을 알려준다.(set으로 반환)
    """
    def get_color_place(self, color):
        places = set()
        for y in range(size):
            for x in range(size):
                pass
    
    """
    해당 지역에 둘 수 있다면 둔다.
    """
    def can_place(self, x, y, color):
        if self.board[y][x] is None:
            return False
        
        for i in range(8):
            nx, ny = x, y
            chk = color
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= size or ny < 0 or ny >= size:
                    continue
                if self.board[y][x] is None:
                    break
                if color == self.board[ny][nx].get_color() and chk:
                    return True
                #chk ^= self.board[ny][nx].get_color()
        return False
            
            
                    
    
    """
    보드 판의 현 상황을 보여준다.
    """
    def show(self):
        pass
    
    """
    (x, y) 위치에 둔 게임 말로 인해 변경될 사항들을 반영 한다.
    """
    def update(self, x, y):
        pass