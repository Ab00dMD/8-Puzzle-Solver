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
        node_expanded = 0
        path = []

        print("let him cook")
        
        limit = 0
        while limit < 50:
            print(limit)
            root = Node((state,"none"), -1, get_children(state), "none")
            frontier = Frontier()
            mp = dict()
            frontier.push_back(root)
            mp[root.state[0]] = 0
            while not frontier.is_empty(): 
                cur_node = frontier.pop_back()
                node_expanded += 1

                if(is_goal(cur_node.state[0])):
                    path = get_path(cur_node)
                    running_time = time.time() - start_time
                    return {
                        "path": path,
                        "cost": cur_node.cost,
                        "nodes_expanded": node_expanded,
                        "max_search_depth": cur_node.depth,
                        "running_time": running_time
                    }
                
                for child_state in cur_node.children:
                    child_node = Node(child_state, cur_node, get_children(child_state[0]), child_state[1], cur_node.cost + 1, cur_node.depth + 1)
                    if(child_node.depth <= limit):
                        if((child_node.state[0] not in mp) or (mp[child_node.state[0]] > child_node.depth)):
                            frontier.push_back(child_node)
                            mp[child_node.state[0]] = child_node.depth

            limit += 1
        
        return [],-1,-1



if __name__ == "__main__":
    path,node_expanded,search_depth = DFS.start_dfs("123456078")
    print(path)
    print(node_expanded)
    print(search_depth)
        