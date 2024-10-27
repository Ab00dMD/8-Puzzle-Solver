from Node import Node

class Frontier:
    def __init__(self):
        self.frontier = []


    def add(self,item):
        self.frontier.append(item)

    def pop(self):
        if not self.is_empty():
            return self.frontier.pop()
        else:
            raise RuntimeError("frontier is empty")
        
    def is_empty(self):
        return len(self.frontier) == 0
    
    def size(self):
        return len(self.frontier)