class Node:
    def __init__(self, state, parent, children, direction, cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.children = children
        self.direction = direction
        self.cost = cost
        self.depth = depth

    def __lt__(self, other):
        return self.cost < other.cost