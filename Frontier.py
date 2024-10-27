from node import Node
import collections 
class Frontier:
    def __init__(self):
        self.frontier = collections.deque()


    def push_back(self,item):
        self.frontier.append(item)


    def push_front(self,item):
        self.frontier.appendleft(item)


    def pop_back(self):
        if not self.is_empty():
            return self.frontier.pop()
        else:
            raise RuntimeError("frontier is empty")
        

    def pop_front(self):
        if not self.is_empty():
            return self.frontier.popleft()
        else:
            raise RuntimeError("frontier is empty")



    def is_empty(self):
        return len(self.frontier) == 0
    
    
    def size(self):
        return len(self.frontier)