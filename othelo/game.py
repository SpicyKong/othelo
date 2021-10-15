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
    
    