class Node:
    def __init__(self, state, parent, children, direction, cost=0):
        self.state = state
        self.parent = parent
        self.children = children
        self.direction = direction
        self.cost = cost