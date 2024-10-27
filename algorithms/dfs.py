from node import Node
from frontier import Frontier
from utils import Utils

class DFS:

    def __init__(self):
        pass


    def start_dfs(state):
        node_expanded = 0
        search_depth = 0
        path = []
        visited = set()

        root = Node((state,"none"),-1,Utils.get_children(state),"none")
        frontier = Frontier()

        frontier.push_back(root)
        visited.add(root.state[0])
        print("let him cook")
        while not frontier.is_empty():
            print("DO NOT WORRY I'M WORKING :), GIMME SOME TIME!!")
            cur_node = frontier.pop_back()
            node_expanded += 1

            if(Utils.is_goal(cur_node.state[0])):
                path = Utils.get_path(cur_node)
                return path, node_expanded, len(path)
            
            for child_state in cur_node.children:
                child_node = Node(child_state,cur_node,Utils.get_children(child_state[0]),child_state[1])
                if(child_state[0] not in visited):
                    visited.add(child_state[0])
                    frontier.push_back(child_node)
        
        return [],-1,-1



if __name__ == "__main__":
    path,node_expanded,search_depth = DFS.start_dfs("123456078")
    print(path)
    print(node_expanded)
    print(search_depth)
        