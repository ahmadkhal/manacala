class Mancala:
    def __init__(self, holes, seeds):
        self.mancala_table = [[seeds, seeds] for i in range(holes)]
        self.player1_hole = 0
        self.player2_hole = 0
        self.player_turn = 1



