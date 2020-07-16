from tree import Node

class KnightPathFinder:
    def __init__(self, c):
        self._root = Node(c)
        self._considered_positions = set(c)

    def get_valid_moves(self, pos):
        possible = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        moves = []
        x, y = pos

        for a, b in possible:
            newPos = (x + a, y + b)
            newX, newY = newPos
            if newX in range(8) and newY in range(8):
                moves.append(newPos)
        
        return moves

    def new_move_positions(self, pos):
        considered = self._considered_positions
        possible_moves = set(self.get_valid_moves(pos)) - considered
        self._considered_positions = considered | possible_moves
        return possible_moves



finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))
