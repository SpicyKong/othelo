class User:
    username = None
    turn = None
    
    def __init__(self, username):
        self.username = username
    
    def set_turn(self, turn):
        self.turn = turn
        
    def put_a_piece(self, x, y):
        pass
    
    