class Piece:
    color = None
    
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def change_color(self):
        self.color = not self.color
        
    def __repr__(self):
        return str(self.color)