class Piece:
    def __init__(self, team: str, position: [int, int], rank: str or int):
        self.team = team # either 'R' or 'B'
        self.position = position  # type list
        self.rank = rank # one of the possible ranks

    def __repr__(self):
        return "<Piece team:%s position:%s rank:%s>" % (self.team, self.position, self.rank)

    def __str__(self):
        return "Piece team: %s, position: %s, rank: %s" % (self.team, self.position, self.rank)

    def print_piece(self) -> None:
        """Function that prints a piece in the format provided in the assignment. 
        """
        return "%s%s" % (self.team, self.rank)

    def compare_pieces(self, piece) -> str or list:
        """Returns the outcome of a battle between the self piece and the piece
        that is given as argument. Returns the Player when self wins, Victory when
        self gets the flag, both pieces if there is a draw and Enemy when the 
        argument piece wins. 
        """
        # first check the exceptions and return appropriate values
        if piece.rank == 'B':
            if self.rank == 3:
                return 'Player'
            else:
                return 'Enemy'
        elif self.rank == 1 and piece.rank == 10:
            return 'Player'
        elif piece.rank == 'F':
            return 'Victory'
        
        # normal cases
        elif self.rank > piece.rank:
            return 'Player'
        elif self.rank == piece.rank:
            return [piece, self]
        elif self.rank < piece.rank:
            return 'Enemy'


