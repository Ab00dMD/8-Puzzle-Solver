from node import Node
from frontier import Frontier
from utils import get_children, get_path, is_goal

class IDS:

    def start_ids(state):
        node_expanded = 0
        path = []

        print("let him cook")
        
        limit = 0
        while limit < 50:
            print(limit)
            root = Node((state,"none"), -1, get_children(state), "none", 0)
            frontier = Frontier()
            visited = set()
            mp = dict()
            frontier.push_back(root)
            visited.add(root.state[0])
            mp[root.state[0]] = 0
            while not frontier.is_empty(): 
                #print("DO NOT WORRY I'M WORKING :), GIMME SOME TIME!!")
                cur_node = frontier.pop_back()
                node_expanded += 1

                if(is_goal(cur_node.state[0])):
                    path = get_path(cur_node)
                    return path, node_expanded, len(path[-1])
                
                for child_state in cur_node.children:
                    child_node = Node(child_state, cur_node, get_children(child_state[0]), child_state[1], 0, cur_node.depth + 1)
                    if(child_node.depth <= limit):
                        if(child_node.state[0] not in visited):
                            visited.add(child_state[0])
                            frontier.push_back(child_node)
                            mp[child_node.state[0]] = child_node.depth
                        else:
                            if(mp[child_node.state[0]] > child_node.depth):
                                frontier.push_back(child_node)
                                mp[child_node.state[0]] = child_node.depth

            limit += 1
        
        return [],-1,-1



if __name__ == "__main__":
    path,node_expanded,search_depth = DFS.start_dfs("123456078")
    print(path)
    print(node_expanded)
    print(search_depth)
        