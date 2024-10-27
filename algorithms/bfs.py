from node import Node
from frontier import Frontier
from utils import get_children, get_path, is_goal
from algorithms.base import Algorithm

class BFS (Algorithm):
                         
    def search(self):
        state = self.state
        node_expanded = 0
        path = []
        visited = set()

        root = Node((state, "none"), -1, get_children(state), "none")
        frontier = Frontier()

        frontier.push_back(root)
        visited.add(root.state[0])
        print("let him cook")
        while not frontier.is_empty():
            print("DO NOT WORRY I'M WORKING :), GIMME SOME TIME!!")
            cur_node = frontier.pop_front()
            node_expanded += 1

            if is_goal(cur_node.state[0]):
                path = get_path(cur_node)
                return path, node_expanded, len(path)

            for child_state in cur_node.children:
                child_node = Node(child_state, cur_node, get_children(child_state[0]), child_state[1])
                if child_state[0] not in visited:
                    visited.add(child_state[0])
                    frontier.push_back(child_node)

        return [], -1, -1