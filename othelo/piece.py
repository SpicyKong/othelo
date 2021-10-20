class Piece:
    color = None
    
    """
    생성자는 게임 말의 색만 지정한다.
    """
    def __init__(self, color):
        self.color = color
    
    """
    현재 차례의 게임말 색을 반환다.
    """
    def get_color(self):
        return self.color
    
    """
    색을 반전한다.
    """
    def change_color(self):
        #self.color = not self.color
        self.color = 0 if self.color else 1
        
    def __repr__(self):
        return str(self.color)