from utils import print_board, get_children
from algorithms.dfs import DFS
from algorithms.ids import IDS
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
    path,node_expanded,search_depth = IDS.start_ids("641302758")
    print(path)
    print(node_expanded)
    print(search_depth)
        