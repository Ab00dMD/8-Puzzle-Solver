import time

from node import Node
from frontier import Frontier
from utils import get_children, get_path, is_goal
from algorithms.base import Algorithm

class IDS(Algorithm):
    def __init__(self, state):
        super().__init__(state)

    def search(self):
        start_time = time.time()
        state = self.state
        path = []

        print("let him cook")
        
        limit = 0
        while limit < 50:
            print(limit)
            root = Node((state,"none"), -1, get_children(state), "none")
            
            result, path, cost, depth, node_expanded = self.dsl(root,limit,1)
            if(result):
                running_time = time.time() - start_time
                return {
                    "path": path,
                    "cost": cost,
                    "nodes_expanded": node_expanded,
                    "max_search_depth": depth,
                    "running_time": running_time
                }                
            limit += 1
        
        return [],-1,-1
    

    def dsl(self,cur_node,limit,nodes_expanded):
        if(is_goal(cur_node.state[0])):
            return True, get_path(cur_node), cur_node.cost, cur_node.depth, nodes_expanded
        
        for child_state in cur_node.children:
            child_node = Node(child_state, cur_node, get_children(child_state[0]), child_state[1], cur_node.cost + 1, cur_node.depth + 1)
            if(child_node.depth <= limit):
               result, path, cost, depth, nodes_expanded = self.dsl(child_node,limit,nodes_expanded + 1)

               if(result):
                   return result, path, cost, depth, nodes_expanded
        
        return None



if __name__ == "__main__":
    path,node_expanded,search_depth = DFS.start_dfs("123456078")
    print(path)
    print(node_expanded)
    print(search_depth)
        