# the state will be stored as a number 125304678 to represent a board or 3*3
# board 125
#       304
#       678
# empty tile is 0


from utils import print_board, get_children


def main():
    print("Welcome to the 8-Puzzle Solver! please input the initial state of the board:")
    number = input()
    
    print_board(number)
    
    children = get_children(number)
    
    print("Children of the current state:")
    for child in children:
        print(child)
        # print_board(child)
        # print("\n")

if __name__ == "__main__":
    main()