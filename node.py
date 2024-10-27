class Node:
    def __init__(self,state,parent,children,direction,depth):
        self.state = state
        self.parent = parent
        self.children = children
        self.direction = direction
        self.depth = depth