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

    def build_move_tree(self):
        tree = [self._root]

        while len(tree) > 0:
            node = tree.pop(0)
            moves = self.new_move_positions(node.value)
            for move in moves:
                possible = Node(move)
                node.add_child(possible)
                tree.append(possible)
    
    def find_path(self, end_position):
        node = self._root.breadth_search(end_position)
        list = [pos.value for pos in self.trace_to_root(node)]
        return list
    
    def trace_to_root(self, end_node):
        list = []
        current = end_node
        while current != None:
            list.append(current)
            if current.parent != None:
                current = current.parent
            else:
                current = None
        return list



# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder._root.children)   # [<tree.Node object at 0x108fc6520>, <tree.Node object at 0x108fc6850>]

finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((2, 1)))  # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3)))  # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
# => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
print(finder.find_path((7, 6)))
