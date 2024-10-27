# the state will be stored as a number 125304678 to represent a board or 3*3
# board 125
#       304
#       678
# empty tile is 0

from utils import print_board, get_children
from algorithms.dfs import DFS
from algorithms.bfs import BFS

def main():
    print("Welcome to the 8-Puzzle Solver! please input the initial state of the board:")
    number = input()
    
    print_board(number)
    
    children = get_children(number)
    
    print("Children of the current state:")
    for child in children:
        print(child)

if __name__ == "__main__":
    # # For DFS
    # path, node_expanded, search_depth = DFS.start_dfs("123456078")
    # print("DFS Path:", path)
    # print("DFS Nodes Expanded:", node_expanded)
    # print("DFS Search Depth:", search_depth)

    # For BFS
    BFS = BFS("806547231")
    path, node_expanded, search_depth = BFS.search()
    print("BFS Path:", path)
    print("BFS Nodes Expanded:", node_expanded)
    print("BFS Search Depth:", search_depth)