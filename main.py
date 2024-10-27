from utils import print_board, get_children
from algorithms.dfs import DFS
from algorithms.bfs import BFS
from algorithms.a_star import AStar

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
    # DFS = DFS("123456078")
    # path, node_expanded, search_depth = DFS.search()
    # print("DFS Path:", path)
    # print("DFS Nodes Expanded:", node_expanded)
    # print("DFS Search Depth:", search_depth)

    # For BFS
    bfs = BFS("123456078")
    path, node_expanded, search_depth = bfs.search()
    print("BFS Path:", path)
    print("BFS Nodes Expanded:", node_expanded)
    print("BFS Search Depth:", search_depth)

    # For AStar
    AStar = AStar("123456078", "manhattan")
    path = AStar.search()
    print("AStar Path:", path)
