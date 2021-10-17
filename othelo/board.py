from othelo.piece import Piece
class Board:
    size = None
    board = None
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    
    """
    0 0 0
    0   0
    0 0 0
    
    백2개 흑2개 초기 중앙에 위치 시키는것도 추가 해야한다.
    백 흑
    흑 백
    """
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        mid = (size-1)//2
        
        self.put_a_piece(mid, mid, Piece(1))
        self.put_a_piece(mid+1, mid+1, Piece(1))
        self.put_a_piece(mid+1, mid, Piece(0))
        self.put_a_piece(mid, mid+1, Piece(0))
        
    
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
        for y in range(self.size):
            for x in range(self.size):
                if self.can_place(x, y, color):
                    places.add((x, y))
        return places
    
    """
    (x, y) 위치에 말을 둘 수 있는지 여부를 반환 한다.
    """
    def can_place(self, x, y, color):
        piece = self.get_piece(x, y)
        if piece is not None:
            return False
        for i in range(8):
            nx, ny = x+self.dx[i], y+self.dy[i]
            check = 0
            piece = piece = self.get_piece(nx, ny) ############# 여기
            while piece and not piece.get_color() == color:
                check = 1
                #print(nx, ny)
                piece = self.get_piece(nx, ny)
                nx += self.dx[i]
                ny += self.dy[i]
                
            if piece is not None and piece.get_color() == color and check:
                return True
        return False
        
    
    """
    (x, y) 위치에 둔 게임 말로 인해 변경될 사항들을 반영 한다.
    """
    def update(self, x, y):
        piece = self.get_piece(x, y)
        color = piece.get_color()
        if piece is None:
            return
        for i in range(8):
            nx, ny = x+self.dx[i], y+self.dy[i]
            piece = self.get_piece(nx, ny)
            tmp = []
            
            while (piece is not None) and (not piece.get_color() == color):
                nx += self.dx[i]
                ny += self.dy[i]
                if nx < 0 or nx >= self.size or ny < 0 or ny >= self.size:
                    break
                tmp.append((nx, ny))
                piece = self.get_piece(nx, ny)
            
            if (piece is None) or (not piece.get_color() == color) or (not check):
                continue
            
            while tmp:
                nx, ny = tmp.pop()
                piece = self.get_piece(nx, ny)
                piece.change_color()
                
            
                    
    
    """
    보드 판의 현 상황을 보여준다.
    """
    def show(self):
        
        for y in range(self.size):
            for x in range(self.size):
                piece = self.get_piece(x, y)
                value = '.'
                if piece is not None:
                    value = str(piece.get_color())
                print(value, end = " ")
            print()
                
    
    
    
    """
    (x, y) 위치에 있는 게임 말 인스턴스를 반환한다.
    (없다면 None)
    """
    def get_piece(self, x, y):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return None
        return self.board[y][x]