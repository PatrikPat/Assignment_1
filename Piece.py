class Piece:
    def __init__(self, team, position, rank):
        self.team = team
        self.position = position  # type list
        self.rank = rank

    def __repr__(self):
        return "<Piece team:%s position:%s rank:%s>" % (self.team, self.position, self.rank)

    def __str__(self):
        return "Piece team: %s, position: %s, rank: %s" % (self.team, self.position, self.rank)

    def print_piece(self):
        return "%s%s" % (self.team, self.rank)

    def compare_pieces(self, piece):
        if piece.rank == 'B':
            if self.rank == 3:
                return 'Enemy'
            else:
                return 'Player'
        elif self.rank == 1 and piece.rank == 10:
            return 'Enemy'
        elif piece.rank == 'F':
            return 'Victory'
        elif self.rank > piece.rank:
            return 'Enemy'
        elif self.rank == piece.rank:
            return [piece, self]
        else:
            return 'Player'

    def move(self, new_position):
        self.position = new_position

    def remove(self):
        self.position = []



