class Algorithm:
    def __init__(self, state):
        self.state = state
        self.nodes_expanded = 0

    
    def search(self):
        raise NotImplementedError("search method is not implemented")
