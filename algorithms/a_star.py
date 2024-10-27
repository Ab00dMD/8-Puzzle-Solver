from node import Node
from algorithms.base import Algorithm
from queue import PriorityQueue
from utils import get_children, is_goal, get_path

class AStar(Algorithm):
  def __init__(self, state, heuristic):
    self.node = Node(state, -1, [], None)
    self.heuristic = heuristic
    self.pq = PriorityQueue()

  def search(self):
    self.pq.put((self.__evaluation(self.node), self.node))
    visited = set()
    visited.add(self.node.state)
    while not self.pq.empty():
      cur_node = self.pq.get()[1]
      if is_goal(cur_node.state):
        return get_path(cur_node)
      for child_state, direction in get_children(cur_node.state):
        child_node = Node(child_state, cur_node, [], direction, cur_node.cost + 1)
        if child_state not in visited:
          visited.add(child_state)
          self.pq.put((self.__evaluation(child_node), child_node))
    return None
    

  def __evaluation(self, node):
    return node.cost + self.__heuristic(node.state)
  
  def __heuristic(self, state):
    for tile in state:
      if tile != "0":
        current = state.index(tile)
        cur_x = current % 3
        cur_y = current // 3
        goal = int(tile)
        goal_x = goal % 3
        goal_y = goal // 3
        return abs(cur_x - goal_x) + abs(cur_y - goal_y) if self.heuristic == "manhattan" else ((cur_x - goal_x) ** 2 + (cur_y - goal_y) ** 2) ** 0.5
        
        
    
    
